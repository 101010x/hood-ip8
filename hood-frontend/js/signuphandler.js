let signUpHandler = (e) => {
    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let message = document.getElementById('messagesinfo');
    let form = document.getElementById('signupform');

    axios.post('https://hood-drf.herokuapp.com/api/v1/register/', {
        username: username,
        email: email,
        password: password,
    })
    .then((res) => {
        form.reset();
        message.style.display = 'Successfully Signed up';
        window.location.href = 'login.html';
    })
    .catch((err) => {
        form.reset();
        message.style.display = 'block'
        message.innerHTML = 'Username is already taken';
    });
    e.preventDefault();
}

document.getElementById('signupform').addEventListener('submit', signUpHandler);