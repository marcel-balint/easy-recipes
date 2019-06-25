$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();


    //  add/remove functionality for ingredients fields
    var wrapper = $("#ingredients"); 
    var add_button = $("#add"); 
   
    var x = 1;
    
   $(add_button).click(function(){ // on click add a new textarea field
            $(wrapper).append('<div class="input-field col s12 m12 l12" id="ingredients">' +
                    '<textarea id="icon_prefix2" class="materialize-textarea" id="ingredients" name="ingredients" required ></textarea><a href="#" class="remove-field">Remove</a></div>');
            x++; 
    });
   
    $(wrapper).on("click",".remove-field", function(e){ //on click remove textarea field
       e.preventDefault(); 
		$(this).parent('div').remove(); 
		x--;
    });



    //  add/remove functionality for directions fields
    var wrapper_dirctions = $("#directions"); 
    var add_button_directions = $("#add-directions"); 
   
    var x = 1;
    
   $(add_button_directions).click(function(){ // on click add a new textarea field
            $(wrapper_dirctions).append('<div class="input-field col s12 m12 l12" id="directions">' +
                    '<textarea id="icon_prefix2" class="materialize-textarea" id="directions" name="directions" required></textarea><a href="#" class="remove-field">Remove</a></div>');
            x++; 
    });
   
    $(wrapper_dirctions).on("click",".remove-field", function(e){ //on click remove textarea field
       e.preventDefault(); 
		$(this).parent('div').remove(); 
		x--;
    });
    
    var home_text = $(".responsive-img");
    $(home_text).append("<p class='center-align home-text'>Welcome to Easy Recipes! Here you can create, update or delete your very own recipes</p>")

});