
# MQTT credentials
class Credentials:
    mqtt_host = '23.22.94.118'
    mqtt_user = 'julio'
    mqtt_password = 'borden16'
    mqtt_topic = 'leds'

class Config():
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
    # expire token in 30 days
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24 * 30
    