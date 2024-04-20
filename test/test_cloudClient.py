import unittest
from unittest.mock import MagicMock
from cloudClient import CloudStorageClient

class TestCloudStorageClient(unittest.TestCase):
    def setUp(self):
        self.storage_client = CloudStorageClient()

    def test_get_client_connects_when_not_connected(self):
        # Mock del metodo connect per verificare che venga chiamato
        self.storage_client.connect = MagicMock()

        # Chiamata al metodo get_client prima della connessione
        client = self.storage_client.get_client()

        # Verifica che il metodo connect sia stato chiamato
        self.storage_client.connect.assert_called_once()

    def test_get_client_returns_client_when_already_connected(self):
        # Mock del client già connesso
        client_mock = MagicMock()
        self.storage_client.client = client_mock

        # Chiamata al metodo get_client quando il client è già connesso
        client = self.storage_client.get_client()

        # Verifica che il client restituito sia quello già connesso
        self.assertEqual(client, client_mock)

    def test_connect_logs_error_when_exception_occurs(self):
        # Mock del logger per verificare che venga chiamato con il messaggio di errore appropriato
        logger_mock = MagicMock()
        self.storage_client.log = logger_mock

        # Mock del metodo storage.Client per sollevare un'eccezione
        storage_client_mock = MagicMock()
        storage_client_mock.side_effect = Exception("Connection error")
        self.storage_client.storage.Client = storage_client_mock

        # Chiamata al metodo connect che dovrebbe sollevare un'eccezione
        self.storage_client.connect()

        # Verifica che il logger sia stato chiamato con il messaggio di errore appropriato
        logger_mock.error.assert_called_once_with("Error connecting to storage client: Connection error")

if __name__ == "__main__":
    unittest.main()
