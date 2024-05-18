import os
from logger import Log


log_instance = Log()
log = log_instance.logger()

class LocalFileGetter:
    def __init__(self, local_file_path):
        # self.file_name = file_name
        self.local_file_path = local_file_path

    def get_local_file_size(self):
        """Get the size of a local file."""
        # Check if the file exists
        if os.path.exists(self.local_file_path):
            # Get the size of the file
            size_in_bytes = float(os.path.getsize(self.local_file_path))
            size_in_kb = size_in_bytes/1024
            size_in_mb = size_in_kb/1024
            size_in_gb = size_in_mb/1024

            log.info(f"File '{self.local_file_path}' size is: '{size_in_gb}'GB")
            return size_in_gb
        else:
            return None
