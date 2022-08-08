from unicodedata import name
from  flask_restful import Resource,reqparse

from  models.store import StoreModel

class Store(Resource):
    parser=reqparse.RequestParser()
    def get(self,name):
        store=StoreModel.find_name(name)
        if store:
            return store.json()
        return {'message':'this store is not avaiable'},404
    def post(self,name):
        if StoreModel.find_name(name) is not None:
            return {'message':'the store {} is already available'.format(name)},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'the was an error '},500
        return store.json(),201
    def delete(self,name):
        store=StoreModel.find_name(name)
        if store:
            store.delete_from_db()
        return{'message':'the item have been deleted'}
class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}

