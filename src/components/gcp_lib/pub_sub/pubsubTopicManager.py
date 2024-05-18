from components.cloudClientConnector import PubSubClient
from components.logger import Log
import components.inputRequests


log_instance = Log()
log = log_instance.logger()

class Topic:
    def __init__(self, project_id, topic_id):

        self.__pubsub_client = PubSubClient().get_client()
        self.project_id = project_id
        self.topic_id = topic_id
        self.topic_path = self.__pubsub_client.topic_path(self.project_id, self.topic_id)


    def create_topic(self):

        topic = self.__pubsub_client.create_topic(request={"name": self.topic_path})
        log.info(f"Topic '{topic.name}' created succesfully!")

        return topic

