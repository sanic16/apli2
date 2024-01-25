import paho.mqtt.client as mqtt
from passlib.hash import pbkdf2_sha256


def on_publish(client, userdata, mid):
    print("Message Published")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Connection to MQTT Broker failed with error code {rc}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection from MQTT Broker with code {rc}")

# MQTT client function connection
def mqtt_message(username: str, password: str, host: str, topic: str, message: str) -> bool:
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(
        username=username,
        password=password
    )
    mqtt_client.on_publish = on_publish
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect

    try:
        # Connect to MQTT broker
        mqtt_client.connect(
            host = host,
            bind_port = 1883,
            keepalive = 20
        )

        # Publish MQTT message
        mqtt_client.publish(
            topic=topic,
            payload=message,
        )

        # Disconnect MQTT client
        mqtt_client.disconnect()

        return True
    except Exception as mqtt_error:
        print(mqtt_error)
        return False
    
def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)

def check_password(password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(password, hashed_password)
    