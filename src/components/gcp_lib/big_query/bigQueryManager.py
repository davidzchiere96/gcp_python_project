from components.logger import Log
from components.cloudClientConnector import CloudStorageClient
from components.gcp_lib.cloud_storage.storageGetter import BucketGetter
from bigQueryGetter import TableGetter
import components.inputRequests


log_instance = Log()
log = log_instance.logger()

class Table:
    def __init__(self, table_id):
        self.__storage_client = CloudStorageClient().get_client()
        self.__bucket_getter =TableGetter(table_id)
        self.table_id = table_id

    def create_bucket(self):
        new_bucket = self.__storage_client.create_bucket(self.table_id)
        log.info(f"New bucket '{self.table_id}' created!")

    def delete_bucket(self):
        bucket = self.__bucket_getter.get_bucket()
        bucket.delete(force=True)
        log.info(f"Bucket '{self.bucket_name}' deleted!")

    def update_bucket_storage_class(self, storage_class):
        bucket = self.__bucket_getter.get_bucket()

        bucket.update_storage_class(storage_class)  # es. "NEARLINE"
        log.info(f"Storage class of the bucket '{self.bucket_name}' updated to '{storage_class}'")

    # TODO: def lifecycle_management


def manage_bucket():
    operation_required = inputRequests.input_bucket_operation()

    if operation_required == 1:
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.create_bucket()

    elif operation_required == 2:
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.delete_bucket()

    elif operation_required == 3:
        storage_class = inputRequests.input_storage_class()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.update_bucket_storage_class(storage_class)

    else:
        log.warning("No operation found!")
        return


# buc = Bucket()
# buc.list_files("asset_storage_bucket")

# bucket_manager = Bucket()
# bucket_manager.create_bucket("asset_storage_bucket_april")
# bucket_manager.delete_bucket("asset_storage_bucket_april")
