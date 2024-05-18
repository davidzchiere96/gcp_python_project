from components.logger import Log
from components.cloudClientConnector import CloudStorageClient
from storageGetter import BucketGetter
import components.inputRequests


log_instance = Log()
log = log_instance.logger()

class Bucket:
    def __init__(self, bucket_name):

        """API connectors"""""""""""""""""""""""""""""""""""""""""""""
        self.__storage_client = CloudStorageClient().get_client()
        self.__bucket_getter = BucketGetter(bucket_name)
        self.__declare_bucket = self.__bucket_getter.declare_bucket()
        self.__get_bucket = self.__bucket_getter.get_bucket()
        self.input_bucket_name = bucket_name

        """Bucket Metadata"""""""""""""""""""""""""""""""""""""""""""""
        self.id = self.__declare_bucket.id
        self.name = self.__declare_bucket.name
        self.storage_class = self.__declare_bucket.storage_class
        self.location = self.__declare_bucket.location
        self.location_type = self.__declare_bucket.location_type
        self.lifecycle_rules = self.__declare_bucket.lifecycle_rules
        self.time_created = self.__declare_bucket.time_created
        self.versioning = self.__declare_bucket.versioning_enabled
        self.labels = self.__declare_bucket.labels
        self.retention_period = self.__declare_bucket.retention_period

        # self.object_retention_mode = self.__declare_bucket.object_retention_mode
        # self.retention_policy_effective_time
        # self.retention_policy_locked
        # self.cors = self.__declare_bucket.cors
        # self.default_event_based_hold = self.__declare_bucket.default_event_based_hold
        # print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
        # print(f"Metageneration: {bucket.metageneration}")
        # print(
        #     f"Public Access Prevention: {bucket.iam_configuration.public_access_prevention}"
        # )
        # print(f"Requester Pays: {bucket.requester_pays}")
        # print(f"Self Link: {bucket.self_link}")


    def create_bucket(self, local_zone="eu", storage_class="Standard"):
        # self.location = local_zone
        # self.storage_class = storage_class
        new_bucket = self.__storage_client.create_bucket(self.input_bucket_name, location=local_zone)
        # self.storage_class = storage_class

        log.info(
            f"New bucket '{self.input_bucket_name}' created in local zone '{local_zone}' "
            f"with storage class '{storage_class}'"
        )
        return new_bucket

    def delete_bucket(self,force=True):
        # bucket = self.__bucket_getter.get_bucket()
        bucket = self.__get_bucket
        bucket.delete(force=force)

        log.info(f"Bucket '{self.name}' deleted!")
        return

    def print_bucket_metadata(self):
        metadata = {
            'id': self.id,
            'name': self.name,
            'storage_class': self.storage_class,
            'location': self.location,
            'location_type': self.location_type,
            'lifecycle_rules': self.lifecycle_rules,
            'time_created': self.time_created,
            'versioning': self.versioning,
            'labels': self.labels,
            'retention_period': self.retention_period,
            'object_retention_mode': self.object_retention_mode,
        }

        log.info(f"Bucket {self.name} metadata: {metadata}")
        return

    # """Deprecated"""
    # def update_bucket_location(self, local_zone="eu"):
    #    bucket = self.__get_bucket
    #    bucket.location = local_zone
    #    log.info(f"Location for bucket '{self.name}' has been set to '{local_zone}'.")

    def update_bucket_storage_class(self, storage_class="Standard"):
        bucket = self.__get_bucket
        bucket.storage_class = storage_class   # constants.COLDLINE_STORAGE_CLASS
        bucket.patch()

        log.info(f"Default storage class for bucket '{self.name}' has been set to '{bucket.storage_class}'.")
        return

    def update_lifecycle_rules(self, operation="ADD", new_lifecycle_rules=None):  # parameters: action, value, interval
        bucket = self.__get_bucket
        if operation.strip().upper()=="ADD":
            current_rules = list(bucket.lifecycle_rules)
            current_rules.extend(new_lifecycle_rules)
            bucket.lifecycle_rules = current_rules
            bucket.patch()
            log.info(f"Lifecycle rules added successfully for bucket '{self.name}'.")

        elif operation.strip().upper()=="CLEAR":
            bucket.clear_lifecycle_rules()
            bucket.patch()
            log.info(f"Lifecycle rules deleted successfully for bucket '{self.name}'.")

        else:
            log.warning(f"No Lifecycle operation '{operation}' performed. Try with 'ADD' or 'CLEAR' operations.")


    def set_versioning(self, versioning_flag=True):
        bucket = self.__get_bucket
        bucket.versioning_enabled = versioning_flag
        bucket.patch()

        log.info(f"Versioning set to '{versioning_flag}' for bucket {self.name}")
        return

    def update_retention_policy(self, retention_period=None):
        bucket = self.__declare_bucket
        bucket.retention_period = retention_period
        bucket.patch()

        log.info(f"Retention period set to '{retention_period}' seconds for bucket {self.name}")
        return


# bucket = Bucket("bucket_chieregatod_gcs_asset")
# bucket.update_retention_policy()
# rules = [
#         {
#             "action": {"type": "Delete"},
#             "condition": {"age": 60}  # Delete objects after 30 days
#         }
#     ]
# rules = [
#         {
#             "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
#             "condition": {"age": 30}  # Move objects to Nearline storage class after 30 days
#         }
#     ]
# bucket.update_lifecycle_rules("add",rules)
# bucket.delete_bucket()
# bucket = Bucket("bucket_chieregatod_test")
# bucket.update_bucket_location()
# bucket.create_bucket(storage_class="NEARLINE")
# bucket=bucket.create_bucket("europe-west8")



def manage_bucket():
    operation_required = inputRequests.input_bucket_operation()

    if operation_required == 1:
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.create_bucket()

    elif operation_required == 2:
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.delete_bucket()

    elif operation_required == 3:
        storage_class = inputRequests.input_storage_class()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.update_bucket_storage_class(storage_class)

    else:
        log.warning("No operation found!")
        return


# buc = Bucket()
# buc.list_files("asset_storage_bucket")

# bucket_manager = Bucket()
# bucket_manager.create_bucket("asset_storage_bucket_april")
# bucket_manager.delete_bucket("asset_storage_bucket_april")
