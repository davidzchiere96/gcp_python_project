from components.cloudClientConnector import PublisherClient, SubscriberClient
from components.logger import Log
import components.inputRequests
import json


log_instance = Log()
log = log_instance.logger()

class Topic:
    def __init__(self, project_id="training-gcp-309207", topic_id="chieregatod_topic"):

        self.__pub_client = PublisherClient().get_client()
        self.project_id = project_id
        self.topic_id = topic_id
        self.topic_path = self.__pub_client.topic_path(self.project_id, self.topic_id)

    def create_topic(self):

        topic = self.__pub_client.create_topic(request={"name": self.topic_path})
        log.info(f"Topic '{topic.name}' created succesfully!")

        return topic


class Subscription:
    def __init__(self, project_id, topic_id, subscription_id):

        self.__sub_client = SubscriberClient().get_client()
        self.topic_path = Topic(project_id, topic_id).topic_path
        self.subscription_id = subscription_id
        self.subscription_path = self.__sub_client.subscription_path(project_id, subscription_id)

    def create_subscription(self):
        self.__sub_client.create_subscription(name=self.subscription_path, topic=self.topic_path)
        log.info(f"Subscription '{self.subscription_id}' created succesfully!")
        return self.subscription_path



