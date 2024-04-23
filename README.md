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

####

## References

[Poetry Doc](https://python-poetry.org/docs/)

[Cloud Storage Doc](https://cloud.google.com/storage/docs?hl=i)

[BigQuery Doc](https://cloud.google.com/bigquery/docs?hl=it)



####


## Introduction
This is a simple Python project managed by poetry to call Google APIs 
in order to use the main Google Cloud Platform libraries.


## Main Architecture
The structure of the project is based on the Object Oriented Paradigm.
####
The first two classes implemented in the cloudClientConnector.py**:
    
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

are used to encapsulate the Cloud Storage and BigQuery client connection operations.
####
In the **storageGetter.py** other two classes are defined:
    
    class BucketGetter
    -> Variables: bucket_name, __storage_client
    -> Methods:
        - def get_bucket()

    class FileGetter
    -> Variables: file_name, bucket_name, __bucket_getter
    -> Methods:
        - def file_bucket()

that consent to instantiate a Bucket object and a File object 
containing the get methods in order to have access to the storage object desired. 

####
Finally in the **bigQueryGetter.py** the connection to a BQ table is defined as follows:
    
    class TableGetter
    -> Variables: table_id, __big_query_client
    -> Methods:
        - def get_table()

All these classes are orchestrated by the **main.py** and the **inputRequests.py** 
and logs are customized in the **logger.py**.

### Code Flow
<p align="center">
  <img src="doc\img\GCS_ASSET_CODE_FLOW.png" />
</p>
<br>

### Class Diagram
<p align="center">
  <img src="doc\img\CLASS_DIAGRAM.png" />
</p>
<br>