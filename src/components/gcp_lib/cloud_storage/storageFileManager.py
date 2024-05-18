from components.logger import Log
from storageBucketManager import Bucket
from storageGetter import BucketGetter, FileGetter
from components.localGetter import LocalFileGetter
import components.inputRequests


log_instance = Log()
log = log_instance.logger()

class File:
    def __init__(self, bucket_name, file_name, local_file_path=None):
        self.__file = FileGetter(bucket_name, file_name)
        self.__bucket = BucketGetter(bucket_name)
        self.__local_file = LocalFileGetter(local_file_path)
        self.file_name = file_name
        self.bucket_name = bucket_name
        self.local_file_path = local_file_path

    def upload_file(self):
        bucket = self.__bucket.get_bucket()
        blob = bucket.blob(self.file_name)
        file_size = self.__local_file.get_local_file_size()

        if file_size > 1.0:
            # MANCA PROCEDURA DI GRACEFUL SHUTDOWN
            """Upload a large file to GCS using streaming"""
            with open(self.local_file_path, "rb") as f:
                blob.upload_from_file(f)
            log.info(f"streaming...")
            log.info(f"File '{self.local_file_path}' uploaded to '{self.bucket_name}/{self.file_name}'")
            return

        else:
            file_to_upload = blob.upload_from_filename(self.local_file_path)
            log.info(f"File '{self.local_file_path}' uploaded to '{self.bucket_name}/{self.file_name}'")

        return

    def download_file(self):
        bucket = self.__bucket.get_bucket()
        blob = bucket.blob(self.file_name)
        file_size = self.__file.get_file_size()

        if file_size > 1:
            # MANCA PROCEDURA DI GRACEFUL SHUTDOWN
            """Download a large file from GCS using streaming"""
            with open(self.local_file_path, "wb") as f:
                blob.download_to_file(f)
            log.info(f"streaming...")
            log.info(f"File '{self.bucket_name}/{self.file_name}' downloaded to '{self.local_file_path}'")
            return

        else:
            file_to_download = blob.download_to_filename(self.local_file_path)
            log.info(f"File '{self.file_name}' downloaded from bucket '{self.bucket_name}' to '{self.local_file_path}'.")

        return

    def delete_file(self):
        bucket = self.__bucket.get_bucket()
        blob = bucket.blob(self.file_name)
        file_to_delete = blob.delete()
        log.info(f"File '{self.file_name}' deleted from bucket '{self.bucket_name}'.")
        return

    def write_to_file(self, message):
        try:
            """Write and read a blob from GCS using file-like IO"""
            bucket = self.__bucket.get_bucket()
            blob = bucket.blob(self.file_name)

            with blob.open("w") as f:
                f.write(message)
                log.info(f"Message written in file '{self.file_name}'")

        except FileNotFoundError:
            log.error("File not found.")

    def read_from_file(self):
        try:
            """Write and read a blob from GCS using file-like IO"""
            bucket = self.__bucket.get_bucket()
            blob = bucket.blob(self.file_name)

            with blob.open("r") as f:
                log.info(f"Read file '{self.file_name}'")
                print(f.read())

        except FileNotFoundError:
            log.error("File not found.")

    def update_file_storage_class(self, storage_class):
        bucket = self.__bucket.get_bucket()
        blob = bucket.blob(self.file_name)
        blob.update_storage_class(storage_class)  # es. "NEARLINE"
        log.info(f"Storage class of the object '{self.file_name}' updated to '{storage_class}'")
        return

    # TODO: def lifecycle
    # TODO: def versioning


def manage_file():
    operation_required = inputRequests.input_file_operation()

    if operation_required == 1:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file_path = inputRequests.input_source_file_path()
        file = File(bucket_name, file_name, file_path)
        file.upload_file()

    elif operation_required == 2:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file_path = inputRequests.input_source_file_path()
        file = File(bucket_name, file_name, file_path)
        file.download_file()

    elif operation_required == 3:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file = File(bucket_name, file_name)
        file.delete_file()

    elif operation_required == 4:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        message = inputRequests.input_message()
        file = File(bucket_name, file_name)
        file.write_to_file(message)

    elif operation_required == 5:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file = File(bucket_name, file_name)
        file.read_from_file()

    elif operation_required == 6:
        storage_class = inputRequests.input_storage_class()
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file = File(bucket_name, file_name)
        file.update_file_storage_class(storage_class)

    else:
        log.warning("No operation found!")
        return


# file = File()
# file.upload_file("asset_storage_bucket", "message_streaming.json", "config\message.json")
# file.download_file("asset_storage_bucket", "message_streaming.json", "config\message_streaming.json")

    # MUOVI UN FILE DA UN BUCKET AD UN ALTRO
    # CREA UNA DIRECTORY NEL BUCKET
    # ELIMINA UNA DIRECTORY NEL BUCKET

# file = File()
# file.download_file("asset_storage_bucket", "april_fool.json", "config\message_april_fool.json")
# file.delete_file("asset_storage_bucket", "april_fool.json")


# File().delete_file("asset_storage_bucket", "message_new_incapsulated.json")
# download_file("asset_storage_bucket", "message_newest.json", "config\message_newest.json")
# delete_file("asset_storage_bucket", "message_newest.json")

