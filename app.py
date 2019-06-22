import os
import re
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
    _countries = mongo.db.countries.find()
    country_list = [country for country in _countries]
    return render_template('add_recipe.html', countries= country_list)

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipe = mongo.db.recipes
    
    form = request.form.to_dict()
    directions = []
    ingredients = []
        
    for key in form:
        regex = re.compile("^directions")
        if regex.match(key):
            directions.append(form[key]) 
        
    for key in form:
        regex = re.compile("^ingredient")
        if regex.match(key):
            ingredients.append(form[key])
        
    recipe.insert_one({
            "recipe_name": request.form.get("recipe_name"),
            "country": request.form.get("country"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": ingredients,
            "author": request.form.get("author"),
            "directions": directions
        })        
        
    return redirect('home')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    