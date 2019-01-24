$(document).ready(function() {

    var valueof = $("#valueof");
    var button_clear = $("#clear");
    var button_withdraw = $("#withdraw");
    var button = $(".number");

    button.on("click", function() {
        var currentvalue = $("#valueof").val();
        var value = ($(this).attr('id'));
        valueof.attr('value', (currentvalue + value));
    });

    // button_withdraw.on("click", function() {
    //     $("#button_withdraw").attr("disabled", null);
    //
    // });

    button_clear.on("click", function() {
        valueof.attr('value', null);
        $(".number").removeAttr("disabled");
    });

});




