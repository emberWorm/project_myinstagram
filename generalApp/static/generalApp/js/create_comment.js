document.body.addEventListener('submit', function (event) {
    const myForm = document.getElementById('comment-form')
    if (event.target === myForm) {
        // Проверки или действия, которые должны выполняться при отправке формы
        event.preventDefault();
        console.log('отмена презагрузки');
        const dataForm = new FormData(myForm)
        console.log(dataForm);
        const formDataObj = Object.fromEntries(dataForm.entries());
        console.log(formDataObj);

        document.getElementById('comment-input').value = '';
        fetch('http://127.0.0.1:8000/api/create_comment/', {
            method: 'POST',
            body: dataForm // для бади всегда нужно указание метода
        })
        .then(otvetik => otvetik.json())
        .then(function udateCommentsPost(data) {
            console.log(data)
            document.getElementById('comments-section').innerHTML +=
        `<div class="modal-comment">
            <div>
                <img src="${data.insert_comment.avatar_url}" class="avatar" alt="Avatar">
            </div>
            <div class="comment-info">
                <span class="comment-username">${data.insert_comment.author}</span>
                ${data.insert_comment.body}
                <div style="color: #8e8e8e;">now Reply</div>
            </div>
        </div>`
        });


        // event.preventDefault(); // Если нужно предотвратить стандартное поведение формы
    }
})