from ctypes import c_void_p
from multiprocessing import connection
import sqlite3
from flask_restful import Resource,reqparse
from models.items import ItemModel


from flask import request
from flask_jwt import  jwt_required
class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
           type=float,
           required=True,
           help="you have to  put in the price please "
        )
    parser.add_argument('isbn',
           type=float,
           required=True,
           help="you have to  put in the price please "
        )
    parser.add_argument('store_id',
           type=str,
           required=True,
           help="you have to  put  in a valid store id  please "
        )
        
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_name(name)
        if item:
            return item.json()
        return {'message':'the item is not avaiable'},404
   
    def post(self,name):
        if ItemModel.find_name(name) is not None:
            return {'message':"the item with name {} allready exist".format(name)},400 
        # request_data = request.get_json() 
        data = Item.parser.parse_args()
        item=ItemModel(name,data['price'],data['isbn'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message':'the was an error '},500
        return item.json(),201
   
    def delete(self,name):
        item =Item.find_name(name)
        if item:
            item.delete_from_db()
        return{'message':'the item have been deleted'}

    def put(self,name):
       
        data = Item.parser.parse_args()
        item = ItemModel.find_name(name)
        if item is None:
             item = ItemModel(name,data['price'],data['isbn'],data['store_id'])
        else:
            item.price= data['price']
            item.isbn= data['isbn']
            item.store_id=data['store_id']
        item.save_to_db()
        return item.json()
   

class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]} 