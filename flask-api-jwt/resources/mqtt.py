from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from config import Credentials
from utils import mqtt_message
from models.models import User, Device, Gpio, GpioStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from datetime import datetime

class ControlDeviceResource(Resource):
    @jwt_required(optional=False)
    def post(self):
        data = request.get_json()
        led_number: int = data['ledNumber']
        new_status: str = data['status']
        gpioName = data.get('gpioName')
        deviceName = data.get('deviceName')

        current_user = User.get_by_id(id=ObjectId(get_jwt_identity()))

        # check if device exists and belongs to current user
        device = next((device for device in current_user.devices if device.deviceName == f"{current_user.username}_{deviceName}"), None)
       
        if device is None:
            return {'message': 'Device not found'}, HTTPStatus.NOT_FOUND

        # check if gpio exists and belongs to current device
        gpio = next((gpio for gpio in device.gpios if gpio.gpioName == f"{device.deviceName}_{gpioName}"), None)
        
        if gpio is None:
            return {'message': 'GPIO not found'}, HTTPStatus.NOT_FOUND 
        
        # check is led_number is the same as gpioPin
        if gpio.gpioPin != led_number:
            return {'message': 'gpioPin and ledNumber do not match'}, HTTPStatus.BAD_REQUEST

        status = new_status.lower() == 'on' 
        
        gpio_status = GpioStatus(
            gpioStatus=bool(status),
            created_at=datetime.now(),
        )
        gpio_status.save()

        # add gpio status to gpio
        gpio.gpioStatus.append(gpio_status)
        gpio.save()

        mqtt_message(
            username=Credentials.mqtt_user,
            password=Credentials.mqtt_password,
            host=Credentials.mqtt_host,
            topic=Credentials.mqtt_topic,
            message=f"Led{led_number}:{new_status.upper()}"
        )

        return jsonify({
            'message': f'Led{led_number} is now {new_status.upper()}'
        })

class StatusDeviceResource(Resource):
    @jwt_required(optional=False)
    # retrieve the last gpioStatus of all gpios of a device of a specific user
    def get(self, device_name):
        current_user = User.get_by_id(id=ObjectId(get_jwt_identity()))

        device = next((device for device in current_user.devices if device.deviceName == f"{current_user.username}_{device_name}"), None)

        # check if device exists and belongs to current user and check if device has gpios
        if device is None:
            return {'message': 'Device not found'}, HTTPStatus.NOT_FOUND
        
        if len(device.gpios) == 0:
            return {'message': 'Device has no GPIOs'}, HTTPStatus.NOT_FOUND
        
        # retrieve the last gpioStatus of all gpios 
        
        
        data = []
        # format datetime
        for gpio in device.gpios:
            if gpio.last_gpioStatus is not None:
                data.append({
                'gpioName': gpio.gpioName,
                'gpioStatus': gpio.last_gpioStatus.gpioStatus,
                'created_at': gpio.last_gpioStatus.created_at.strftime("%d/%m/%Y, %H:%M:%S")
            })
        print(data)
        return data, HTTPStatus.OK

        
       
