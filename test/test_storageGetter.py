import unittest
from unittest.mock import MagicMock, patch
from storageGetter import BucketGetter,FileGetter
from cloudClientConnector import CloudStorageClient


class TestBucketGetter(unittest.TestCase):

    @patch('storageGetter.CloudStorageClient.get_client')
    def test_get_client_success(self, mock_get_client):
        bucket_getter = BucketGetter("test_bucket")
        bucket_getter._BucketGetter__storage_client
        mock_get_client.assert_called_once()

    @patch('storageGetter.CloudStorageClient.get_client')
    @patch('logger.Log')
    def test_get_bucket_success(self, mock_log, mock_get_client):

        bucket_getter = BucketGetter("test_bucket")

        bucket = bucket_getter.get_bucket()

        mock_get_client.return_value.get_bucket.assert_called_once()
        self.assertEqual(bucket, mock_get_client.return_value.get_bucket("test_bucket"))

    @patch('storageGetter.CloudStorageClient.get_client')
    @patch('logger.Log.logger')
    def test_get_bucket_failure(self, mock_log, mock_get_client):

        mock_get_client.get_bucket.side_effect = Exception("Bucket not found")
        bucket_getter = BucketGetter("test_bucket")

        bucket = bucket_getter.get_bucket()

        # mock_log.error.assert_called_once_with("Bucket 'test_bucket' not exists.")




class TestFileGetter(unittest.TestCase):
    def test_get_file(self):
        # Mocking: Bucket, BucketGetter and get_bucket
        mock_bucket = MagicMock()
        mock_bucket_getter = MagicMock()
        mock_bucket_getter.get_bucket.return_value = mock_bucket


        file_getter = FileGetter(bucket_name="mock_bucket_name", file_name="mock_file_name")
        file_getter._FileGetter__bucket = mock_bucket_getter
        file_getter.get_file()

        # TEST 1
        mock_bucket_getter.get_bucket.assert_called_once()
        # TEST 2
        mock_bucket.blob.assert_called_once_with("mock_file_name")
        #NO ASSERT EQUAL TEST because no returned value


if __name__ == '__main__':
    unittest.main()