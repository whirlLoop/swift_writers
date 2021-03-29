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

$('#remove-messages-bar').on('click', function(){
    $('.messages').fadeOut(600);
});

setTimeout(() => { $('.messages').fadeOut(600); }, 5000);

$(".dropdown-container").hover( function () {
    $(".dropdown").animate({
        height: "toggle",
        opacity: "toggle",
    });
    $(".order-btn").css({
        "border-radius": "5px 5px 0 0"
    });
}, function () {
    $(".dropdown").animate({
        height: "toggle",
        opacity: "toggle",
    });
    $(".order-btn").css({
        "border-radius": "5px"
    });
});

$(".mobile-dropdown-container").on('click', function () {
    $(".mobile-dropdown").animate({
        height: "toggle",
        opacity: "toggle",
    });
    $(".order-btn").css({
        "border-radius": "5px 5px 0 0"
    });
});