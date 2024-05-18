from components.logger import Log
from google.cloud import storage, bigquery, pubsub_v1
# import os
from abc import ABC, abstractmethod


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"global_path/to/file"
log_instance = Log()
log = log_instance.logger()


class CloudClient(ABC):
    @abstractmethod
    def get_client(self):
        pass


class CloudStorageClient(CloudClient):
    def __init__(self):
        self.client = None

    def connect(self):
        try:
            self.client = storage.Client()
            log.info("GCS Client connected!")

        except Exception as e:
            log.error(f"Error connecting to storage client: {e}")

    def get_client(self):
        if not self.client:
            self.connect()
        return self.client


class BigQueryClient(CloudClient):
    def __init__(self):
        self.client = None

    def connect(self):
        try:
            self.client = bigquery.Client()
            log.info("BigQuery Client connected!")

        except Exception as e:
            log.error(f"Error connecting to BigQuery client: {e}")

    def get_client(self):
        if not self.client:
            self.connect()
        return self.client


class PubSubClient(CloudClient):
    def __init__(self):
        self.client = None

    def connect(self):
        try:
            self.client = pubsub_v1.PublisherClient()
            log.info("Pub/Sub Publisher Client connected!")

        except Exception as e:
            log.error(f"Error connecting to Pub/Sub Publisher client: {e}")

    def get_client(self):
        if not self.client:
            self.connect()
        return self.client


# CloudStorageClient().connect()
# BigQueryClient().get_client()








