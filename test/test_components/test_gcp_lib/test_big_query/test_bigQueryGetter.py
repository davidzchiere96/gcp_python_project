# import sys
# sys.path.append(r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\gcp_python_project\gcp_python_project\src")

import unittest
import components.logger
from unittest.mock import MagicMock, patch
from components.gcp_lib.big_query.bigQueryGetter import TableGetter


class TestTableGetter(unittest.TestCase):

    @patch('components.gcp_lib.big_query.bigQueryGetter.BigQueryClient.get_client')
    def test_get_client(self, mock_get_client):
        table_getter = TableGetter("test_table")
        table_getter._TableGetter__big_query_client
        mock_get_client.assert_called_once()

    @patch('components.gcp_lib.big_query.bigQueryGetter..BigQueryClient.get_client')
    @patch('logger.Log')
    def test_get_table_success(self, mock_log, mock_get_client):
        table_getter = TableGetter("test_table")
        table = table_getter.get_table()

        mock_get_client.return_value.get_table.assert_called_once()
        self.assertEqual(table, mock_get_client.return_value.get_table("test_table"))

    @patch('components.gcp_lib.big_query.bigQueryGetter..BigQueryClient.get_client')
    @patch('logger.Log.logger')
    def test_get_table_failure(self, mock_log, mock_get_client):
        mock_get_client.get_table.side_effect = Exception("Table not found")
        table_getter = TableGetter("test_table")
        table = table_getter.get_table()

        # mock_log.error.assert_called_once_with("Table 'test_table' not exists.")


if __name__ == '__main__':
    unittest.main()