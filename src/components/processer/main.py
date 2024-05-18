from components.gcp_lib.big_query.bigQueryGetter import TableGetter
from components.gcp_lib.cloud_storage.storageGetter import FileGetter, BucketGetter
from components.logger import Log
from components import inputRequests


log_instance = Log()
log = log_instance.logger()


def main():

    operation_required = inputRequests.input_operation()

    # Verify Bucket existence
    if operation_required == 1:
        # log.info("Your request is to verify the existence of a bucket in Cloud Storage")
        bucket_name = inputRequests.input_bucket_name()
        BucketGetter(bucket_name).get_bucket()

    # Verify File existence
    elif operation_required == 2:
        # log.info("Your request is to verify the existence of a blob in Cloud Storage")
        bucket_name = inputRequests.input_bucket_name()
        file_name = inputRequests.input_file_name()
        FileGetter(bucket_name,file_name).get_file()
        # FileGetter(bucket_name, file_name).get_file_size()

    # Verify Table existence
    elif operation_required == 3:
        # log.info("Your request is to verify the existence of a table in BigQuery")
        table_id = inputRequests.input_table_id()
        TableGetter(table_id).get_table()

    else:
        log.warning("No operation found!")
        return


if __name__ == "__main__":
    main()