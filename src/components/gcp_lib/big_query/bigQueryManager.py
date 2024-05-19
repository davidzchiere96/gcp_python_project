from components.logger import Log
from components.cloudClientConnector import CloudStorageClient, BigQueryClient
from components.gcp_lib.cloud_storage.storageGetter import BucketGetter
from bigQueryGetter import TableGetter
import components.inputRequests


log_instance = Log()
log = log_instance.logger()

class SQL:
    def __init__(self, table_id):
        self.__bq_client = BigQueryClient().get_client()

    # def execute_query_select(self):
    #     self.__bq_client...
    #     "SELECT COUNT(*) FROM training-gcp-309207.dataset_chieregatoD.film"


class Table:
    def __init__(self, table_id):
        self.__storage_client = CloudStorageClient().get_client()
        self.__bucket_getter =TableGetter(table_id)
        self.table_id = table_id

    # def create_bucket(self):
    #     new_bucket = self.__storage_client.create_bucket(self.table_id)
    #     log.info(f"New bucket '{self.table_id}' created!")
    #
    # def delete_bucket(self):
    #     bucket = self.__bucket_getter.get_bucket()
    #     bucket.delete(force=True)
    #     log.info(f"Bucket '{self.bucket_name}' deleted!")
    #
    # def update_bucket_storage_class(self, storage_class):
    #     bucket = self.__bucket_getter.get_bucket()
    #
    #     bucket.update_storage_class(storage_class)  # es. "NEARLINE"
    #     log.info(f"Storage class of the bucket '{self.bucket_name}' updated to '{storage_class}'")

    def process_from_storage(self):


