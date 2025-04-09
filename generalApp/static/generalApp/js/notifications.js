document.getElementById('notifications').addEventListener('click', function () {

    const extraBar = document.getElementById('extra-bar');


    const blackHeartSrc = document.getElementById('img-heart').dataset.blackHeart;
    const simpleHeartSrc = document.getElementById('img-heart').dataset.simpleHeart;


    // открываем бар
    extraBar.classList.toggle('active');

    if (extraBar.classList.contains('active')) {
        document.getElementById('img-heart').src = blackHeartSrc;
    } else {
        document.getElementById('img-heart').src = simpleHeartSrc;
    }

    document.getElementById('main-sidebar').classList.toggle('add-extra-bar');
    console.log('КЛИК');

    // document.getElementById('extra-container').innerHTML = '';
    const extraContainer = document.getElementById('extra-container');

    extraContainer.innerHTML = `
    <h2>Notifications</h2>
    <div class="notifications-results" id="notifications-results">
        
    </div>`;

    const likePng = extraContainer.dataset.like;

    const notifDiv = document.getElementById('notifications-results');
    fetch('http://127.0.0.1:8000/api/notifications/')
        .then(response => response.json())
        // document.getElementById('extra-container').innerHTML = `<h2>Notifications</h2>`
        .then(data => {
            notifDiv.innerHTML = '';
            console.log(data);
            likesArray = data.likes_event.reverse() // самые новые
            likesArray.forEach(element => {
                notifDiv.innerHTML +=
                    `
                    <div class="notification-profile" data-post_id="${element.id_post}">
                        <img src="${element.user_avatar_url}" class="n-avatar" ">

                        <div class="n-text">
                            <p><b>${element.username}</b> liked your post. </p> 
                        </div>


                        <div class="n-preview">
                            <img src="${element.thumbnail_url}" class="image">
                            <img src="${likePng}" class="on-img">

                        </div>
                    
                    </div> `;
            });

        });

    notifDiv.addEventListener('click', function (e) {

        const targetPostID = e.target.closest('.notification-profile');
        // closest - вверх по DOM находит элем '.___'

        const PostId = targetPostID.dataset.post_id;
        // dataset предоставляет доступ к кастомным data-* атрибутам элемента
        //Для элемента <div class="search-profile" data-username="alice"> значение userDiv.dataset.username будет "alice".

        window.location.href = `/post/${PostId}/`; // Совпадает с вашим Django URL
    });




});
