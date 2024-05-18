# import sys
# sys.path.append(r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\gcp_python_project\gcp_python_project\src")

import unittest
import logger
from unittest.mock import patch, MagicMock
from cloudClientConnector import CloudStorageClient,BigQueryClient

# log = logger.logger()

class TestCloudStorageClient(unittest.TestCase):

    # patch per mockare le due chiamate
    @patch('cloudClientConnector.storage.Client')
    @patch('cloudClientConnector.Log')
    def test_connect_success(self, mock_log, mock_storage_client):

        # istanziamo un oggetto della classe CloudStorageClient su cui poi fare il test
        cloud_storage_client = CloudStorageClient()

        # chiamiamo il metodo che vogliamo testare
        cloud_storage_client.connect()

        # Assert
        mock_storage_client.assert_called_once()  # Verifica se storage.Client() è stato chiamato esattamente una volta
        # mock_log.info.assert_called_once_with("GCS Client connected!")

    @patch('cloudClientConnector.storage.Client')
    @patch('cloudClientConnector.Log')
    def test_connect_failure(self, mock_log, mock_storage_client):

        # instantiate
        cloud_storage_client = CloudStorageClient()
        mock_storage_client.side_effect = Exception("Connection error")

        # act
        cloud_storage_client.connect()

        # assert
        # mock_log.logger.error.assert_called_once_with("Error connecting to storage client: Connection error")

    @patch('cloudClientConnector.CloudStorageClient.connect')
    def test_get_client_if_not_connected(self, mock_storage_client_connect):

        cloud_storage_client = CloudStorageClient()
        cloud_storage_client.get_client()
        mock_storage_client_connect.assert_called_once()

    @patch('cloudClientConnector.storage.Client')
    def test_get_client_if_connected(self, mock_storage_client):

        cloud_storage_client = CloudStorageClient()
        cloud_storage_client.client = MagicMock()

        client = cloud_storage_client.get_client()

        self.assertEqual(client, cloud_storage_client.client)


class TestBigQueryClient(unittest.TestCase):

    @patch('cloudClientConnector.bigquery.Client')
    @patch('cloudClientConnector.Log')
    def test_connect_success(self, mock_log, mock_bigquery_client):


        bigquery_client = BigQueryClient()

        bigquery_client.connect()

        mock_bigquery_client.assert_called_once()
        # mock_log.info.assert_called_once_with("BigQuery Client connected!")

    @patch('cloudClientConnector.bigquery.Client')
    @patch('cloudClientConnector.Log')
    def test_connect_failure(self, mock_log, mock_bigquery_client):

        # instantiate
        bigquery_client = BigQueryClient()
        mock_bigquery_client.side_effect = Exception("Connection error")

        # act
        bigquery_client.connect()

        # assert
        # mock_log.error.assert_called_once_with("Error connecting to BigQuery client: Connection error")

    @patch('cloudClientConnector.BigQueryClient.connect')
    def test_get_client_if_not_connected(self, mock_bigquery_client_connect):

        bigquery_client = BigQueryClient()
        bigquery_client.get_client()
        mock_bigquery_client_connect.assert_called_once()

    @patch('cloudClientConnector.bigquery.Client')
    def test_get_client_if_connected(self, mock_bigquery_client):

        bigquery_client = BigQueryClient()
        bigquery_client.client = mock_bigquery_client

        client = bigquery_client.get_client()

        self.assertEqual(client, bigquery_client.client)


if __name__ == '__main__':
    unittest.main()