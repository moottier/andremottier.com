window.onload=function(){
    const inputElement = document.getElementById("resize-file");
    const submitElement = document.getElementById("resize-file-submit");
    const targetUrl = "";
    inputElement.addEventListener("change", handleSelectedFiles, false);
    submitElement.addEventListener("click", handleFormSubmit, false);
    submitElement.addEventListener("touchend", handleFormSubmit, false);
    init();
}

function init() {
    setPictureSourceInit();
    setFileName('null');
}

function validateSelectedFile(fileList) {
    if (!file.type.startsWith('image/')){ return false; }
    if !(0 < file.size < 5000000) { return false; }
    return true;
}

function validateForm(fd) {
    const width = fd.get('width');
    const height = fd.get('height')
    const file = fd.get('file');
    if !(width && height && file) { return false; }
    if (!isNaN(width) && !isNaN(height)) { return false; }

    files = document.getElementById('resize-file').files;
    if (!validateSelectedFile(files)) { return false; }    
    return true;
}

function handleInvalidFileSelection() { 
    setPictureSourceInit();
    showStatus();
    setFileName('null');
}

function handleInvalidForm() { 
    setPictureSourceInit();
    showStatus();
    setFileName('null');
}

function showStatus() {
    // do nothing
}

function setFileName(name) {
    // do nothing
}

function setPictureSource(el, src) {
    el.querySelector('source').srcset = src;
    el.querySelector('img').src = src;
}

function setPictureSourceInit() {
    src = "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=";    // minimal gif
    preview = document.getElementById("resize-file-preview");
    setPictureSource(preview, src);
}

function handleSelectedFiles(e) {
    
    console.log(e);  // DBG
    
    let files = e.srcElement.files;
    if (validateSelectedFile(files)) {
        const file = files[0];
        
        console.log(file.type);  // DBG

        const preview = document.getElementById("resize-file-preview");
        
        const reader = new FileReader();
        reader.onload = (function(aPreview) { return function(e) { 
            setPictureSource(aPreview, e.target.result); 
            setFileName('null');
        }; })(preview);
        reader.readAsDataURL(file);

    } else {
        handleInvalidFileSelection();
    }
  }

function getResponseFileDownloadName(contentDispositionHeader) {
    let cdh = contentDispositionHeader;
    return cdh.substr(cdh.indexOf("filename=")+"filename=".length);
}

function handleFormSubmitResponse(e) {
    console.log(e);//.srcElement.responseText);
    if (e.srcElement.status == 200) {
        URL = window.URL;
        url = URL.createObjectURL(this.response);
        console.log(this.response);
        //console.log(this.response.blob());
        
        const link = document.getElementById("resize-file-download");
        link.href = url;
        console.log(url);
        link.download = getResponseFileDownloadName(this.getResponseHeader('Content-Disposition'));
        console.log(link.download);    // can get filename from here
    } else {
        showStatus();
    }
}

function handleFormSubmit(e) {
    e.preventDefault();
    let fd = new FormData(e.srcElement.form);
    if (validateForm(fd)) {
        let xhr = new XMLHttpRequest();
        xhr.responseType = 'blob';
        console.log(fd.get('file'));

        xhr.onloadend = handleFormSubmitResponse;
        xhr.open("POST", e.srcElement.form.target);
        xhr.send(fd);
    } else {
        console.log("Inalid!");   // dgb
        handleInvalidForm();
    }
}