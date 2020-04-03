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


let createBizHandler = (e) => {
    refreshToken()
    access = JSON.parse(localStorage.getItem('access_token'));
    tosend = `Bearer ${access}`;
    
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let description = document.getElementById('description').value;

    let message = document.getElementById('messagesinfo');
    let form = document.getElementById('profileform');

    user_hood = localStorage.getItem('user_profile_hood');
    fetch('https://hood-drf.herokuapp.com/api/v1/bussinesses/' + user_hood + '/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-type': 'application/json',
                'Authorization': tosend,
            },
            body: JSON.stringify({
                name: name,
                email:email,
                description:description
            })
        })
    .then((res) => {
        if(res.status == 200){
            message.style.display = 'block'
            message.innerHTML = 'Only neighbourhood admins can Update this field!';
            setTimeout(function(){
                window.location.href='../hoodTemplates/hood.html';
              }, 5000);              
        } else if(res.status == 201){
            message.style.display = 'block'
            message.innerHTML = 'Bussiness Successfully Added!';
            form.reset()
            window.location.href='../hoodTemplates/hood.html';
        }
    })
    .catch((err) => {
        form.reset()
        message.style.display = 'block'
        message.innerHTML = 'A bussiness with that name already exists';
    });
    e.preventDefault();
}

document.getElementById('bizform').addEventListener('submit', createBizHandler);