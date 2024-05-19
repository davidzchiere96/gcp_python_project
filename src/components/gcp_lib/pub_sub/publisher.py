from components.cloudClientConnector import PublisherClient, SubscriberClient
from components.logger import Log
from components.gcp_lib.pub_sub.pubsubManager import Topic
import json


log_instance = Log()
log = log_instance.logger()

class Publisher:
    def __init__(self, message, project_id="training-gcp-309207", topic_id="chieregatod_topic"):

        self.__pub_client = PublisherClient().get_client()
        self.topic_path = Topic(project_id, topic_id).topic_path
        self.message = message

    def publish_message(self):

        message = self.__pub_client.publish(self.topic_path, json.dumps(self.message).encode())
        log.info(f"Published message ID: '{message.result()}'")

        return message



