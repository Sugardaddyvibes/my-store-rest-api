import sqlite3
from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import  JWT ,jwt_required
from security import aunthentication,identity
from resources.user import user_register
from resources.items import Item,ItemList
from resources.store import Store,StoreList
from db import db
   

   



app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.secret_key='jose'  
api = Api(app)
jwt= JWT(app,aunthentication,identity) 
db.init_app(app) 





api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(user_register,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
@app.before_first_request
def create_tables():
   db.create_all()
         
            
       
      
    
      
        
            

        


if __name__=='__main__':
   app.run(port=5000,debug=True) 
   
    
      
    
    
    

    
    
   
            
        
       
         
 
 
   


