import unittest
import logger
from unittest.mock import MagicMock
from storageGetter import BucketGetter,FileGetter

log = logger.logger()

class TestBucketGetter(unittest.TestCase):
    def test_get_bucket(self):
        # Mocking the CloudStorageClient object AND the get_bucket method
        storage_client_mock = MagicMock()
        storage_client_mock.get_bucket = MagicMock(return_value="mock_bucket")

        # Creating an instance of BucketGetter with the mocked CloudStorageClient
        bucket_getter = BucketGetter("mock_bucket_name")
        bucket_getter._BucketGetter__storage_client = storage_client_mock
        # Calling the get_bucket method
        bucket = bucket_getter.get_bucket()

        # TEST 1
        # Verifying that the get_bucket method of the mocked CloudStorageClient is called
        storage_client_mock.get_bucket.assert_called_once_with("mock_bucket_name")

        # TEST 2
        # Verifying that the returned bucket is correct
        self.assertEqual(bucket, "mock_bucket")

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