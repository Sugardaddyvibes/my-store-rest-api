
import sqlite3
from unittest import result
from flask_restful import Resource,reqparse
from flask import Request
from models.user import UserModel







class user_register(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('username',
    type=str,required= True,
            help = 'you have to put the username please'
        )
    parser.add_argument('password',
    type=str,required= True,
            help = 'you have to put the password please'
        )
   
    def post(self):
        data = user_register.parser.parse_args()
        if  UserModel.get_username(data['username']):
            return{'message':'the user already exist'},400
        user=UserModel(data['username'],data['password'])
        user.save_to_db()
        return{'message': 'the user have been created successfully'},201
