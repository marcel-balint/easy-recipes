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
   - **Add Recipes** - links to page with a form where a user can add a new recipe: on hover, the text and the border bottom transitions into a white color(`#fff`);
 
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
    - Users are able to edit a recipe by clicking the _Edit_ button that will be displayed on top-right side of the recipe page.
      A form pre-populated with the details from the recipe record will be displayed. Users can make any changes that they require.
- **Delete Recipes**
    - Users may choose to delete any recipe by clicking the _Delete_ button from the recipe page page (the recipe is deleted from the database). 

#### Features Left to Implement

- Filtering - functionality to filter recipes by author, cook time, type of meal.
- Pagination
    