// alert('js here');

// реализация ссылки не трогая макет страницы
document.querySelectorAll('.link-button, .profile-pic, .obj-click').forEach(function(button) {

    button.addEventListener('click', 
        function() {
        window.location.href = this.getAttribute('data-url');
    });
});

document.getElementById('more').addEventListener('click', function(){
    document.getElementById('logout-btn').classList.toggle('open');
});



// про create
// Получить элементы
const fileInput = document.getElementById('image-input');
const uploadButton = document.getElementById('upload-button');

// Симулировать клик на кнопке ""
uploadButton.addEventListener('click', function() {
    fileInput.click();
});

fileInput.addEventListener('change', function() {
    if (this.files.length > 0) {
        uploadButton.textContent = 'File load';
        uploadButton.classList.add('load');
    } else {
        uploadButton.textContent = 'Select photo';
    }
});