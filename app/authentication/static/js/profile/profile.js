$( document ).ready(function() {
  const hashLocation = localStorage.getItem('hashLocation');
  const targetEvent = localStorage.getItem('targetEvent');
  console.log(targetEvent);
  if( hashLocation && targetEvent){
    const hashLocation = localStorage.getItem('hashLocation');
    openNestedTab(targetEvent, hashLocation);
  }else {
    $("#defaultNestedOpen").click();
  }
  element.autocomplete = isGoogleChrome() ? 'disabled' :  'off';
});

// if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
//   var url = window.location.href;
//   console.log( url );
//   // window.location.href = url;
//   var hash = window.location.hash;
//   if( hash ){
//     // console.log($(hash));
//     hash = hash.substring(1);
//     console.log(id + ' removed has');
//     openNestedTab(this, hash);
//   }
//   //  return false;
// } else {
//   console.info( "This page is not reloaded");
// }

$("#profileSection").ready(
  function () {
    $("#defaultOpen").click();
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

    // window.location.hash = tabName;
    // return false;
}

// function hashWindow(hash){
//   window.location.hash = hash;
//   return false;
// }

function openNestedTab(evt, nestedTab) {
  // Declare all variables
  var i, nestedTabContent, tablinks;
  // Get all elements with class="tabcontent" and hide them
  nestedTabContent = $(".nestedTabContent");
  for (i = 0; i < nestedTabContent.length; i++) {
    nestedTabContent[i].style.display = "none";
  }
  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = $(".tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  // Show the current tab, and add an "active" class to the button that opened the tab
  // document.getElementById(nestedTab).style.display = "block";
  $(`#${nestedTab}`).show();
  evt.currentTarget.className += " active";

  localStorage.setItem('hashLocation', nestedTab);
  localStorage.setItem('targetEvent', evt);
  console.log(evt.currentTarget);
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