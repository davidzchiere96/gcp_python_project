"""Logger helper"""
import uuid
import logging

class Log:
    def logger(self):
        # Create transaction id
        transaction_id = str(uuid.uuid4())
        # Create log configurations
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(threadName)s | GCP_API_python_project | {transaction_id} | %(message)s".format(transaction_id=transaction_id),
            handlers=[
                logging.StreamHandler()
            ])
        # Create logger
        logger = logging.getLogger()
        return logger
