import re
import pytz, boto3, datetime, os, io, base64, calendar, json, xml.etree.ElementTree as ET

from typing import Any, Tuple, Optional
from datetime import timedelta

from tzlocal import get_localzone
from ..dtos.response.enum_response import EnumStatusCode
from ..dtos.response.exception import GenericException
from imap_tools import MailMessage
from email.message import EmailMessage
from botocore.exceptions import ClientError
from ..dtos.request.user_dto import UserDtoMetadata
from ..models.user_metadata import UserMetadata
from ..models.user import User

class Utils:

    @staticmethod
    def construct_user_meta_data(current_user: User) -> UserMetadata:
        """
        construit et retourne un objet user meta data
        """
        return UserMetadata(id=current_user.id, fullname=current_user.firstname +" "+ current_user.lastname, user_id=current_user.userId, email=current_user.email)
    
    @staticmethod
    def construct_user_meta_data_dto(current_user: User) -> UserDtoMetadata:
        data = {
            '_id':str(current_user.id), 
            'email': current_user.email, 
            'firstname': current_user.firstname, 
            'lastname': current_user.lastname, 
            'enabled': None, 
            'disabledByAdmin': None, 
            'userId': current_user.userId,
        }
        return UserDtoMetadata(**data)

    def get_date_in_gmt() -> int:
        """
        convertir une date dans le fuseau horaire GMT (UTC)
        """
        # Get GMT time zone (UTC)
        gmt_timezone = pytz.timezone('UTC')

        # Get current date and time in GMT
        current_time_gmt = datetime.datetime.now(gmt_timezone)

        return current_time_gmt

    def convert_date_in_gmt_and_timstamp(date: datetime.datetime) -> int:
        """
        convertir une date dans le fuseau horaire GML puis en timestamp
        """

        # Obtenir le fuseau horaire local
        system_timezone = get_localzone()

        dt_in_system_timezone = date.astimezone(system_timezone)

        # Convertir en GMT (UTC)
        new_timezone = pytz.timezone("UTC")
        date_in_gmt = dt_in_system_timezone.astimezone(new_timezone)

        # Obtenir le timestamp (en secondes depuis l'époque)
        date_timestamp = int(date_in_gmt.timestamp())

        return date_timestamp

    def get_file_extension(file):
        file_name = file.filename
        file_extension = file_name.split('.')[-1] if '.' in file_name else None
        return file_extension

    @staticmethod
    def get_unique_key(s3_client, bucket_name, destination_prefix, file_name):
        base_name, extension = os.path.splitext(file_name)

        base_key = f"{destination_prefix}/{base_name}"

        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=destination_prefix)
        files_with_base_key = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].startswith(base_key)]

        counter = 0

        unique_key = f"{destination_prefix}/{file_name}"
        while unique_key in files_with_base_key:
            counter += 1
            unique_key = f"{destination_prefix}/{base_name}_{counter}{extension}"

        return unique_key

    @staticmethod
    def get_last_day_of_month(year: int, month: int) -> datetime.date:
        last_day = calendar.monthrange(year, month)[1]
        return datetime.date(year, month, last_day)

    @staticmethod
    def get_next_month(year: int, month: int) -> Tuple[int, int]:
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        return next_year, next_month

    @staticmethod
    def get_collect_rule_filter_date(year: int, month: int, before: str, after: str):
        print("get_collect_rule_filter_date year: %s, month:  %s, before:  %s, after:  %s", year, month, before, after)
        if before.lower() == 'l':
            before_date = Utils.get_last_day_of_month(year, month)
        else:
            before_date = datetime.date(year, month, int(before))

        if before.lower() == 'l' and after.lower() == 'l':
            after_date = before_date
        elif (before.lower() == 'l' and after.lower() != 'l') or (
                before.lower() != 'l' and after.lower() != 'l' and int(before) > int(after)):
            next_year, next_month = Utils.get_next_month(year, month)
            after_date = datetime.date(next_year, next_month, int(after))
        elif after.lower() == 'l':
            after_date = Utils.get_last_day_of_month(year, month)
        else:
            after_date = datetime.date(year, month, int(after))

            print("get_collect_rule_filter_date before_date: %s, after_date:  %s", before_date, after_date)

        return before_date, after_date

    def get_media_type_by_file_extension(file_extension):
        if file_extension == "html":
            media_type = "text/html"
        elif file_extension == "png":
            media_type = "image/png"
        elif file_extension == "jpeg":
            media_type = "image/jpeg"
        elif file_extension == "pdf":
            media_type = "application/pdf"
        else:
            raise ValueError("the extension is not yet taken into account.")
        return media_type
    
    @staticmethod
    def kms_encrypt(data: str, KEY_ID) -> str:
        kms_client = boto3.client('kms')
        kms_response = kms_client.encrypt(
            KeyId=KEY_ID,
            Plaintext=data.encode('utf-8')
        )
        return base64.b64encode(kms_response['CiphertextBlob']).decode('utf-8')

    @staticmethod
    def kms_decrypt(data: str) -> str:
        ciphertext_blob = base64.b64decode(data)
        kms_client = boto3.client('kms')
        response = kms_client.decrypt(
            CiphertextBlob=ciphertext_blob
        )
        return response['Plaintext'].decode('utf-8')
    
    @staticmethod
    def upload_file_with_incremental_key(bucket_name, prefix_key, file_name, file_content, s3_endpoint_url=None):
        if s3_endpoint_url:
            s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)
        else:
            s3 = boto3.client('s3')

        unique_key = Utils.get_unique_key(s3, bucket_name, prefix_key, file_name)
        
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=unique_key)
        
        new_file_name = os.path.basename(unique_key)
        
        print(f'File uploaded to {bucket_name}/{unique_key}')
        return unique_key, new_file_name
    

    @staticmethod
    def move_file_with_incremental_key(bucket_name, source_key, destination_prefix, s3_endpoint_url=None):
        if s3_endpoint_url:
            s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)
        else:
            s3 = boto3.client('s3')

        file_name = os.path.basename(source_key)

        unique_key = Utils.get_unique_key(s3, bucket_name, destination_prefix, file_name)

        copy_source = {'Bucket': bucket_name, 'Key': source_key}
        s3.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=unique_key)

        # s3.delete_object(Bucket=bucket_name, Key=source_key)

        new_file_name = os.path.basename(unique_key)

        print(f'File moved to {bucket_name}/{unique_key}')
        return unique_key, new_file_name


    def delete_file_from_s3(bucket_name, unique_key, s3_endpoint_url=None):
        # Initialize S3 client
        if s3_endpoint_url:
            s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)
        else:
            s3 = boto3.client('s3')
        
        # Delete the object from S3
        s3.delete_object(Bucket=bucket_name, Key=unique_key)
        
        print(f'File deleted from {bucket_name}/{unique_key}')


    def rename_file_in_s3(bucket_name, prefix_key, file_name, new_file_name, s3_endpoint_url=None):
        if s3_endpoint_url:
            s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)
        else:
            s3 = boto3.client('s3')
    
        # Check whether a file with the proposed new name already exists among the existing files
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix_key)
        existing_files = [obj['Key'] for obj in response.get('Contents', [])]
        
        if f"{prefix_key}/{new_file_name}" in existing_files:
            raise GenericException(EnumStatusCode.INVOICE_ALREADY_EXISTS, f"An Invoice with the name '{new_file_name}' already exists.")
        
        # Rename file
        old_key = f"{prefix_key}/{file_name}"
        new_key = f"{prefix_key}/{new_file_name}"
        
        s3.copy_object(CopySource={'Bucket': bucket_name, 'Key': old_key}, Bucket=bucket_name, Key=new_key)
        s3.delete_object(Bucket=bucket_name, Key=old_key)
        
        print(f"The file has been renamed from '{file_name}' to '{new_file_name}' in bucket '{bucket_name}'.")

        return new_key, new_file_name

    def send_message_on_sqs(message: Any, region_name: str, queue_url: str, sqs_endpoint_url: str = None):
        if sqs_endpoint_url:
            sqs = boto3.client('sqs', region_name=region_name, endpoint_url=sqs_endpoint_url)
        else:
            sqs = boto3.client('sqs', region_name=region_name)

        # Send a message to the queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message
        )

        # return response
        return response
    
    @staticmethod
    def kms_encrypt(data: str, KEY_ID) -> str:
        kms_client = boto3.client('kms')
        kms_response = kms_client.encrypt(
            KeyId=KEY_ID,
            Plaintext=data.encode('utf-8')
        )
        return base64.b64encode(kms_response['CiphertextBlob']).decode('utf-8')

    @staticmethod
    def kms_decrypt(data: str) -> str:
        ciphertext_blob = base64.b64decode(data)
        kms_client = boto3.client('kms')
        response = kms_client.decrypt(
            CiphertextBlob=ciphertext_blob
        )
        return response['Plaintext'].decode('utf-8')
    
    @staticmethod
    def get_last_day_of_month(year: int, month: int) -> datetime.date:
        last_day = calendar.monthrange(year, month)[1]
        return datetime.date(year, month, last_day)

    @staticmethod
    def get_next_month(year: int, month: int) -> Tuple[int, int]:
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        return next_year, next_month
    
    @staticmethod
    def get_collect_rule_filter_date(year: int, month: int, before: str, after: str):
        print("get_collect_rule_filter_date year: %s, month:  %s, before:  %s, after:  %s", year, month, before, after)
        if before.lower() == 'l':
            before_date = Utils.get_last_day_of_month(year, month)
        else:
            before_date = datetime.date(year, month, int(before))

        if before.lower() == 'l' and after.lower() == 'l':
            after_date = before_date
        elif (before.lower() == 'l' and after.lower() != 'l') or (before.lower() != 'l' and after.lower() != 'l' and int(before) > int(after)):
            next_year, next_month = Utils.get_next_month(year, month)
            after_date = datetime.date(next_year, next_month, int(after))
        elif after.lower() == 'l':
            after_date = Utils.get_last_day_of_month(year, month)
        else:
            after_date = datetime.date(year, month, int(after))

            print("get_collect_rule_filter_date before_date: %s, after_date:  %s", before_date, after_date)

        return before_date, after_date
    
    def convert_mail_message_to_map(obj: MailMessage):
        return {
                    'date': obj.date.isoformat() if obj.date else None,
                    'subject': obj.subject,
                    'from': obj.from_,
                    'to': obj.to,
                    'cc': obj.cc,
                    'bcc': obj.bcc,
                    # 'body': obj.text or obj.html,
                    # 'headers': obj.headers,
                    'attachments': [{
                        'filename': attachment.filename,
                        'content_type': attachment.content_type,
                        'size': attachment.size,
                        # 'data': attachment.payload
                    } for attachment in obj.attachments]
                }
    
    def convert_email_message_to_map(obj: EmailMessage):
        return {
            'date': obj['Date'],
            'subject': obj['Subject'],
            'from': obj['From'],
            'to': obj.get_all('To', []),
            'cc': obj.get_all('Cc', []),
            'bcc': obj.get_all('Bcc', []),
            # 'body': obj.get_body(preferencelist=('plain', 'html')).get_content() if obj.get_body(preferencelist=('plain', 'html')) else None,
            'body': None,
            'headers': dict(obj.items()),
            'attachments': [{
                'filename': part.get_filename(),
                'content_type': part.get_content_type(),
                'size': len(part.get_payload(decode=True)) if part.get_payload(decode=True) else 0,
                # 'data': part.get_payload(decode=True)
            } for part in obj.iter_attachments()]
        }
        
    def get_file_in_s3(bucket_name, prefix_key, s3_endpoint_url=None):
        if s3_endpoint_url:
            s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)
        else:
            s3 = boto3.client('s3')
        try:
            response = s3.get_object(Bucket=bucket_name, Key=prefix_key)
            print("response:: ", response)
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print("error_code:: ", error_code)
            if error_code == 'NoSuchKey':
                raise GenericException(EnumStatusCode.FILE_DOES_NOT_EXISTS, f"File with Key '{prefix_key}' doesn't exists.")
            else:
                raise Exception(f"An error occurred while retrieving the file from S3: {error_code}")
        return response
    
    def fetch_s3_files(bucket_name, file_paths,drive_paths, s3_endpoint_url=None):
        if s3_endpoint_url:
            s3 = boto3.client('s3', endpoint_url=s3_endpoint_url)
        else: 
            s3 = boto3.client('s3')
        downloaded_files = []

        try:
            for i,file_path in enumerate(file_paths):
                # print("access_token drive connection",bucket_name)
                # print("Fetching file from S3:", bucket_name, file_path)
                try:
                    file_obj = s3.get_object(Bucket=bucket_name, Key=file_path)
                    file_content = file_obj['Body'].read()  # Read binary data
                    downloaded_files.append((drive_paths[i], file_content))  # Store filename and content as a tuple
                except ClientError as e:
                    error_code = e.response['Error']['Code']
                    print(f"Error fetching file '{file_path}',drive '{drive_paths[i]}' from S3: {error_code}")
                    if error_code == 'NoSuchKey':
                        raise GenericException(EnumStatusCode.FILE_DOES_NOT_EXISTS, f"File with Key '{file_path}' doesn't exist.")
                    else:
                        raise Exception(f"An error occurred while retrieving the file '{file_path}' from S3: {error_code}")
        
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        
        return downloaded_files

    def get_media_type_by_file_extension(file_extension):
        if file_extension == "html":
            media_type = "text/html"
        elif file_extension == "png":
            media_type = "image/png"
        elif file_extension == "jpeg":
            media_type = "image/jpeg"
        elif file_extension == "pdf":
            media_type = "application/pdf"
        else:raise ValueError("the extension is not yet taken into account.")
        return media_type
    
    def percent_by_amount(invoiceAmount: float, transactionValue: float) -> Optional[Tuple[float, float]]:
        if transactionValue == 0 or invoiceAmount == 0:
            return  0.0, 0.0
        percent_invoice_to_transaction = round((invoiceAmount / transactionValue) * 100, 2)
        percent_transaction_to_invoice = round((transactionValue / invoiceAmount) * 100, 2)
        return percent_invoice_to_transaction, percent_transaction_to_invoice
    
    def export_to_csv(transactions, company_name: str):
        """
        Export the transactions to a CSV file.
        """
        output = io.StringIO()
        output.write("Wording,Amount,Date,Original Value,Original Currency,Category,Provider,Method\n")
        
        # Write the transactions
        for transaction in transactions:
            output.write(
                f"{str(transaction.wording)},{str(transaction.value)},{str(transaction.date)},{str(transaction.original_value)},{str(transaction.original_currency)},{str(transaction.category)},{str(transaction.provider)},{str(transaction.method)}\n"
            )

        csv_data = output.getvalue()
        output.close()
        
        # Generate the filename
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{company_name}_transactions_{current_datetime}.csv"
        
        print("CSV file created successfully.")
        return {
            "data": csv_data.encode('utf-8'),
            "media_type": "text/csv",
            "file_name": file_name
        }
    
    def export_to_xml(transactions, company_name: str):
        """
        Export the transactions to an XML file.
        """
        # Create an in-memory bytes buffer
        buffer = io.BytesIO()
        
        # Write the XML content to the buffer
        buffer.write(b"<?xml version='1.0' encoding='UTF-8'?>\n")
        buffer.write(b"<transactions>\n")

        # Write the transactions
        for transaction in transactions:
            buffer.write(
                f"<transaction>\n"
                f"  <wording>{str(transaction.wording)}</wording>\n"
                f"  <amount>{str(transaction.value)}</amount>\n"
                f"  <date>{str(transaction.date)}</date>\n"
                f"  <original_value>{str(transaction.original_value)}</original_value>\n"
                f"  <original_currency>{str(transaction.original_currency)}</original_currency>\n"
                f"  <category>{str(transaction.category)}</category>\n"
                f"  <provider>{str(transaction.provider)}</provider>\n"
                f"  <method>{str(transaction.method)}</method>\n"
                f"</transaction>\n".encode('utf-8')
            )

        buffer.write(b"</transactions>\n")
        
        # Get the byte content
        xml_bytes = buffer.getvalue()
        buffer.close()
        
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{company_name}_transactions_{current_datetime}.xml"
        
        print("XML byte stream created successfully.")
        return {
            "data": xml_bytes,
            "media_type": "application/xml",
            "file_name": file_name
        }
    
    def export_to_json(transactions, company_name: str):
        """
        Export the transactions to a JSON file.
        """
        # Serialize the transactions to JSON
        transactions_json = json.dumps([{
            "wording": transaction.wording,
            "amount": transaction.value,
            "date": transaction.date,
            "original_value": transaction.original_value,
            "original_currency": transaction.original_currency,
            "category": transaction.category,
            "provider": transaction.provider,
            "method": transaction.method
        } for transaction in transactions], indent=2)
        
        # Convert the JSON string to bytes
        transactions_bytes = transactions_json.encode('utf-8')
        
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{company_name}_transactions_{current_datetime}.json"
        
        print("JSON byte stream created successfully.")
        return {
            "data": transactions_bytes,
            "media_type": "application/json",
            "file_name": file_name
        }
               
    def export_to_sepa(transactions, company_name: str):
        """
        Export the transactions to a SEPA file.
        """
        root = ET.Element("Document", xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.001.03")
        cstmr_cdt_trf_initn = ET.SubElement(root, "CstmrCdtTrfInitn")
        
        grp_hdr = ET.SubElement(cstmr_cdt_trf_initn, "GrpHdr")
        ET.SubElement(grp_hdr, "MsgId").text = f"FICHIER-{datetime.now().strftime('%Y%m%d')}-001"
        ET.SubElement(grp_hdr, "CreDtTm").text = datetime.now().isoformat()
        ET.SubElement(grp_hdr, "NbOfTxs").text = str(len(transactions))
        ET.SubElement(grp_hdr, "CtrlSum").text = f"{sum(tx.value for tx in transactions):.2f}"
        initg_pty = ET.SubElement(grp_hdr, "InitgPty")
        ET.SubElement(initg_pty, "Nm").text = "Entreprise ABC"
        
        pmt_inf = ET.SubElement(cstmr_cdt_trf_initn, "PmtInf")
        ET.SubElement(pmt_inf, "PmtInfId").text = f"PAYMENT-{datetime.now().strftime('%Y%m%d')}-001"
        ET.SubElement(pmt_inf, "PmtMtd").text = "TRF"
        ET.SubElement(pmt_inf, "BtchBookg").text = "false"
        ET.SubElement(pmt_inf, "ReqdExctnDt").text = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        
        # dbtr = ET.SubElement(pmt_inf, "Dbtr")
        # ET.SubElement(dbtr, "Nm").text = "Entreprise ABC"
        # dbtr_acct = ET.SubElement(pmt_inf, "DbtrAcct")
        # dbtr_acct_id = ET.SubElement(dbtr_acct, "Id")
        # ET.SubElement(dbtr_acct_id, "IBAN").text = "FR7630004000031234567890143"
        
        # dbtr_agt = ET.SubElement(pmt_inf, "DbtrAgt")
        # fin_instn_id = ET.SubElement(dbtr_agt, "FinInstnId")
        # ET.SubElement(fin_instn_id, "BIC").text = "BNPAFRPPXXX"
        
        for tx in transactions:
            cdt_trf_tx_inf = ET.SubElement(pmt_inf, "CdtTrfTxInf")
            pmt_id = ET.SubElement(cdt_trf_tx_inf, "PmtId")
            ET.SubElement(pmt_id, "EndToEndId").text = f"{tx.value:.2f}" #TODO: generate a unique ID
            amt = ET.SubElement(cdt_trf_tx_inf, "Amt")
            ET.SubElement(amt, "InstdAmt", Ccy=f"{tx.original_currency}").text = f"{tx.value:.2f}"
            
            cdtr_agt = ET.SubElement(cdt_trf_tx_inf, "CdtrAgt")
            fin_instn_id = ET.SubElement(cdtr_agt, "FinInstnId")
            ET.SubElement(fin_instn_id, "BIC").text = "BNPAFRPPXXX"
            
            cdtr = ET.SubElement(cdt_trf_tx_inf, "Cdtr")
            ET.SubElement(cdtr, "Nm").text = tx.wording
            cdtr_acct = ET.SubElement(cdt_trf_tx_inf, "CdtrAcct")
            cdtr_acct_id = ET.SubElement(cdtr_acct, "Id")
            ET.SubElement(cdtr_acct_id, "IBAN").text = tx.bank_account.iban
            
            rmt_inf = ET.SubElement(cdt_trf_tx_inf, "RmtInf")
            ET.SubElement(rmt_inf, "Ustrd").text = f"{tx.value:.2f}" #TODO: generate remittance info
        
        # Create an in-memory byte buffer
        byte_stream = io.BytesIO()
        
        # Write XML content to the byte buffer
        tree = ET.ElementTree(root)
        tree.write(byte_stream, encoding="utf-8", xml_declaration=True)
        
        # Get the byte content
        xml_bytes = byte_stream.getvalue()
        byte_stream.close()
        
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{company_name}_sepa_transactions_{current_datetime}.xml"
        
        print("SEPA byte stream created successfully.")
        return {
            "data": xml_bytes,
            "media_type": "application/xml",
            "file_name": file_name
        }
    
    def generate_next_slug(slug: str):
        """
        Generate a new slug by appending an incrementing number to the existing slug.
        """
        pattern = r"^(.*?)(?:-(\d+))?$"
        match = re.match(pattern, slug)

        if match:
            base_slug = match.group(1)
            counter = int(match.group(2)) + 1 if match.group(2) else 1
            return f"{base_slug}_{counter}"

        return f"{slug}-1"
    
    def check_min_price(price: float, min_price: float) -> float:
        """
        Check if the price is greater than or equal to the minimum price.
        """
        min_price = min_price
        if price is None:
            return min_price
        return price if price >= min_price else min_price

