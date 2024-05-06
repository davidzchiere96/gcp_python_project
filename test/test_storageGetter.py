import unittest
from unittest.mock import MagicMock, patch
from storageGetter import BucketGetter,FileGetter
from cloudClientConnector import CloudStorageClient


class TestBucketGetter(unittest.TestCase):

    @patch('storageGetter.CloudStorageClient.get_client')
    def test_get_client(self, mock_get_client):
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

    @patch('storageGetter.BucketGetter.get_bucket')
    @patch('logger.Log')
    def test_get_file_success(self, mock_log, mock_get_bucket):
        mock_bucket = mock_get_bucket.return_value
        mock_blob = mock_bucket.blob.return_value

        file_getter = FileGetter("test_bucket", "test_file")
        file = file_getter.get_file()

        mock_get_bucket.assert_called_once_with()
        mock_bucket.blob.assert_called_once_with("test_file")
        self.assertEqual(file, mock_blob)
        # mock_log.info.assert_called_once_with("File 'test_file' from buket 'test_bucket' returned!")

    @patch('storageGetter.CloudStorageClient.get_client')
    @patch('logger.Log.logger')
    def test_get_file_failure(self, mock_log, mock_get_bucket):
        mock_get_bucket.blob.side_effect = Exception("File not found")
        file_getter = FileGetter("test_bucket","test_file")
        file = file_getter.get_file()

        # mock_log.error.assert_called_once_with("File 'test_file' not exists.")


if __name__ == '__main__':
    unittest.main()