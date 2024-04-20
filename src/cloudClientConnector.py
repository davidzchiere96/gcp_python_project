# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
# Client connector
# Per i log utilizzare nuove librerie assettizzate
import logger
from google.cloud import storage
import os
from abc import ABC, abstractmethod


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"config\training-gcp-309207-683a827c1e0e.json"
log = logger.logger()

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


CloudStorageClient().get_client()








