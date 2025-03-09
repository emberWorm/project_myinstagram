// alert('js here');

// реализация ссылки не трогая макет страницы
document.querySelectorAll('.link-button').forEach(function(button) {

    button.addEventListener('click', 
        function() {
        window.location.href = this.getAttribute('data-url');
    });
});
