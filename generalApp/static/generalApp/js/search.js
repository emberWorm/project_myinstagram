alert("Ура победа")
document.addEventListener('DOMContentLoaded', function() { // пока документ загрузится

    const searchInput = document.getElementById('live-search');

    const resultsContainer = document.getElementById('search-results');

    let debounceTimer;

    searchInput.addEventListener('input', function(e) {
        
        clearTimeout(debounceTimer);
        const query = e.target.value.trim();
        
        // Не ищем если меньше 2 символов
        if (query.length < 2) {
            resultsContainer.innerHTML = '';
            return;
        }

        // Задержка 300 мс перед запросом
        debounceTimer = setTimeout(() => {
            fetch(`/api/search-users/?query=${encodeURIComponent(query)}`)
                .then(response => {
                    if (!response.ok) throw new Error('Network error');
                    return response.json();
                })
                .then(data => {
                    resultsContainer.innerHTML = data.users.map(user => `
                        <div class="user-result">
                            <div class="username">${user.username}</div>
                            ${user.bio ? `<div class="bio">${user.bio}</div>` : ''}
                        </div>
                    `).join('');
                })
                .catch(error => {
                    console.error('Error:', error);
                    resultsContainer.innerHTML = '<div class="error">Ошибка загрузки</div>';
                });
        }, 300);
    });
});