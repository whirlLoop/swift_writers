$( document ).ready(function() {
    var d = new Date();
    $("#year").html(d.getFullYear());
});

$('#mobile-menu-icon').click(function (){
    $(".mobile-menu-items").animate({
        height: "toggle",
        opacity: "toggle",
    });
    $('#mobile-menu-icon').toggleClass("fa-bars fa-times");
});