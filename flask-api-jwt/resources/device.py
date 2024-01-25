from flask import Flask, request
from flask_restful import Resource
from http import HTTPStatus
from models.models import Device, User, Gpio
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from bson import ObjectId

class DeviceRegisterResource(Resource):
    @jwt_required(optional=False)
    def post(self):
        json_data = request.get_json()
        deviceName = json_data.get('deviceName')
        deviceType = json_data.get('deviceType')
        deviceModel = json_data.get('deviceModel')

       # create new device and link to user
        user_id = ObjectId(get_jwt_identity())
        
        current_user = User.get_by_id(id=user_id)

        device = next((device for device in current_user.devices if device.deviceName == f"{current_user.username}_{deviceName}"), None)
        if device is not None:
            return {'message': 'Device already registered'}, HTTPStatus.BAD_REQUEST
        
        # create new device
        device = Device(
            deviceName=f"{current_user.username}_{deviceName}",
            deviceType=deviceType,
            deviceModel=deviceModel,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            is_active=True
        )
        device.save()

        # add device to user
        current_user.devices.append(device)
        current_user.save()

        message = {
            'message': f"Device {deviceName} registered successfully",
        }

        return message, HTTPStatus.CREATED


class GPIORegisterResource(Resource):
    @jwt_required(optional=False)
    def post(self):
        json_data = request.get_json()
        gpioName = json_data.get('gpioName')
        gpioDescription = json_data.get('gpioDescription')
        gpioPin = json_data.get('gpioPin')
        deviceName = json_data.get('deviceName')

        user_id = ObjectId(get_jwt_identity())
        current_user = User.get_by_id(id=user_id)

     

        # check if device exists and belongs to user 
        device = next((device for device in current_user.devices if device.deviceName == f"{current_user.username}_{deviceName}"), None)
        if device is None:
            return {'message': 'Device not found'}, HTTPStatus.NOT_FOUND
        
        # check if gpioName and gpioPin already exists 
        gpio = next((gpio for gpio in device.gpios if (gpio.gpioName == f"{device.deviceName}_{gpioName}" or gpio.gpioPin == gpioPin)), None)
        if gpio is not None:
            return {'message': 'GPIO already registered'}, HTTPStatus.BAD_REQUEST
        
        # create new GPIO
        gpio = Gpio(
            gpioName=f"{device.deviceName}_{gpioName}",
            gpioDescription=gpioDescription,
            gpioPin=gpioPin,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        gpio.save()

        # add GPIO to device
        device.gpios.append(gpio)
        device.save()

        message = {
            'message': f"GPIO {gpioName} registered successfully",
        }

        return message, HTTPStatus.CREATED 

