import unittest
import logger
from unittest.mock import MagicMock
from bigQueryGetter import TableGetter

log = logger.logger()

class TestTableGetter(unittest.TestCase):
    def test_get_table(self):
        # Mocking the BQClient object AND the get_bucket method
        bq_client_mock = MagicMock()
        bq_client_mock.get_table = MagicMock(return_value="mock_table")

        # Creating an instance of BucketGetter with the mocked CloudStorageClient
        table_getter = TableGetter("mock_table_name")
        table_getter._TableGetter__big_query_client = bq_client_mock
        table = table_getter.get_table()

        # TEST 1
        # Verifying that the get_table method is called
        bq_client_mock.get_table.assert_called_once_with("mock_table_name")

        # TEST 2
        # Verifying that the returned bucket is correct
        self.assertEqual(table, "mock_table")


if __name__ == '__main__':
    unittest.main()