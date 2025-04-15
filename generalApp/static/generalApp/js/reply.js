document.body.addEventListener('click', function (event) {
    if (event.target.classList.contains('reply')) {
        console.log('REPLY');
        
        const commentInput = document.getElementById('comment-input');
        commentInput.focus(); // Установить фокус на input

        const bebra_id = event.target.dataset.username

        commentInput.value = `${bebra_id}, `;
    }
})