from typing import Any, Tuple
import pytz, boto3, datetime, os, base64, calendar

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
        return UserDtoMetadata(id=str(current_user.id), email=current_user.email, firstname=current_user.firstname, lastname=current_user.lastname, enabled=current_user.enabled, disabledByAdmin=current_user.disabledByAdmin, userId=current_user.userId)

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
    def upload_file_with_incremental_key(bucket_name, prefix_key, file_name, file_content):
        s3 = boto3.client('s3')

        unique_key = Utils.get_unique_key(s3, bucket_name, prefix_key, file_name)
        
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=unique_key)
        
        new_file_name = os.path.basename(unique_key)
        
        print(f'File uploaded to {bucket_name}/{unique_key}')
        return unique_key, new_file_name
    

    @staticmethod
    def move_file_with_incremental_key(bucket_name, source_key, destination_prefix):
        s3 = boto3.client('s3')

        file_name = os.path.basename(source_key)

        unique_key = Utils.get_unique_key(s3, bucket_name, destination_prefix, file_name)

        copy_source = {'Bucket': bucket_name, 'Key': source_key}
        s3.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=unique_key)

        # s3.delete_object(Bucket=bucket_name, Key=source_key)

        new_file_name = os.path.basename(unique_key)

        print(f'File moved to {bucket_name}/{unique_key}')
        return unique_key, new_file_name


    def delete_file_from_s3(bucket_name, unique_key):
        # Initialize S3 client
        s3 = boto3.client('s3')
        
        # Delete the object from S3
        s3.delete_object(Bucket=bucket_name, Key=unique_key)
        
        print(f'File deleted from {bucket_name}/{unique_key}')


    def rename_file_in_s3(bucket_name, prefix_key, file_name, new_file_name):
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

    def send_message_on_sqs(message: Any, region_name: str, queue_url: str):
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
        
    def get_file_in_s3(bucket_name, prefix_key):
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
    
    def fetch_s3_files(bucket_name, file_paths,drive_paths):
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