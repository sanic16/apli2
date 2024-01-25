from flask import Flask
from flask_restful import Api
from resources.mqtt import ControlDeviceResource, StatusDeviceResource
from resources.user import UserListResource, UserResource, MeResource
from resources.token import TokenResource
from resources.device import DeviceRegisterResource, GPIORegisterResource
from extensions import jwt, cors
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app=app)
    register_extensions(app=app)
    return app

def register_extensions(app):
    jwt.init_app(app=app)
    cors.init_app(app=app)

def register_resources(app):
    api = Api(app=app)
    
    # add resources 
    
    api.add_resource(ControlDeviceResource, '/api/device-control')
    api.add_resource(StatusDeviceResource, '/api/device-status/<string:device_name>')

    api.add_resource(UserListResource, '/api/users')
    api.add_resource(UserResource, '/api/users/<string:username>')
    api.add_resource(MeResource, '/api/users/me')

    api.add_resource(TokenResource, '/api/token')

    api.add_resource(DeviceRegisterResource, '/api/device/register')
    api.add_resource(GPIORegisterResource, '/api/gpio/register')

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )