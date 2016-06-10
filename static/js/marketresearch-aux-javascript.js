$(document).ready (function() {

    $('.glyphicon-heart').on('click', function() {
        console.log("Inside the glypicon whatever");
        $('.glyphicon-heart').addClass('selected');
    });
});