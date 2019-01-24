$(document).ready(function() {

    var valueof = $("#valueof");
    var button_clear = $("#clear");
    var button = $(".number");

    button.on("click", function() {
        var currentvalue = $("#valueof").val();
        var value = ($(this).attr('id'));
        valueof.attr('value', (currentvalue + value));
    });

    button_clear.on("click", function() {
        valueof.attr('value', null);
        $(".number").removeAttr("disabled");
    });

});




