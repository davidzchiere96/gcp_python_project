import unittest
import logger
from unittest.mock import MagicMock, patch
from bigQueryGetter import TableGetter
from storageGetter import BucketGetter, FileGetter
import main


log = logger.logger()

class TestMain(unittest.TestCase):
    @patch("inputRequests.input_operation", return_value=1)
    @patch("inputRequests.input_bucket_name", return_value="mock_bucket_name")
    @patch("storageGetter.BucketGetter")
    def main_bucket_existence(self, mock_bucket_getter, mock_input_bucket_name, mock_input_operation):
        # Creare un mock per la classe BucketGetter
        # Impostare il mock di get_bucket per restituire qualcosa (simulando l'esistenza del bucket)
        bucket_getter_mock = MagicMock()
        bucket_getter_mock.get_bucket.return_value = "mock_bucket_object"
        # Impostare il mock di BucketGetter per essere restituito quando viene creato un nuovo oggetto BucketGetter
        mock_bucket_getter.return_value = bucket_getter_mock

        main()

        # TEST 1: Verificare le chiamate ai metodi di input
        mock_input_operation.assert_called_once()
        mock_input_bucket_name.assert_called_once()
        # TEST 2: Verificare che il metodo get_bucket della classe BucketGetter sia stato chiamato una volta
        bucket_getter_mock.get_bucket.assert_called_once_with("mock_bucket_name")

    # @patch("inputRequests.input_operation", return_value=2)
    # @patch("inputRequests.input_bucket_name", return_value="mock_bucket_name")
    # @patch("inputRequests.input_file_name", return_value="mock_file_name")
    # @patch("storageGetter.FileGetter")
    # def main_file_existence(self, mock_file_getter, mock_input_bucket_name, mock_input_file_name, mock_input_operation):
    #
    #     file_getter_mock = MagicMock()
    #     file_getter_mock.get_file.return_value = "mock_file_object"
    #     # Impostare il mock di BucketGetter per essere restituito quando viene creato un nuovo oggetto BucketGetter
    #     mock_file_getter.return_value = file_getter_mock
    #
    #     main()
    #
    #     # TEST 1: Verificare le chiamate ai metodi di input
    #     mock_input_operation.assert_called_once()
    #     mock_input_bucket_name.assert_called_once()
    #     mock_input_file_name.assert_called_once()
    #
    #     # TEST 2: Verificare che il metodo get_bucket della classe BucketGetter sia stato chiamato una volta
    #     file_getter_mock.get_bucket.assert_called_once_with("mock_file_name")




if __name__ == '__main__':
    unittest.main()