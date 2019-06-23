$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
});

	$(document).ready(function() {
    var wrapper = $("#ingredients"); 
    var add_button = $("#add"); 
   
    var x = 1;
    
   $(add_button).click(function(){ // on click add new textarea field
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

