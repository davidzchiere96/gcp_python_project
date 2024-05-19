from components.cloudClientConnector import PublisherClient, SubscriberClient
from components.logger import Log
from concurrent.futures import TimeoutError

timeout = 15.0    # timeout in seconds

log_instance = Log()
log = log_instance.logger()

class Subscriber:
    def __init__(self, project_id, topic_id, subscription_id):

        self.__sub_client = SubscriberClient().get_client()
        self.subscription_id = subscription_id
        self.subscription_path = self.__sub_client.subscription_path(project_id, subscription_id)

    def callback(self, message):
        log.info(f"Recieved message message with data: '{message.data}'")
        message.ack() # message acknowledge

        return message

    def subscribe(self):
        streaming_pull_future = self.__sub_client.subscribe(self.subscription_path, callback=self.callback)

        try:
            streaming_pull_future.result(timeout = timeout)
        except TimeoutError:
            streaming_pull_future.cancel()
            streaming_pull_future.result()
        return
