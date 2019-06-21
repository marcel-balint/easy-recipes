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
   
    
@app.route('/countries/<country_recipes>')
def show_recipes_by_country(country_recipes):
    recipes = mongo.db.recipes.find({'country': country_recipes})
    recipes_list = [recipe for recipe in recipes]
    return render_template('countries/country.html', recipes=recipes_list)


@app.route('/recipes/<recipe>')
def dispaly_recipe(recipe):
    _recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe)})
    return render_template('/recipes/recipe_page.html', recipe=_recipe)

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
    