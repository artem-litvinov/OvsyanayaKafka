var form = document.querySelector('form');
var status_text = document.querySelector('#status_text');

function showStatus(xhr) {
    status_text.classList.add(xhr.status === 200? 'success': 'error');
    status_text.innerHTML = xhr.status + ': ' + xhr.statusText;
    status_text.style.display = 'block';
    dismiss();
}

function dismiss() {
    setTimeout(function(){
        status_text.classList.remove('error');
        status_text.classList.remove('success');
        status_text.style.display = 'none';
    }, 5000);
}

function makeFormData(obj) {
    var fd = new FormData();
    Object.keys(obj).map(key => fd.append(key, obj[key]));
    return fd;
}

function request(type, url, ctype, data, cb) {
    var xhr = new XMLHttpRequest();
    xhr.open(type, url, true);
    switch (ctype) {
        case 'application/json':
            xhr.setRequestHeader('Content-type', ctype);
            xhr.send(JSON.stringify(data));
            break;
        case 'multipart/form-data':
            xhr.send(makeFormData(data));
            break;
        case 'application/x-www-form-urlencoded':
            xhr.setRequestHeader('Content-type', ctype);
            xhr.send(makeFormData(data));
            break;
        default:
            xhr.send(data);
            break;
    }
    xhr.onreadystatechange = function() {
        if (xhr.readyState != 4) return;
        cb(xhr);
    };
}