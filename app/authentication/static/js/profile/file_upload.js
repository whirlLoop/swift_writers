let dropArea = document.getElementById('drop-area');
let droppableArea = document.getElementById('droppable-area');
let uploadProgress = [];
let progressBar = document.getElementById('progress-bar');
let filesLength;
let gallery = $('#gallery');
let materialsList = new Array();

['dragenter', 'dragover', 'dragleave', 'drop', 'drag', 'dragstart', 'dragend'].forEach(eventName => {
  droppableArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults (e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    // dropArea.addEventListener(eventName, highlight, false);
    droppableArea.addEventListener(eventName, highlight, false);
  });

['dragleave', 'drop'].forEach(eventName => {
    droppableArea.addEventListener(eventName, highlight, false);
    // dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight(e) {
    dropArea.classList.add('highlight');
}

function unhighlight(e) {
    dropArea.classList.remove('highlight');
}

// dropArea.addEventListener('drop', handleDrop, false);
droppableArea.addEventListener('drop', handleDrop, false);

var globalFiles;
function handleDrop(e) {
  let dt = e.dataTransfer;
  let files = dt.files;

  handleFiles(files);
  globalFiles = files;
}

function handleFiles(files) {
    progressBar.style.display = "block";
    files = [...files];
    initializeProgress(files.length);
    files.forEach(uploadFile);
}

function uploadFile(file, i) {
  var url = '/order/material/';
  var CSRFToken = $('input[name=csrfmiddlewaretoken]').val();

  var xhr = new XMLHttpRequest();
  var formData = new FormData();
  xhr.open('POST', url, true);
  xhr.setRequestHeader('X-CSRFToken', CSRFToken);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhr.setRequestHeader('Accept', 'application/json');

  xhr.upload.addEventListener("progress", function(e) {
    updateProgress(i, (e.loaded * 100.0 / e.total) || 100);
  });

  xhr.addEventListener('readystatechange', function(e) {
    if (xhr.readyState == 4 && xhr.status == 201) {
      console.log("file upload success");
      var file = JSON.parse(xhr.response);
      previewFile(file);
      materialsList.push(file.pk);
    }
    else if (xhr.readyState == 4 && xhr.status != 200) {
      var errors = JSON.parse(xhr.response);
      Object.values(errors).forEach(val => {
        renderError(val);
      });
    }
  });

  formData.append('material', file);
  xhr.send(formData);

}

function initializeProgress(numFiles) {
  progressBar.value = 0;
  uploadProgress = [];

  for(let i = numFiles; i > 0; i--) {
    uploadProgress.push(0);
  }
}

function updateProgress(fileNumber, percent) {
  uploadProgress[fileNumber] = percent;
  let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length;
  progressBar.value = total;
}


function renderError (error){
  let errorList = $("#image-error-list");
  var errorLi = $("<li/>");
  errorLi.append(error);
  errorList.append(errorLi);

}

function previewFile(file){
    let fileSpan = $('<span/>');
    fileSpan.addClass('file-span');
    fileSpan.attr('id', file.pk);
    let fileNameSpan = $('<span/>');
    fileNameSpan.addClass('file-name-span');
    var fileNameString = `${'<i class="fas fa-file"></i>'} ${file.filename}`;
    fileNameSpan.append(fileNameString);
    fileSpan.append(fileNameSpan);
    var trashIcon = $('<i class="fas fa-trash" onclick="deleteFileByIndex(event)"></i>');
    trashIcon.attr('id', file.pk);
    fileSpan.append(trashIcon);
    gallery.append(fileSpan);
}

function deleteFileByIndex(event){
  var itemId = event.target.id;
  var url = '/order/material/temp/';
  url = url + itemId;
  var CSRFToken = $('input[name=csrfmiddlewaretoken]').val();

  var xhr = new XMLHttpRequest();
  xhr.open('POST', url, true);
  xhr.setRequestHeader('X-CSRFToken', CSRFToken);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhr.setRequestHeader('Accept', 'application/json');

  xhr.addEventListener('readystatechange', function(e) {
    if (xhr.readyState == 4 && xhr.status == 204) {
      var $itemSelector = ".file-span#" + itemId;
      var item = $($itemSelector);
      removeItem(item);
      removeItemFromMaterialList(itemId);
      // console.log(itemId)
    }
    else {
      var errors = xhr.status;
      console.error(errors)
    }
  });
  xhr.send();
}

function removeItem(item){
  item.remove();
  if ( gallery.children().length == 0 ) {
    $(".image-upload-row").empty();
  }
}

function removeItemFromMaterialList(itemId){
  console.log(itemId);
  const index = materialsList.indexOf(parseInt(itemId));
  // console.log(index);
  if (index > -1) {
   materialsList.splice(index, 1);
  }
}

function arrayRemove(value) {
  return materialsList.filter(function(ele){
      return ele != value;
  });
}

$("#droppable-area").submit(e => {
  addFileToOrderMaterialsList();
});

function addFileToOrderMaterialsList(){
  $("#id_materials").val(materialsList);
}