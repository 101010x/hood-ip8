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


let createPostsHandler = (e) => {
    refreshToken()
    access = JSON.parse(localStorage.getItem('access_token'));
    tosend = `Bearer ${access}`;

    let title = document.getElementById('posttitle').value;
    let content = document.getElementById('content').value;
    let post_image = 'https://images.pexels.com/photos/695644/pexels-photo-695644.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
    let message = document.getElementById('messagesinfo');
    let form = document.getElementById('postform');

    user_hood = localStorage.getItem('user_profile_hood');
    fetch('https://hood-drf.herokuapp.com/api/v1/posts/' + user_hood + '/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-type': 'application/json',
                'Authorization': tosend,
            },
            body: JSON.stringify({
                post_title:title,
                post_content:content,
                post_image:post_image
            })
        })
    .then((res) => {
        console.log(res)
        message.style.display = 'block'
        message.innerHTML = 'Post Successfully Saved!';
        form.reset()
        window.location.href='../hoodTemplates/hood.html';
    })
    .catch((err) => {
        console.log(err)
        form.reset()
        message.style.display = 'block'
        message.innerHTML = 'Please use another Title!';
    });
    e.preventDefault();
}

document.getElementById('postform').addEventListener('submit', createPostsHandler);