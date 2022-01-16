from pymongo import MongoClient
from flask import Flask,request,jsonify



app =  Flask(__name__)

app.config['SECRET_KEY'] = 'e23739c67eade607c64f90c3ebb479ca' 


client= MongoClient("mongodb://localhost:27017")
db = client.coursebooks

if __name__ ==  '__main__':
    app.run(debug=True)

from coursebook import routes