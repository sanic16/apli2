from utils import mqtt_message
from config import credentials

result = mqtt_message(
    username=credentials['mqtt_user'],
    password=credentials['mqtt_password'], 
    host=credentials['mqtt_host'],
    topic=credentials['mqtt_topic'],
    message='Led15:ON'
)







print(result)