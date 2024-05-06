import os
from logger import Log
from cloudClientConnector import CloudStorageClient

log_instance = Log()
log = log_instance.logger()


class BucketGetter:
    def __init__(self, bucket_name):
        self.__storage_client = CloudStorageClient().get_client()
        self.bucket_name = bucket_name

    def get_bucket(self):
        try:
            bucket = self.__storage_client.get_bucket(self.bucket_name)
            log.info(f"Bucket '{self.bucket_name}' returned!")
            return bucket
        except Exception as e:
            log.error(f"Bucket '{self.bucket_name}' not exists.")


class FileGetter:
    def __init__(self, bucket_name, file_name=None):
        self.__bucket = BucketGetter(bucket_name)
        self.file_name = file_name
        self.bucket_name = bucket_name

    def get_file(self):
        try:
            bucket = self.__bucket.get_bucket()
            blob = bucket.blob(self.file_name)
            log.info(f"File '{self.file_name}' from buket '{self.bucket_name}' returned!")
            return blob
        except Exception as e:
            log.error(f"File '{self.file_name}' not exists.")

    # tirare fuori oppure chiamare la size dirattemente nel managestoragefile
    def get_file_size(self):
        """Get the size of a GCS file."""
        bucket = self.__bucket.get_bucket()
        blob = bucket.blob(self.file_name)

        if blob.size is not None:
            size_in_bytes = float(blob.size)
            size_in_kb = size_in_bytes / 1024
            size_in_mb = size_in_kb / 1024
            size_in_gb = size_in_mb / 1024
            log.info(f"File '{self.file_name}' size is: '{size_in_gb}'GB")
            return size_in_gb
        else:
            log.error(f"Failed to retrieve file size for '{self.file_name}'. Blob size is None.")
            return None
