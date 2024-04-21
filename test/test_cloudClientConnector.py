import unittest
import logger
from unittest.mock import patch, MagicMock
from cloudClientConnector import CloudStorageClient

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


if __name__ == '__main__':
    unittest.main()