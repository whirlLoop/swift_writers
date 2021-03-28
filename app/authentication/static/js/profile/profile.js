$( document ).ready(function() {
    $("#defaultOpen").click();
    element.autocomplete = isGoogleChrome() ? 'disabled' :  'off';
});

function checkScreenSizeAndChangeTabTitles() {
  if ($(window).width() <= 480){
    $('#defaultOpen').text('Profile');
    $('#historyBtn').text('History');
    $('#accountBtn').text('Account');
  }else {
    $('#defaultOpen').text('Profile Settings');
    $('#historyBtn').text('Order History');
    $('#accountBtn').text('Account Settings');
 }
}

$(window).on('load', () => {
  checkScreenSizeAndChangeTabTitles();
});

$(window).resize(function () {  // no `on` here
  checkScreenSizeAndChangeTabTitles();
});

function openTab(evt, tabName, message) {
    // Declare all variables
    var i, tabcontent, tablinks;
    // Get all elements with class="tabcontent" and hide them
    tabcontent = $(".tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = $(".tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

    $('#page-head').html(message);

}

function openFormContainer(evt, formName, displayingBtnId){
  $(`.${formName}`).css({'display':'flex', 'justify-content': 'space-between'});
  $(`#${displayingBtnId}`).css('display', 'none');
}

function closeForm(evt, formId, displayingBtnId){
  $(`.${formId}`).css('display', 'none');
  $(`#${displayingBtnId}`).css('display', 'flex');
}

$("#id_avatar").on('change', function(){
  $( "#avatar-form" ).submit();
});