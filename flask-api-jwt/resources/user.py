from flask import request
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.models import User
import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()
        firstName = json_data.get('firstName')
        lastName = json_data.get('lastName')
        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        is_active = False
        is_admin = False


        print(User.get_by_username(username))
        # check if user already exists
        if User.get_by_username(username):
            return {'message': 'username already exists'}, HTTPStatus.BAD_REQUEST
        
        print(User.get_by_email(email))
        # check if email already exists
        if User.get_by_email(email):
            return {'message': 'email already exists'}, HTTPStatus.BAD_REQUEST

        # hash password
        password = hash_password(non_hash_password)

        user = User(
            firstName=firstName,
            lastName=lastName,
            username=username,
            email=email,
            password=password,
            crated_at=created_at,
            updated_at=updated_at,
            is_active=is_active,
            is_admin=is_admin
        )
        user.save()

        data = {
            'firstName': user.firstName,
            'lastName': user.lastName,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active,
            'is_admin': user.is_admin
        }

        return data, HTTPStatus.CREATED

class UserResource(Resource):
    @jwt_required(optional=True)
    def get(self, username):
        user = User.get_by_username(username=username)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user == str(user.id):
            data = {
                'firstName': user.firstName,
                'lastName': user.lastName,
                'username': user.username,
                'email': user.email,
            }
        else:
            data = {
                'username': user.username
            }
        
        return data, HTTPStatus.OK

class MeResource(Resource):
    @jwt_required(optional=False)
    def get(self):
        # compare mongodb id with jwt string id
        user = User.get_by_id(id=ObjectId(get_jwt_identity()))

        data = {
            'firstName': user.firstName,
            'lastName': user.lastName,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active,
            'is_admin': user.is_admin
        }

        return data, HTTPStatus.OK