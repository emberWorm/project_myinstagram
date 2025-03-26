document.querySelectorAll('.open_post_link').forEach(link => {

    link.addEventListener('click', async (e) => {
        e.preventDefault(); // отменить стандартный переход

        const postId = link.dataset.postId;

        // ждем ответа
        const response = await fetch(`/post/${postId}/`);
        // ждем преобразования в текст
        const response_content = await response.text(); 

        const modelContent = document.getElementById('modal-content');
        modelContent.innerHTML = response_content;

        // чтобы показывалась url поста
        history.pushState({ postId }, '', `/post/${postId}/`);
    });
    
});