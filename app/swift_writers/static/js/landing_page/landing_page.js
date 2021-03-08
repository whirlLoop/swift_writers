$( document ).ready(function() {
    // $('.datepicker-input').html('nogos nagasht')
});

$('.datepicker-input').change(function() {
    $('#cover').css('display', 'none');
});

$(document).on('input', '#id_no_of_pages', function(){
    var pages = $("#id_no_of_pages").val();
    if (pages > 0){
        var no_of_pages = pages * 275;
        $('#no-of-pages').html(no_of_pages);
        var price = pages * 9;
        $('#total-cost').html(price);
    }else {
        $("#id_no_of_pages").html(1);
    }
})