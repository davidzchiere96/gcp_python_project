from storageBucketManager import Bucket, manage_bucket
from storageFileManager import File, manage_file
from storageObjectGetter import FileGetter, BucketGetter
import logger
import inputRequests


log = logger.logger()

def get_infos(info_required):

    # Get file size
    if info_required == 1:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        # file_path = inputRequests.input_source_file_path()
        FileGetter(bucket_name, file_name).get_file_size()

    # List of files within a bucket
    elif info_required == 2:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_prefix = inputRequests.input_file_prefix()
        FileGetter(bucket_name).list_files(file_prefix)

    else:
        log.info("No info retrieved!")
        return

def manage_objects(operation_required):

    # Manage bucket
    if operation_required == 1:
        manage_bucket()

    # Manage blob
    elif operation_required == 2:
        manage_file()

    else:
        log.info("No object found!")
        return


def main():

    domain_required = inputRequests.input_domain()
    if domain_required == 1:
        info_required = inputRequests.input_to_get_info()
        get_infos(info_required)
    elif domain_required == 2:
        operation_required = inputRequests.input_operation()
        manage_objects(operation_required)
    else:
        log.info("No action domain found!")
        return


if __name__ == "__main__":
    main()