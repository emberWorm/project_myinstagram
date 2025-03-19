// alert('js here');

// реализация ссылки не трогая макет страницы
document.querySelectorAll('.link-button, .profile-pic, .obj-click').forEach(function (button) {

    button.addEventListener('click',
        function () {
            window.location.href = this.getAttribute('data-url');
        });
});

document.getElementById('more').addEventListener('click', function () {
    document.getElementById('logout-btn').classList.toggle('open');
});

// пришлось перенести выше
document.getElementById('search').addEventListener('click', function () {

    document.getElementById('extra-bar').classList.toggle('active');
    document.getElementById('main-sidebar').classList.toggle('add-extra-bar');
    console.log('КЛИК');

});


// КНОПКА ЗАГРУЗКИ ИЗОБРАЖЕНИЯ
// Получить элементы

const fileInput = document.getElementById('image-input');
const uploadButton = document.getElementById('upload-button');

// Симулировать клик на кнопке ""
uploadButton.addEventListener('click', function () {
    fileInput.click();
});

fileInput.addEventListener('change', function () {
    if (this.files.length > 0) {
        uploadButton.textContent = 'File load';
        uploadButton.classList.add('load');
    } else {
        uploadButton.textContent = 'Select photo';
    }
})

// 
// Чтобы area удлинялась
// function autoGrow(element) {
//     element.style.height = '5px';
//     element.style.height = element.scrollHeight + 'px';
// }

// document.getElementById('bio-area').addEventListener('input', function() {
//     autoGrow(this);
// });

document.getElementById('bio-area').addEventListener('input', function () {
    const maxLength = this.getAttribute('maxlength');
    const currentLength = this.value.length;
    const remaining = maxLength - currentLength;

    // ))
    document.getElementById('p-count').style.opacity = 1;


    document.getElementById('remaining').innerText = remaining;
});

document.getElementById('bio-area').addEventListener('blur', function () {
    document.getElementById('p-count').style.opacity = 0;
});


