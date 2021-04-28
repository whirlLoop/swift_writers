let dropArea = document.getElementById('drop-area');
let droppableArea = document.getElementById('droppable-area');
['dragenter', 'dragover', 'dragleave', 'drop', 'drag', 'dragstart', 'dragend'].forEach(eventName => {
  droppableArea.addEventListener(eventName, preventDefaults, false)
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
    let fileInput = document.getElementById('fileElem');
    fileInput.files = files;
    ([...files]).forEach(previewFile);
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

