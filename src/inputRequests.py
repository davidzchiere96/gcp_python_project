import logger

log = logger.logger()

def input_operation():
    operation_request = int(input(
                            "Hello! Please, select the operation you want to execute: \n"
                            " 1 - Verify BUCKET existence in CloudStorage\n "
                            "2 - Verify FILE existence in CloudStorage\n "
                            "3 - Verify TABLE existence in BigQuery\n "
                            "\n "
    ))
    return operation_request

def input_bucket_name():
    return str(input("Input the bucket_name to check: "))

def input_file_name():
    return str(input("Input the file_name to check: "))

def input_table_id():
    return str(input("Input the table_id to check: "))