let refreshToken = () => {
    try {
        let token_refresh = JSON.parse(localStorage.getItem('refresh_token'));        
        if(token_refresh === null){
            window.location.href='../registrationTemplates/login.html';
        } else {
            axios.post('https://hood-drf.herokuapp.com/api/v1/token/refresh/',{
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-type': 'application/json'
                },
                refresh: token_refresh,
            })
            .then((res) => {
                new_access_token = JSON.stringify(res.data.access);
                localStorage.setItem('access_token', new_access_token)
            })
        }
    }
    catch(err) {
        // console.log(err)
        // window.location.href='../registrationTemplates/login.html';
    }
}


let createProfileHandler = (e) => {
    refreshToken()
    access = JSON.parse(localStorage.getItem('access_token'));
    tosend = `Bearer ${access}`;
    let name = localStorage.getItem('username')
    let bio = document.getElementById('bio').value;
    let location = $('#userlocation :selected').val()
    // let profile_picture = document.getElementById('profile_pic').files[0];
    let message = document.getElementById('messagesinfo');
    let form = document.getElementById('profileform');

    fetch('https://hood-drf.herokuapp.com/api/v1/profiles/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-type': 'application/json',
                'Authorization': tosend,
            },
            body: JSON.stringify({
                name: name,
                bio: bio,
                location: location,
            })
        })
    .then((res) => {
        message.style.display = 'block'
        message.innerHTML = 'Profile Successfully Saved!';
        form.reset()
        window.location.href='../profileTemplates/userprofile.html';
    })
    .catch((err) => {
        form.reset()
        message.style.display = 'block'
        message.innerHTML = 'Profile already exists';
    });
    e.preventDefault();
}

document.getElementById('profileform').addEventListener('submit', createProfileHandler);