document.querySelectorAll('.open_post_link').forEach(link => {

    link.addEventListener('click', async (e) => {
        e.preventDefault(); // отменить стандартный переход

        const postId = link.dataset.postId;

        // чтобы показывалась url поста
        history.pushState({ postId }, '', `/post/${postId}/`);

        // ждем ответа
        const response = await fetch(`/post/${postId}/`, {
            headers: {
                // 'X-Requested-With': 'XMLHttpRequest', // историческое наследие
                // X - исторический префикс для эксперим. (своих заголовков)
                'X-Request-With': 'Fetch',
            }
        });
        // ждем преобразования в текст
        const response_content = await response.text();

        // обновляем модалку
        const modalContent = document.getElementById('base-modal-post-content');
        modalContent.innerHTML = response_content


        // Получаем данные из data-атрибутов
        const postAuthorId = modalContent.querySelector('.modal-post-content').dataset.authorId;
        const currentUserId = modalContent.querySelector('.modal-post-content').dataset.userId;

        // открыть модалку More
        const moreModal = document.getElementById("moreModal");
        const btnMore = document.getElementById("open_more_post_link");

        btnMore.onclick = function () {
            moreModal.style.display = "block";
            console.log("ТЫ НАЖАЛ НА МОРЕ")
        };

        const baseModalMmoreContent = document.getElementById("base-modal-more-content");

        baseModalMmoreContent.innerHTML =
            // <div class="base-modal-more-content" id="base-modal-more-content">
            `
                ${currentUserId === postAuthorId ?
                '<button class="more-option delete-post" id="btn-delete-post">Удалить пост</button>' :
                '<button class="more-option report-post">Пожаловаться</button>'}
                <button class="more-option cancel-more">Отмена</button>
        `;

        // const modalMoreContent = document.getElementById("base-modal-more-content");
        const modalMoreContentDel = document.getElementById("base-modal-more-content-delete");
        const btnDelPost = document.getElementById("btn-delete-post");

        // *удалить пост*
        btnDelPost.onclick = function () {
            baseModalMmoreContent.style.display = "none";
            modalMoreContentDel.style.display = "block";
        }

        // отмена удаления
        const btnCancelDelete = document.getElementById("cancel-detele");
        btnCancelDelete.onclick = function () {
            modalMoreContentDel.style.display = "none";
            baseModalMmoreContent.style.display = "block";
        }

        // подтверждение удаления 
        const btnConfirmDelete = document.getElementById("confirm-delete");

        btnConfirmDelete.onclick = async function handleDeletePost() {
            console.log(postId)

            const response = await fetch(`/post/${postId}/delete/`)

            if (response.ok) {
                // Если запрос успешен, перенаправляем пользователя
                window.location.href = "/";  // Перенаправление на главную страницу
            }


            console.log(response);
        }
        // const response = await fetch(`/post/${postId}/delete/`);
        // //  {
        // //     method: 'DELETE',
        // //     headers: {
        // //         'X-CSRFToken': getCsrfToken(),
        // //         'Content-Type': 'application/json'
        // //     }
        // // });
        // console.log(response);





        // history.pushState(state, title, url);

        // pushState() для реализации SPA (Single Page Applications), 
        // динамически изменять URL и управлять состоянием приложения без полной перезагрузки страниц.
        // const moreModal = document.getElementById("moreModal");



        // request.user.id === post.author.id ?
        // '<button class="more-option delete-post" id="btn-delete-post">Удалить пост</button>':
        // '<button class="more-option report-post">Пожаловаться</button>'}

        //    `<div class="more-modal-content">
        //         ${request.user.id === post.author.id ?
        //             '<button class="more-option delete-post">Удалить пост</button>' :
        //             '<button class="more-option report-post">Пожаловаться</button>'}
        //         <button class="more-option cancel-more">Отмена</button>
        //     </div>
        //             `;

        // btnMore.addEventListener('click', function(e) {
        //     e.stopPropagation();

        //     // Создаем модалку More
        //     const moreModal = document.createElement('div');
        //     moreModal.className = 'more-modal';
        //     moreModal.innerHTML = `
        //         <div class="more-modal-content">
        //             ${request.user.id === post.author.id ? 
        //                 '<button class="more-option delete-post">Удалить пост</button>' : 
        //                 '<button class="more-option report-post">Пожаловаться</button>'}
        //             <button class="more-option cancel-more">Отмена</button>
        //         </div>
        //     `;

        document.getElementById('url-pic').addEventListener('click', function (event) {
            console.log('переходик');
            
            window.location.href = event.target.dataset.url;
        })


    });


});