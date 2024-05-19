import os
from components.logger import Log
from components.cloudClientConnector import CloudStorageClient
import components.inputRequests
from datetime import datetime


log_instance = Log()
log = log_instance.logger()

class BucketGetter:
    def __init__(self, bucket_name=None):
        self.__storage_client = CloudStorageClient().get_client()
        self.bucket_name = bucket_name

    def declare_bucket(self):
        bucket = self.__storage_client.bucket(self.bucket_name)
        log.info(f"Bucket '{self.bucket_name}' declared!")
        return bucket

    def get_bucket(self):
        try:
            bucket = self.__storage_client.get_bucket(self.bucket_name)
            log.info(f"Bucket '{self.bucket_name}' returned!")
            return bucket
        except Exception as e:
            log.error(f"Bucket '{self.bucket_name}' not exists.")

    def list_buckets(self, prefix=None):
        """Lists all buckets in the project."""
        client = self.__storage_client
        buckets = client.list_buckets(prefix=prefix)
        log.info("Listing buckets...")

        metadata = []
        num_buckets = 0
        for bucket in buckets:
            created_time = datetime.strptime(bucket.time_created, "%Y-%m-%dT%H:%M:%S")
            metadata.append({
                'name': bucket.name,
                'created_time': created_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'storage_class': bucket.storage_class
            })
            num_buckets += 1

        log.info(f"There are {num_buckets} buckets in current project: {metadata}")
        return metadata

    def list_files(self, prefix=None):
        """Lists all the blobs in the bucket."""
        bucket = self.get_bucket()
        list_of_files = bucket.list_blobs(prefix=prefix, versions=False)
        log.info(f"Listing objects in bucket '{self.bucket_name}'")

        metadata = []
        num_files = 0
        for file in list_of_files:
            metadata.append({
                'name': file.name,
                'size_in_bytes': file.size,
                'created_time': file.time_created.strftime("%Y-%m-%dT%H:%M:%S"),
                'storage_class': file.storage_class
            })
            num_files += 1

        log.info(f"There are {num_files} objects in bucket '{self.bucket_name}': {metadata}")
        return metadata


class FileGetter:
    def __init__(self, bucket_name, file_name=None):
        self.__bucket = BucketGetter(bucket_name)
        self.file_name = file_name
        self.bucket_name = bucket_name

    def declare_file(self):
        bucket = self.__bucket.get_bucket()
        blob = bucket.blob(self.file_name)
        log.info(f"File '{self.file_name}' from buket '{self.bucket_name}' declared!")
        return blob

    def get_file(self):
        try:
            bucket = self.__bucket.get_bucket()
            blob = bucket.get_blob(self.file_name)
            log.info(f"File '{self.file_name}' from buket '{self.bucket_name}' returned!")
            return blob
        except Exception as e:
            log.error(f"File '{self.file_name}' not exists.")





    # tirare fuori oppure chiamare la size dirattemente nel managestoragefile come metadato
    def get_file_size(self):
        """Get the size of a GCS file."""
        # bucket = self.__bucket.get_bucket()
        # blob = bucket.blob(self.file_name)
        blob = self.get_file()

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

