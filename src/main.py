from bigQueryGetter import TableGetter
from storageGetter import FileGetter, BucketGetter
import logger
import inputRequests


log = logger.logger()


def main():

    operation_required = inputRequests.input_operation()

    # Verify Bucket existence
    if operation_required == 1:
        bucket_name = inputRequests.input_bucket_name()
        BucketGetter(bucket_name).get_bucket()

    # Verify File existence
    elif operation_required == 2:
        bucket_name = inputRequests.input_bucket_name()
        file_name = inputRequests.input_file_name()
        FileGetter(bucket_name,file_name).get_file()

    # Verify Table existence
    elif operation_required == 3:
        table_id = inputRequests.input_table_id()
        TableGetter(table_id).get_table()

    else:
        log.info("No operation found!")
        return


if __name__ == "__main__":
    main()