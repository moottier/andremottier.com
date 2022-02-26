window.onload=function(){
    const inputElement = document.getElementById("resize-file");
    inputElement.addEventListener("change", handleFiles, false);
    init();
}

function init() {
    setPictureSourceInit();
}

function validateInput(fileList) {
    return true;
}

function handleInvalidFile() { 
    setPictureSourceInit();    
}

function setPictureSource(el, src) {
    el.querySelector('source').srcset = src;
    el.querySelector('img').src = src;
}

function setPictureSourceInit() {
    src = "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=";
    preview = document.getElementById("resize-file-preview");
    setPictureSource(preview, src);
}

function handleFiles(e) {
    console.log(e);  // DBG
    let files = e.srcElement.files;
    if (validateInput(files)) {
        const file = files[0];
        console.log(file.type);  // DBG
        if (!file.type.startsWith('image/')){ handleInvalidFile(); }
        
        const preview = document.getElementById("resize-file-preview");
        
        const reader = new FileReader();
        reader.onload = (function(aPreview) { return function(e) { setPictureSource(aPreview, e.target.result); }; })(preview);
        reader.readAsDataURL(file);

    } else {
        handleInvalidFile();
    }
  }