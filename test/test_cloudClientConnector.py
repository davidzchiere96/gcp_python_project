import sys
sys.path.append(r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\gcp_python_project\gcp_python_project\src")

import unittest
import logger
from unittest.mock import patch, MagicMock
from cloudClientConnector import CloudStorageClient,BigQueryClient

log = logger.logger()

class TestCloudStorageClient(unittest.TestCase):
    @patch('cloudClientConnector.storage.Client')
    def test_connect(self, storage_client_mock):
        # Crea un'istanza di CloudStorageClient e chiamo metodo connect
        cloud_storage_client = CloudStorageClient()
        cloud_storage_client.connect()

        # Verifica che il client di storage mockato sia stato creato
        storage_client_mock.assert_called_once()

    def test_get_client(self):
        storage_client_mock = MagicMock()

        cloud_storage_client = CloudStorageClient()
        cloud_storage_client.connect = MagicMock(return_value=None)

        cloud_storage_client.client = storage_client_mock
        storage_client_instance = cloud_storage_client.get_client()

        self.assertEqual(storage_client_instance, storage_client_mock)


class TestBigQueryClient(unittest.TestCase):
    @patch('cloudClientConnector.bigquery.Client')
    def test_connect(self, bq_client_mock):
        # Crea un'istanza di CloudStorageClient e chiamo metodo connect
        bq_client = CloudStorageClient()
        bq_client.connect()

        # Verifica che il client di storage mockato sia stato creato
        bq_client_mock.assert_called_once()

    def test_get_client(self):
        bq_client_mock = MagicMock()

        bq_client = BigQueryClient()
        bq_client.connect = MagicMock(return_value=None)

        bq_client.client = bq_client_mock
        bq_client_instance = bq_client.get_client()

        self.assertEqual(bq_client_instance, bq_client_mock)


if __name__ == '__main__':
    unittest.main()