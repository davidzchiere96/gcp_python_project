from components.cloudClientConnector import BigQueryClient, PublisherClient
from components.gcp_lib.big_query.bigQueryGetter import TableGetter
from components.gcp_lib.cloud_storage.storageGetter import FileGetter, BucketGetter
from components.gcp_lib.cloud_storage.storageFileManager import Bucket, File
from components.gcp_lib.pub_sub.pubsubManager import Topic, Message
from components.localGetter import LocalFileGetter
from components.logger import Log
from components import inputRequests
import json
import time


log_instance = Log()
log = log_instance.logger()


# Nome del bucket di Google Cloud Storage
bucket_name = "nome-del-tuo-bucket"
file_name = ""
local_file_path = ""

# Funzione per caricare un file in Google Cloud Storage

upload_to_storage = File(bucket_name,file_name,local_file_path).upload_file()

# Funzione per leggere un file da Google Cloud Storage e inserirlo in BigQuery
def process_file(file_path, dataset_id, table_id):

    blob = FileGetter(bucket_name,file_name).declare_file()
    data = json.loads(blob.download_as_string())

    # dataset_ref = bigquery_client.dataset(dataset_id)
    # table_ref = dataset_ref.table(table_id)
    # table = bigquery_client.get_table(table_ref)
    table = TableGetter(table_id).get_table()

    bq_client = BigQueryClient().get_client()
    errors = bq_client.insert_rows_json(table, data)

    if errors:
        print("Errors during BigQuery insert:", errors)
    else:
        print("Data inserted into BigQuery successfully!")

def get_query_count_result(): # query sulla tabella che fa una count sulla tabella e il risultato finira poi nel messaggio
    result = 4
    return result

# Funzione per pubblicare un messaggio in un topic Pub/Sub
def publish_report_by_message(topic_name, message):
    # publisher = PublisherClient.get_client()
    # topic_path = publisher.topic_path(project_id, topic_name)
    topic_path = Topic().topic_path
    future = Message(message).publish_message
    # future = publisher.publish(topic_path, json.dumps(message).encode())
    # print("Published message ID:", future.result())


def main():
    upload_to_storage("src/config/film.csv")

    # Esempio di processamento di un file da GCS e inserimento in BigQuery
    process_file("path/del/tuo/file.txt", "nome-del-tuo-dataset", "training-gcp-309207.dataset_chieregatoD.film")

    # Esempio di pubblicazione di un messaggio in un topic Pub/Sub
    message = {"rows_count": f"{get_query_count_result()}"} # value = "select count(*) from table film"
    publish_report_by_message("nome-del-tuo-topic", message)



if __name__ == "__main__":
    main()