# _GCP Python Project_

  </a>
  <a href="https://www.python.org/downloads/release/python-311">
    <img src="https://img.shields.io/badge/python-3.11-blue.svg" lazyload />
  </a>
  </a>
  <a href="https://cloud.google.com/python/docs/reference/storage/latest">
    <img src="https://img.shields.io/badge/CloudStorage lib-2.16.0-lightblue.svg" lazyload />
  </a>
  </a>
  <a href="https://cloud.google.com/python/docs/reference/bigquery/latest">
    <img src="https://img.shields.io/badge/BigQuery lib-3.21.0-lightgreen.svg" lazyload />
  </a>
  </a>
  <a href="https://cloud.google.com/python/docs/reference/pubsub/latest">
    <img src="https://img.shields.io/badge/Pub/Sub lib-2.21.1-bluegreen.svg" lazyload />
  </a>

####

## References

[Poetry Doc](https://python-poetry.org/docs/)

[Cloud Storage Doc](https://cloud.google.com/storage/docs?hl=i)

[BigQuery Doc](https://cloud.google.com/bigquery/docs?hl=it)

[Pub/Sub Doc](https://cloud.google.com/pubsub/docs?hl=it)



####


## Introduction
This is a basic Python project managed by Poetry, designed to interact 
with Google APIs and utilize core Google Cloud Platform libraries.

## Main Architecture (to update)
The structure of the project is based on the Object Oriented Paradigm.
####
The first two classes implemented in the **cloudClientConnector.py**:
    
    class CloudStorageClient(CloudClient)
    -> Variables: client
    -> Methods:
        - def connect()
        - def get_client()

    class BigQueryClient(CloudClient)
    -> Variables: client
    -> Methods:
        - def connect()
        - def get_client()

    class PublisherClient(CloudClient)
    -> Variables: client
    -> Methods:
        - def connect()
        - def get_client()

    class SubscriberClient(CloudClient)
    -> Variables: client
    -> Methods:
        - def connect()
        - def get_client()

are used to encapsulate the Cloud Storage, BigQuery and Pub/Sub client connection operations.
####
In the **storageGetter.py** other two classes are defined:
    
    class BucketGetter
    -> Variables: bucket_name, __storage_client
    -> Methods:
        - def declare_bucket()
        - def get_bucket()
        - def list_buckets()
        - def list_files()

    class FileGetter
    -> Variables: file_name, bucket_name, __bucket_getter
    -> Methods:
        - def declare_file()
        - def get_file()
        - def get_file_size()

that consent to instantiate a Bucket object and a File object 
containing the get methods in order to have access to the storage object desired. 

####
In the **bigQueryGetter.py** the connection to a BQ table is defined as follows:
    
    class TableGetter
    -> Variables: table_id, __big_query_client
    -> Methods:
        - def declare_table()
        - def get_table()

All these classes are used in the "Manager" layer which represents the base modules
used by tools like the **processer.main.py**.
All the logs generated are customized in the **logger.py**.

### Code Flow (to update)
<p align="center">
  <img src="doc\img\api_python_project_code_flow.png" />
</p>
<br>

### Class Diagram (to update)
<p align="center">
  <img src="doc\img\CLASS_DIAGRAM.png" />
</p>
<br>