document.addEventListener('click', function (event) {
    if (event.target.classList.contains('img-like')) {
        console.log('клик лайк');
        const icon = event.target;
        // const iconNowSrc = icon.src;
        const likedSrc = icon.dataset.likedSrc;
        const unlikedSrc = icon.dataset.unlikedSrc;

        const likesCounter = icon.closest('.post, .modal-post-content').querySelector('.likes-count');

        // Меняем src иконки
        if (icon.src.endsWith(likedSrc)) {
            icon.src = unlikedSrc;
        } else {
            icon.src = likedSrc;
        }

        const postID = event.target.dataset.postId

        async function postLike() {
            const response = await fetch(`http://127.0.0.1:8000/post_like/${postID}/`)

            console.log(response)

            if (response.ok) {
                const data = await response.json();
                console.log("ВЫПОЛНЕН")
                console.log(data.likes)
                likesCounter.textContent = data.likes + 350;

            } else {
                console.log('НЕ ВЫПОЛНЕН')
            }
        }
        
        postLike()
    }

})