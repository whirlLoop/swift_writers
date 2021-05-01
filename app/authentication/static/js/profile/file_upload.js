let dropArea = document.getElementById('drop-area');
let droppableArea = document.getElementById('droppable-area');
let uploadProgress = [];
let progressBar = document.getElementById('progress-bar');
let filesLength;

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
    let fileInput = document.getElementById('fileElem');
    fileInput.files = files;
    files = [...files];
    initializeProgress(files.length);
    files.forEach(previewFile);
    files.forEach(uploadFile)
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
    fileSpan.attr('id', file.name);
    let fileNameSpan = $('<span/>');
    fileNameSpan.addClass('file-name-span');
    var fileNameString = `${'<i class="fas fa-file"></i>'} ${file.name}`;
    fileNameSpan.append(fileNameString);
    fileSpan.append(fileNameSpan);
    var trashIcon = '<i class="fas fa-trash" onclick="deleteFileByIndex(event)"></i>';
    fileSpan.append(trashIcon);
    let gallery = $('#gallery');
    gallery.append(fileSpan);
}

function deleteFileByIndex(event){
  var parent = event.target.parentNode.id;
  console.log(parent);
  var file = globalFiles.item(q)
}

