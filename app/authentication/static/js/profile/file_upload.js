let dropArea = document.getElementById('drop-area');
let droppableArea = document.getElementById('droppable-area');
let filesDone = 0;
let filesToDo = 0;
let progressBar = document.getElementById('progress-bar');

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
    files = [...files]
    initializeProgress(files.length);
    files.forEach(previewFile);
    files.forEach(uploadFile)
}

function uploadFile(file) {
  var url = '/order/material/';
  var CSRFToken = $('input[name=csrfmiddlewaretoken]').val();

  // var xhr = new XMLHttpRequest();
  // var formData = new FormData();
  // xhr.open('POST', url, true);

  // xhr.addEventListener('readystatechange', function(e) {
  //   if (xhr.readyState == 4 && xhr.status == 200) {
  //     console.log(data);
  //   }
  //   else if (xhr.readyState == 4 && xhr.status != 200) {
  //     // Error. Inform the user
  //   }
  // });

  // formData.append('material', file);
  // xhr.send(formData);




  const formData = new FormData();
  formData.append('material', file);

  const request = new Request(
    url,
      {
        headers: {
          'X-CSRFToken': CSRFToken,
          'X-Requested-With':'XMLHttpRequest',
          'Accept': 'application/json',
        }
      }
  );
  fetch(request, {
      method: 'POST',
      mode: 'same-origin',
      body: formData,
  })
  .then(response => response.json())
  .then(data => {
    progressDone();
    if (data) {
      console.log(data);
    }
  })
  .catch((error) => {
    console.log(error);
    error.forEach(renderError);
  });
}

function initializeProgress(numfiles) {
  progressBar.value = 0
  filesDone = 0
  filesToDo = numfiles
}

function progressDone() {
  filesDone++
  progressBar.value = filesDone / filesToDo * 100
}

function renderError (error){
  console.log(error);
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

