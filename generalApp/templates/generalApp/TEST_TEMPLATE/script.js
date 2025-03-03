// document.getElementById('link').addEventListener('click', 
//     function() {

//     const icon = document.getElementById('icon');

//     if (icon.src.includes('home_white.png')) {
//         icon.src = 'home_black.png';
//     } else {
//         icon.src = 'home_white.png';
//     }

//     const text = document.getElementById('text');
//     if (text.classList.contains('bold')) {
//         text.classList.remove('bold');
//     } else {
//         text.classList.add('bold');
//     }
// });

// // JavaScript
// document.getElementById('iconButton').addEventListener('click', function() {
//     const icon = document.getElementById('icon');
//     if (icon.src.includes('home.png')) {
//         icon.src = 'heart.png';
//         localStorage.setItem('icon', 'heart.png');
//     } else {
//         icon.src = 'home.png';
//         localStorage.setItem('icon', 'home.png');
//     }
// });

// // При загрузке страницы
// window.onload = function() {
//     const storedIcon = localStorage.getItem('icon');
//     if (storedIcon) {
//         document.getElementById('icon').src = storedIcon;
//     }
// };

