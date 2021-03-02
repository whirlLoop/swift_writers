$( document ).ready(function() {
    // $('.datepicker-input').html('nogos nagasht')
});

$('.datepicker-input').change(function() {
    var date = $(this).val();
    $('#cover').css('display', 'none');
});