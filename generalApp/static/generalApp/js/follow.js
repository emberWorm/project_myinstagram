document.body.addEventListener('click', function name(event) {
    if (event.target.id === 'btn-follow') {
        const button = document.getElementById('btn-follow');
        const userId = event.target.dataset.userId
        const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        fetch('http://127.0.0.1:8000/api/make_follow/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'user_id': userId })
            // JSON.stringify(): Преобразует объект JavaScript в строку JSON.
            // JSON.parse(): Преобразует строку JSON в объект JavaScript. (синхпронный) json()- для fetch
        })
            .then(jsonResponse => jsonResponse.json())
            .then(parsedJson => {
                console.log(parsedJson);
                console.log(parsedJson.Follow);
                if (parsedJson.Follow === "True") {
                    button.innerText = "Unfollow";
                    button.style.backgroundColor = "rgba(244, 155, 250, 0.98)";
                    button.style.border = "2px solid #9a77f9";
                } else {
                    button.innerText = "Follow";
                    button.style.backgroundColor = "#3897f0";
                    button.style.border = "1px solid #3897f0";

                }
            })
    }


});