import os
import logger
from cloudClientConnector import BigQueryClient


log = logger.logger()


class TableGetter:
    def __init__(self, table_id):
        self.__big_query_client = BigQueryClient().get_client()
        self.table_id = table_id

    def get_table(self):
        try:
            table = self.__big_query_client.get_table(self.table_id)
            log.info(f"Table '{self.table_id}' returned!")
            return table
        except Exception as e:
            log.error(f"Table '{self.table_id}' not exists.")