$( document ).ready(function() {
    // $('.datepicker-input').html('nogos nagasht')
});

$('.datepicker-input').change(function() {
    var date = $(this).val();
    $('#cover').css('display', 'none');
});

$(document).on('input', '#id_no_of_pages', function(){
    var pages = $("#id_no_of_pages").val();
    var no_of_pages = pages * 275;
    $('#no-of-pages').html(no_of_pages);
})