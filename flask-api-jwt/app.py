from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from pymongo import MongoClient
import paho.mqtt.client as mqtt
import sys

app = Flask(__name__)

# Initialize MongoDB connection
try:
    client = MongoClient("mongodb+srv://julio:borden16@testing.zvaswda.mongodb.net/apli2?retryWrites=true&w=majority")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
    sys.exit()

db = client["apli2"]

# Enable CORS
cors = CORS()
cors.init_app(app=app)

# MQTT credentials
mqtt_host = "23.22.94.118"
mqtt_user = "julio"
mqtt_password = "borden16"
mqtt_topic = "leds"

# LED dictionary
led_status = {
    2: "OFF",
    12: "OFF",
    13: "OFF",
    14: "OFF",
    15: "OFF",
}

# Create a new collection for LED status in MongoDB
led_status_collection = db["led_status"]

def on_publish(client, userdata, mid):
    print("Message Published")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Coonection to MQTT Broker failed with error code {rc}")
    
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection from MQTT Broker with code {rc}")

@app.route("/api/control-led", methods=["POST"])
def control_led():
    try:
        data = request.get_json()
        led_number = data['ledNumber']
        new_status = data['status']

        if led_number not in led_status:
            return jsonify({
                'message': 'LED number not found'
            }), 404
        
        # Update LED status
        led_status[led_number] = new_status

        # Create a new LED status document in mongoDB
        led_status_document = {
            'led_number': led_number,
            'status': new_status,
            'timestamp': datetime.utcnow()
        }
        led_status_collection.insert_one(led_status_document)

        # Create a new MQTT client for each request
        mqtt_client = mqtt.Client()
        mqtt_client.username_pw_set(mqtt_user, mqtt_password)
        mqtt_client.on_publish = on_publish
        mqtt_client.on_connect = on_connect
        mqtt_client.on_disconnect = on_disconnect

        try:
            # Connect to MQTT broker
            mqtt_client.connect(mqtt_host, 1883, 20)

            # Publish MQTT message
            mqtt_message = f"Led{led_number}:{new_status.upper()}"
            mqtt_client.publish(mqtt_topic, mqtt_message)

            # Disconnect MQTT client
            mqtt_client.disconnect()
        except Exception as mqtt_error:
            return jsonify({
                'error': 'MQTT Error',
                'message': str(mqtt_error)
            }), 500
        
        return jsonify({
            'message': f'LED {led_number} is now {new_status}'
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Invalid request'
        }), 400
    
@app.route("/api/led-status/<int:led_number>", methods=["GET"])
def get_led_status(led_number):
    try:
        # Query the database for LED status based on the led_number
        led_status_db = led_status_collection.find({'led_number': led_number}).sort('timestamp', -1).limit(1)
        

        document_count = 0
        for _ in led_status_db:
            document_count += 1

        if document_count == 0:
            return jsonify({'message': f'LED {led_number} status not found'}), 404

        # Reset the cursor to the beginning of the query
        led_status_db.rewind()

        led_status_db = led_status_db[0]

        return jsonify({
            'ledNumber': led_status_db['led_number'],
            'status': led_status_db['status'],
            'timestamp': led_status_db['timestamp'].strftime("%m/%d/%Y, %H:%M:%S")
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'error': 'Invalid request'
        }), 400

@app.route('/api/all-led-status', methods=['GET'])
def get_all_led_status():
    try:
        # Query the database for the most recent status of all LEDs, limited to 100 entries
        led_status_db = led_status_collection.find().sort('timestamp', -1).limit(50)

        # Create a list to store LED status data
        led_status_data = []

        for entry in led_status_db:
            led_status_data.append({
                'ledNumber': entry['led_number'],
                'status': entry['status'],
                'timestamp': entry['timestamp'].strftime("%m/%d/%Y, %H:%M:%S")
            })
        
        return jsonify(led_status_data), 200
    except Exception as e:
        return jsonify({
            'error': 'Invalid request'
        }), 400
    
@app.route('/api/led-status', methods=['GET'])
def get_led_status_query():
    # Get the last status of each LED
    try:
        led_status_db = led_status_collection.aggregate([
            {
                '$sort': {'timestamp': -1}
            },
            {
                '$group': {
                    '_id': '$led_number',
                    'status': {'$first': '$status'},
                    'timestamp': {'$first': '$timestamp'}
                }
            }
        ])

        led_status_data = []

        for entry in led_status_db:
            led_status_data.append({
                'ledNumber': entry['_id'],
                'status': entry['status'],
                'timestamp': entry['timestamp'].strftime("%m/%d/%Y, %H:%M:%S")
            })
        
        return jsonify(led_status_data), 200
    except Exception as e:
        return jsonify({
            'error': 'Invalid request'
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
