$( document ).ready(function() {
  const hashLocation = localStorage.getItem('hashLocation');
  const targetEvent = localStorage.getItem('targetEvent');
  if( hashLocation && targetEvent){
    const hashLocation = localStorage.getItem('hashLocation');
    openNestedTab(targetEvent, hashLocation);
  }else {
    $("#defaultNestedOpen").click();
  }
  element.autocomplete = isGoogleChrome() ? 'disabled' : 'off';
});

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
}

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

$(document).on('input', '#id_no_of_pages', function(){
  var pages = $("#id_no_of_pages").val();
  if (pages > 0){
      var no_of_pages = pages * 275;
      $('#words').html(no_of_pages);
  }else {
      $("#id_no_of_pages").val(1);
  }
})


function getCitation(evt, citation){
  var citationInput = $("#id_citation");
  citationInput.attr('type', 'hidden');
  var citationLinks;

  citationLinks = $(".citation");
  for (i = 0; i < citationLinks.length; i++) {
    citationLinks[i].className = citationLinks[i].className.replace(" active", "");
  }

  var currentCitation = $(`#${citation}`);
  currentCitation.addClass('active');
  citationInput.val(currentCitation.html())
}

$("#other-citation").on('click', function(){
  citationLinks = $(".citation");
  for (i = 0; i < citationLinks.length; i++) {
    citationLinks[i].className = citationLinks[i].className.replace(" active", "");
  }
  $("#other-citation").addClass("active");
  var citationInput = $("#id_citation");
  citationInput.val("");
  citationInput.attr('placeholder', 'Enter the format or citation style');
  citationInput.attr('type', 'text');
});

$("#or-words").on('click', function( ){
  var wordsInput = $("#id_words");
  wordsInput.attr('type', (_, attr) => attr == "hidden" ? "text" : "hidden");
  var pagesInput = $("#id_no_of_pages");
  pagesInput.attr('type', (_, attr) => attr == "hidden" ? "number" : "hidden");
  var wordsContainer = $("#words-container");
  wordsContainer.toggleClass("hidden");
  $("#or-words").html() === "or words" ? $("#or-words").html("or pages") : $("#or-words").html("or words");
})

$("#id_due_date").on('change', function(){
  $("#id_due_time").val(0);
  var dateInput = $(this).val();
  const expiration = moment(dateInput);
  checkDateAndDisplayTimeLeft(expiration);
});

function checkDateAndDisplayTimeLeft(expiration){
  const now = moment();
  var isCurrentDate = expiration.isSame(new Date(), "day");
  if(isCurrentDate) {
    let diff = moment(now).endOf('day') - now;
    let diffDuration = moment.duration(diff);
    displayTimeLeft(diffDuration);
  }else {
    const diff = expiration.diff(now);
    const diffDuration = moment.duration(diff);
    displayTimeLeft(diffDuration);
  }
}

$("#id_due_time").on('change', function(){
  var dateInput = $("#id_due_date").val();
  var timeInput = $("#id_due_time").val();
  if (dateInput) {
    var isCurrentDate = moment(dateInput).isSame(new Date(), "day");
    if(isCurrentDate) {
      handleTimeDisplayForToday(timeInput);
    }else {
      const expiration = moment(dateInput).add(timeInput, 'hours');
      checkDateAndDisplayTimeLeft(expiration);
    }
  }else{
    handleTimeDisplayForToday(timeInput);
  }
});

function handleTimeDisplayForToday(timeInput){
  var now = moment();
  now = now.set({hour:0,minute:0,second:0,millisecond:0});
  var timeLeftToday = now.add(timeInput, 'hours');
  now = moment();
  const diff = timeLeftToday.diff(now);
  if (diff > 0){
    const diffDuration = moment.duration(diff);
    displayTimeLeft(diffDuration);
  }else {
    var timeLeft = `${0}h ${0}m left`;
    $('#time-left').html(timeLeft);
    $("#time-left").addClass('warning');
    $("#time-left").removeClass('bluish-bgc');
  }
}

function displayTimeLeft(diffDuration){
  if (diffDuration.days() <= 0){
    var timeLeft = `${diffDuration.hours()}h ${diffDuration.minutes()}m left`;
    $('#time-left').html(timeLeft);
    $("#time-left").addClass('warning');
    $("#time-left").removeClass('bluish-bgc');
  }else {
    var timeLeft = `${diffDuration.days()}d ${diffDuration.hours()}h ${diffDuration.minutes()}m left`;
    $('#time-left').html(timeLeft);
    $("#time-left").addClass('bluish-bgc');
    $("#time-left").removeClass('warning');
  }
}