document.getElementById('notifications').addEventListener('click', function () {

    ///// Notifications Bar

    // открываем бар
    const extraBar = document.getElementById('extra-bar');
    extraBar.classList.toggle('active');

    const imgHeart = document.getElementById('img-heart');
    const blackHeartSrc = imgHeart.dataset.blackHeart;
    const simpleHeartSrc = imgHeart.dataset.simpleHeart;

    extraBar.classList.contains('active')
        ? imgHeart.src = blackHeartSrc
        : imgHeart.src = simpleHeartSrc;

    //
    // если search bold поменять
    const imgSearch = document.getElementById('img-search')
    const boldSearchSrc = imgSearch.dataset.boldSearch;
    const simpleSearchSrc = imgSearch.dataset.simpleSearch;

    imgSearch.src.includes(boldSearchSrc) ? imgSearch.src = simpleSearchSrc : imgSearch.src;
    // 

    document.getElementById('main-sidebar').classList.toggle('add-extra-bar');
    console.log('КЛИК');

    // document.getElementById('extra-container').innerHTML = '';
    const extraContainer = document.getElementById('extra-container');

    extraContainer.innerHTML = `
    <h2>Notifications</h2>
    <img id="load-gif" style="height: 2rem; width: 2rem; display: block; align-self: center;     margin-right: 60px;" 
    src="/static/generalApp/icons/loading.gif"></img>

    <div class="notifications-results" id="notifications-results">
        
    </div>`;

    const loadGIF = document.getElementById('load-gif')
    // loadGIF.style.display = "block";


    const likePng = extraContainer.dataset.like;

    const notifDiv = document.getElementById('notifications-results');

    function renderFollowNotification(event) {
        notifDiv.innerHTML +=
            ` <div class="notification-profile" data-post_id="${event.post_id}">
                <img src="${event.avatar_url}" class="n-avatar" ">

                <div class="n-text">
                    <p><b>${event.user}</b> ${event.message}</p> 
                </div>
                

            </div> `;
    }

    function renderLikeNotification(event) {
        notifDiv.innerHTML +=
            ` <div class="notification-profile">
                <img src="${event.avatar_url}" class="n-avatar" ">

                <div class="n-text">
                    <p><b>${event.user}</b> ${event.message}</p> 
                </div>

                <div class="n-preview">
                    <img src="${event.thumbnail_url}" class="image">
                    <img src="${likePng}" class="on-img">
                </div>
            </div> `;
    }

    function renderCommentNotification(event) {
        notifDiv.innerHTML +=
            ` <div class="notification-profile" data-post_id="${event.post_id}">
                <img src="${event.avatar_url}" class="n-avatar" ">

                <div class="n-text">
                    <p><b>${event.user}</b> ${event.message}</p> 
                </div>
            
                <div class="n-preview">
                    <img src="${event.thumbnail_url}" class="image">
                </div>
            </div> `;
    }


    fetch('http://127.0.0.1:8000/api/notifications/')
        .then(response => response.json())
        // document.getElementById('extra-container').innerHTML = `<h2>Notifications</h2>`
        .then(data => {
            notifDiv.innerHTML = '';
            console.log(data);
            // // likesArray = data.likes_event.reverse()
            // // самые новые
            data.events.forEach(event => {

                if (event.type === 'follow') {
                    renderFollowNotification(event)
                } else if (event.type === 'like') {
                    renderLikeNotification(event)
                } else if (event.type === 'comment') {
                    renderCommentNotification(event)
                }

            });
            loadGIF.style.display = "none";

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
