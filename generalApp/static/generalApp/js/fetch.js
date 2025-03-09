const get_interval = 5; // seconds

let path_to = ''

function create_info(info) {
    let p = document.createElement('p');
    // запихать в него текст
    p.textContent = 'lat: ' + info.lat; // lat:37

    document.body.appendChild(p);
}


function get_check_post(){

    fetch(path_to);
    
    console.log(`О, прошло ${get_interval} секунд надо обновить страницу`);
    let post_data = {'lat':37};
    console.log('В коде есть заглушка');
    create_info(post_data);

}


function Do_all() {
    // alert('Тут страничка готова');
    console.log('Привет');
    get_check_post();
    setTimeout(Do_all, get_interval + 1000);
}

window.addEventListener(
    'load',
    Do_all
)