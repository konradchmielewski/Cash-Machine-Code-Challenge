$(document).ready(function() {

    var input_value = $("#input_value");
    var button_clear = $("#clear");
    var button = $(".number");

    button.on("click", function() {
        var current_value = $("#input_value").val();
        var value = ($(this).attr('id'));
        input_value.attr('value', (current_value + value));
    });

    button_clear.on("click", function() {
        input_value.attr('value', null);
        $(".number").removeAttr("disabled");
    });

});




