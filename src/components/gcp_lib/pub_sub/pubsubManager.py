from components.cloudClientConnector import PublisherClient, SubscriberClient
from components.logger import Log
import components.inputRequests
import json


log_instance = Log()
log = log_instance.logger()

class Topic:
    def __init__(self, project_id, topic_id):

        self.__pub_client = PublisherClient().get_client()
        self.project_id = project_id
        self.topic_id = topic_id
        self.topic_path = self.__pub_client.topic_path(self.project_id, self.topic_id)

    def create_topic(self):

        topic = self.__pub_client.create_topic(request={"name": self.topic_path})
        log.info(f"Topic '{topic.name}' created succesfully!")

        return topic


#topic = Topic("training-gcp-309207","chieregatod_topic")
# topic.create_topic()

class Message:
    def __init__(self, project_id, topic_id, message):

        self.__pub_client = PublisherClient().get_client()
        self.topic_path = Topic(project_id, topic_id).topic_path
        self.message = message

    def publish_message(self):

        message = self.__pub_client.publish(self.topic_path, json.dumps(self.message).encode())
        log.info(f"Published message ID: '{message.result()}'")

        return message


# message = Message("training-gcp-309207","chieregatod_topic", "ciao")
# message.publish_message()

class Subscription:
    def __init__(self, project_id, topic_id, subscription_id):

        self.__sub_client = SubscriberClient().get_client()
        self.topic_path = Topic(project_id, topic_id).topic_path
        self.subscription_path = self.__sub_client.subscription_path(project_id, subscription_id)

    def create_subscription(self):
        self.__sub_client.create_subscription(name=self.subscription_path, topic=self.topic_path)

        return self.subscription_path

    def callback(self, message):
        log.info(f"Call back function with message: '{message.data}'")
        message.ack()

        return message

    def subscribe(self):
        future = self.__sub_client.subscribe(self.subscription_path, self.callback)

        return


# message = Message("training-gcp-309207","chieregatod_topic", "ciao")
# message.publish_message()

# sub = Subscription("training-gcp-309207","chieregatod_topic","chieregatod_subscription")
# sub.create_subscription()