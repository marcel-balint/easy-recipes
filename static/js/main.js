$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
});

	$(document).ready(function() {
    var wrapper = $("#ingredients"); 
    var add_button = $("#add"); 
   
    var x = 1;
    
    //  add/remove functionality for ingredients fields
   $(add_button).click(function(){ // on click add a new textarea field
            $(wrapper).append('<div class="input-field col s12 m12 l12" id="ingredients">' +
                    '<textarea id="icon_prefix2" class="materialize-textarea" id="ingredients" name="ingredients" required></textarea><a href="#" class="remove-field">Remove</a></div>');
            x++; 
    });
   
    $(wrapper).on("click",".remove-field", function(e){ //on click remove textarea field
       e.preventDefault(); 
		$(this).parent('div').remove(); 
		x--;
    });

});


    //  add/remove functionality for directions fields
	$(document).ready(function() {
    var wrapper = $("#directions"); 
    var add_button = $("#add-directions"); 
   
    var x = 1;
    
   $(add_button).click(function(){ // on click add a new textarea field
            $(wrapper).append('<div class="input-field col s12 m12 l12" id="directions">' +
                    '<textarea id="icon_prefix2" class="materialize-textarea" id="directions" name="directions" required></textarea><a href="#" class="remove-field">Remove</a></div>');
            x++; 
    });
   
    $(wrapper).on("click",".remove-field", function(e){ //on click remove textarea field
       e.preventDefault(); 
		$(this).parent('div').remove(); 
		x--;
    });
});
