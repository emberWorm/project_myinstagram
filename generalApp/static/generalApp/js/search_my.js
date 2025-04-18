document.getElementById('search').addEventListener('click', function () {

    ///// Search Bar

    // открываем бар
    const extraBar = document.getElementById('extra-bar');
    extraBar.classList.toggle('active');

    // меняем иконку search
    const imgSearch = document.getElementById('img-search')
    const boldSearchSrc = imgSearch.dataset.boldSearch;
    const simpleSearchSrc = imgSearch.dataset.simpleSearch;

    extraBar.classList.contains('active') 
    ? imgSearch.src = boldSearchSrc
    : imgSearch.src = simpleSearchSrc;

    ////////////////////// если icon notif black = change
    const imgHeart = document.getElementById('img-heart');
    const blackHeartSrc = imgHeart.dataset.blackHeart;
    const simpleHeartSrc = imgHeart.dataset.simpleHeart;

    imgHeart.src.includes(blackHeartSrc) ? imgHeart.src = simpleHeartSrc : imgHeart.src
    // ? console.log('СЕРДЦЕ ЧЕРНОЕ')
    // ? imgHeart.src = simpleHeartSrc
    // : console.log(`СЕРДЦЕ БЕЛОЕ${imgHeart.src}\n${blackHeartSrc}`)
    // : imgHeart.src = blackHeartSrc;
    ///////////////////////

    document.getElementById('main-sidebar').classList.toggle('add-extra-bar');
    console.log('КЛИК');
    document.getElementById('extra-container').innerHTML = `
    <h2>Search</h2>
    <div class="search-input-div">
            <input id="search-input" type="search" placeholder="Search">
    </div>
    <div class="search-results" id="search-results">
        
    </div>`;

    const inputSearch = document.getElementById('search-input');
    const divResultSearch = document.getElementById('search-results');

    inputSearch.addEventListener('input', function(e) {


        const query_input = e.target.value
        // const query = e.target.value.trim(); -удаляет пробелы сначала и с конца
        // e - объект события, e.target ссылается на элемент, который вызвал событие (input)

        console.log('Запрос отправлен');

        // сделать дебаунс
        fetch(`http://127.0.0.1:8000/api/search/?param=${query_input}`) // localhost:8000 - CORS?
        .then(response => response.json())
        // .then(data => console.log(data))
        .then(data => {
            let htmlContent = ''
            data.users.forEach(userInDiv => {
                htmlContent += `
            <div class="profile-flex search-profile" data-var_custom_name="${userInDiv.username}" style="margin:0;" >
    
                <div class="profile-rec" style="margin:10px;">
        
                    <img src="${userInDiv.avatar_url}" alt="Profile Picture" />
        
                    <div class="profile-rec-info">
        
                        <strong>${userInDiv.username}</strong>
        
                        <span class="profile-rec-info-name">${userInDiv.name}</span>
                    </div>
                </div>

            </div>`;

            });
            divResultSearch.innerHTML = htmlContent;
        });


        // .then(data => console.log(data.нормально));
    });
    


    divResultSearch.addEventListener('click', function(e) {

        const userDiv = e.target.closest('.search-profile');
        // closest - вверх по DOM находит элем '.asdasdsa'

        const username = userDiv.dataset.var_custom_name; 
        // dataset предоставляет доступ к кастомным data-* атрибутам элемента
        //Для элемента <div class="search-profile" data-username="alice"> значение userDiv.dataset.username будет "alice".

        window.location.href = `/usr/${username}/`; // Совпадает с вашим Django URL
    });


});





// document.addEventListener('DOMContentLoaded', function() {
//     // const extraBarContent = document.getElementById('');

//     const inputSearch = document.getElementById('search-input');
//     const divResultSearch = document.getElementById('search-results');

//     inputSearch.addEventListener('input', function(e) {


//         const query_input = e.target.value
//         // const query = e.target.value.trim(); -удаляет пробелы сначала и с конца
//         // e - объект события, e.target ссылается на элемент, который вызвал событие (input)

//         console.log('Запрос отправлен');

//         // сделать дебаунс
//         fetch(`http://127.0.0.1:8000/api/1/?param=${query_input}`) // localhost:8000 - CORS?
//         .then(response => response.json())
//         // .then(data => console.log(data))
//         .then(data => {
//             let htmlContent = ''
//             data.users.forEach(userInDiv => {
//                 htmlContent += `
//             <div class="profile-flex search-profile" data-var_custom_name="${userInDiv.username}" style="margin:0;" >
    
//                 <div class="profile-rec" style="margin:10px;">
        
//                     <img src="${userInDiv.avatar_url}" alt="Profile Picture" />
        
//                     <div class="profile-rec-info">
        
//                         <strong>${userInDiv.username}</strong>
        
//                         <span class="profile-rec-info-name">${userInDiv.name}</span>
//                     </div>
//                 </div>

//             </div>`;

//             });
//             divResultSearch.innerHTML = htmlContent;
//         });


//         // .then(data => console.log(data.нормально));
//     });
    


//     divResultSearch.addEventListener('click', function(e) {

//         const userDiv = e.target.closest('.search-profile');
//         // closest - вверх по DOM находит элем '.asdasdsa'

//         const username = userDiv.dataset.var_custom_name; 
//         // dataset предоставляет доступ к кастомным data-* атрибутам элемента
//         //Для элемента <div class="search-profile" data-username="alice"> значение userDiv.dataset.username будет "alice".

//         window.location.href = `/usr/${username}/`; // Совпадает с вашим Django URL
//     });

// });