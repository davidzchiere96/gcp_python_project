from components.cloudClientConnector import BigQueryClient, PublisherClient
from components.gcp_lib.big_query.bigQueryGetter import TableGetter
from components.gcp_lib.big_query.bigQueryManager import Table, SQL
from components.gcp_lib.cloud_storage.storageGetter import FileGetter, BucketGetter
from components.gcp_lib.cloud_storage.storageFileManager import Bucket, File
from components.gcp_lib.pub_sub.pubsubManager import Topic, Subscription
from components.gcp_lib.pub_sub.publisher import Publisher

from components.localGetter import LocalFileGetter
from components.logger import Log
from components import inputRequests
import json
import time


log_instance = Log()
log = log_instance.logger()


def main():
    bucket_name = "bucket_chieregatod_gcs_asset"
    file_name = "film.json"
    local_file_path = r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\gcp_python_project\gcp_python_project\src\config\film.json"
    table_id = "training-gcp-309207.dataset_chieregatoD.film"
    topic_id = "chieregatod_topic"

    # 1
    File(bucket_name,file_name,local_file_path).upload_file()

    # 2
    # Esempio di processamento di un file da GCS e inserimento in BigQuery
    Table(table_id).process_from_storage(bucket_name, file_name)

    # 3
    query = "SELECT count(*) as count_rows FROM `training-gcp-309207.dataset_chieregatoD.film`"
    query_results = SQL(query).run_query()

    # 4
    # Esempio di pubblicazione di un messaggio in un topic Pub/Sub
    message = {"query_results": f"{query_results}"} # value = "select count(*) from table film"
    # publish_report_by_message("nome-del-tuo-topic", message)
    Publisher(message).publish_message()



if __name__ == "__main__":
    main()