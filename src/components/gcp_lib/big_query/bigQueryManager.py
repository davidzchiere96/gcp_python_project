from components.logger import Log
from components.cloudClientConnector import CloudStorageClient, BigQueryClient
from components.gcp_lib.cloud_storage.storageGetter import BucketGetter, FileGetter
from components.gcp_lib.cloud_storage.storageFileManager import File
from components.gcp_lib.big_query.bigQueryGetter import TableGetter
import components.inputRequests
import json
import csv


log_instance = Log()
log = log_instance.logger()


class Table:
    def __init__(self, table_id):
        self.__bigquery_client = BigQueryClient().get_client()
        self.__storage_client = CloudStorageClient().get_client()
        self.__table_getter = TableGetter(table_id)
        self.table_id = table_id

    def process_from_storage(self, bucket_name, file_name):

        file_downloaded = File(bucket_name, file_name).download_file("STRING")
        log.info(f"file_downloaded as a string: {(file_downloaded)}")
        rows = json.loads(file_downloaded)
        log.info(f"Rows extracted from file!")
        table = TableGetter(self.table_id).get_table()
        job = self.__bigquery_client.insert_rows_json(table, rows)

        log.info(f"Insert job in table '{self.table_id}'completed!")



# table = Table("training-gcp-309207.dataset_chieregatoD.film")
# table.process_from_storage("bucket_chieregatod_gcs_asset","film.json")


class SQL:
    def __init__(self, query):
        self.__bigquery_client = BigQueryClient().get_client()
        self.query = query

    def run_query(self):

        query_job = self.__bigquery_client.query(self.query)
        results = query_job.result()
        # Converte i risultati in una lista di dizionari
        rows = [dict(row) for row in results]
        log.info(f"Query results: '{rows}'")

        return rows

# query = "SELECT count(*) as count_rows FROM `training-gcp-309207.dataset_chieregatoD.film`"
# sql = SQL(query).run_query()

# Esempio di utilizzo della funzione
# query = "SELECT count(*) FROM `training-gcp-309207.dataset_chieregatoD.film`"
# project_id = "your_project_id"
# dataset_id = "your_dataset_id"

# results = run_query(query, project_id, dataset_id)
# for row in results:
#    print(row)


