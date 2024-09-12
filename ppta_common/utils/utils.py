import base64
import calendar
from typing import Any, Tuple
import pytz
import datetime, os

from tzlocal import get_localzone


class Utils:

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
