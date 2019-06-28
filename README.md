## Easy Recipes - Data Centric Development Milestone Project

A live demo can be found [here](https://easy-recipes.herokuapp.com/).

 This is an online recipe website, where users can look up a list of recipes in a database and add their own. Recipes can be added,
 edited, and deleted by users.


## UX

#### User Stories
Users are able to:
  - access the site using their preferred device (mobile, tablet, desktop) without any loss of functionality.
  - add recipes to the site along with the URL of a picture that best represents their recipe.
  - edit any recipe in line with the requirements of the site.
  - view the details of any recipe, including all ingredients, preparation instructions, and the time required to cook the meal.
  - delete any recipe.
  

The wireframes for this website can be seen [here](https://github.com/marcel-balint/easy-recipes/tree/master/static/wireframes).

## Features

- **Navbar**, located at the top of the home page, has a background color of green(`#228B22`) and a box shadow effect. Contains two links:
   - **Home** - links back to home page: on hover, the text and the border bottom transitions into a white color(`#fff`);
   - **Add Recipes** - links to a page with a form where a user can add a new recipe. On hover, the text and the border bottom transitions into a white color(`#fff`);
 
- A background image with introduction text - This section introduces the user to the website and explains the main functionality;
- The home page features a list of 12 cards with each card containing the name of a particular country cuisine.
  - on hover, each card have a zoom effect, (will scale up to 1.03, `transform: scale(1.03);`) and a box shadow.
  - when clicked on a card, this will will bring the user to a country cuisine.
- **Add Recipes**

  Users are able to add new recipes to the database via the _Add Recipe_ page. They are asked to enter:
  - Recipe name
  - Choose a country via dropdown list (populated from the database).
  - Preparation Time
  - Cooking Time
  - Author name
  - A URL for the image that the user wishes to have displayed with their recipe.
  - Ingredients - each ingredient is entered on one line, users have the option to click on _Ad Ingredients_ button, this will append a new input field; there is also a _Remove_ button, which will remove an input field.
  - Directions -  the user will enter all the steps needed to prepare the recipe.
  
- **Recipe Detail Page**
    - When users click on a recipe card, they are taken to the recipe page. Here they are presented with 
      the full details of the recipe: recipe's author, all ingredients that they will require, the steps needed to prepare the recipe,
      information on the total time and cook time.
    - At the top-right side of the page, the user will be presented with _Edit_ and _Delete_ buttons.

- **Edit Recipes**
    - Users are able to edit a recipe by clicking the _Edit_ button that will be displayed on top-right side of each recipe page.
      A form pre-populated with the details from the recipe record will be displayed. Users can make any changes that they require.
- **Delete Recipes**
    - Users may choose to delete any recipe by clicking the _Delete_ button from the recipe page page (the recipe is deleted from the database). 

#### Features Left to Implement

- Filtering - functionality to filter recipes by author, cook time, type of meal.
- Pagination


## Technologies Used


* [HTML5](https://en.wikipedia.org/wiki/HTML) - Used for rendering the website.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - used to style the features of the website and to create responsiveness.
* [JQuery](https://code.jquery.com/jquery/) - Javascript framework used to implement custom code and initialize Materialize functions.
* [Materialize](https://materializecss.com/) - Used as the overall design framework.
* [Flask](http://flask.pocoo.org/) - Framework used to build the application.
* [Python](https://www.python.org/) - Used as the back-end programming language.
* [Heroku](https://www.heroku.com/) - Hosts the deployed version of this project.
* [MongoDB](https://www.mongodb.com/) - Used MongoDB for data storage.
* [Cloud9 IDE](https://aws.amazon.com/cloud9/) - Used to build this project.
* [GitHub](https://github.com/) - Used as remote storage of my code online.


## Testing
All pages have been tested on all screen sizes. This has been done via Google Chrome developer tools and by testing on my own personal phone and ipad.
Also all features of the page are scaling as intended in tablet and mobile devices.


I've created reipes to test the _Add Recipe_ functionality.
For several recipes, I've edited minor things like the recipe author, adding additional ingredients or directions, to test the functionality of updating a recipe to the database.
I've deleted all of my test recipes to confirm that _Delete_ functionality works properly.

If the _Add Recipe_ form is submitted without a field being completed or without containing an image URL there will be an error indicating that.

#### Validators
- **HTML** 

   Passing the HTML code from all templates into the [W3C Markup Validator](https://validator.w3.org/) generates numerous errors, but these are expected as the validator is unable to understand the 
   Jinja2 templating that builds most aspects of the page. For the HTML that does not involve Jinja2, no errors have been found.
- **CSS**
    
  The CSS code passes [W3C CSS Validation Service ](https://jigsaw.w3.org/css-validator/)without errors.

- **JavaScript**
  
  The JavaScript code passes trough [JSHint](https://jshint.com/) without errors.

- **Python**
 
  The Python code was passed through the [PEP8 Online validator](http://pep8online.com/) and is fully PEP8 compliant.
   
 The project was tested to ensure full usability across the following browsers:

  * Google Chrome

  * Mozilla Firefox

  * Microsoft Edge
  
## Deployment

Thre are no differences between the deployed version and the development version.

* Created **requirements.txt** file.
* Created **Procfile** file.
* Created a new app on _[Heroku](https://www.heroku.com/)_
* In command line:
    * `Heroku login` (login to _Heroku_)
    * `git init`
    * `git add .`
    * `git commit -m "initial deployment"`
    * `git push -u heroku master`
    * `heroku ps:scale web=1`
* In _Heroku_  on **Settings** tab clicked on the _Reveal Config Vars_ to configure environmental variables as follows:

  * **IP**: ` 0.0.0.0`, 
  * **PORT**: `5000`,
  * **MONGO_URI**: _my database link_
  
* Deploy process
   * Connected the app to _GitHub_.
   * Enabled automatic deploys from master branch.
   
 Live deployed version: https://easy-recipes.herokuapp.com/  

#### Run the project locally

Clone this GitHub repository by either clicking the green Clone or download button and downloading the project as a zip-file
* Create a **requirements.txt** file: `sudo pip3 freeze --local > requirements.txt`
* Create a **Procfile**: `echo web: python app.py > Procfile`
* Create a new app on _[Heroku](https://www.heroku.com/)_
* In command line:
    * `Heroku login` (login to _Heroku_)
    * `git init`
    * `git add .`
    * `git commit -m "initial deployment"`
    * `git push -u heroku master`
    * `heroku ps:scale web=1`
* In the Heroku **Settings** tab, click on the _Reveal Config Vars_ button to configure environmental variables as follows:
    * **IP**: `0.0.0.0`
    * **PORT**: `5000`
    * **MONGO_URI**: _link to MongoDB database_
    * Click **More** > **Restart all Dynos**
 * Your app should be successfully deployed to Heroku at this point.

## Credits
#### Content

All recipes on website are taken from [this](https://www.simplyrecipes.com/) website.
#### Media

* The background image was taken from [this](https://www.allrecipes.com/) website.
 


#### Acknowledgements

* [Code Institute](https://codeinstitute.net/) tutors