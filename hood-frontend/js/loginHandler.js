let loginHandler = (e) => {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let message = document.getElementById('messagesinfo');
    let form = document.getElementById('loginform');

    axios.post('https://hood-drf.herokuapp.com/api/v1/login/', {
        username: username,
        password: password,
    })
    .then((res) => {
        const refresh_token = res.data.refresh;
        const access_token = res.data.access;

        localStorage.setItem('username', username)
        localStorage.setItem('access_token', JSON.stringify(access_token));
        localStorage.setItem('refresh_token', JSON.stringify(refresh_token));
        form.reset();
        message.style.display = 'block'
        message.innerHTML = 'Successfully logged in!';
        window.location.href = '../index.html';
    })
    .catch((err) => {
        form.reset();
        message.style.display = 'block'
        message.innerHTML = 'Username or password was incorrect! Try Again!';
    });
    e.preventDefault();
}

document.getElementById('loginform').addEventListener('submit', loginHandler);