import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipesProject'
app.config['MONGO_URI'] = 'mongodb+srv://marcel:Euskaltel@myfirstcluster-r0di4.mongodb.net/recipesProject?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route("/")
@app.route('/home')
def home():
    _countries = mongo.db.countries.find()
    countries_list = [countries for countries in _countries]
    return render_template('home.html', countries=countries_list)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
    