$(document).ready(() => {
    refreshToken()
    getServices()
    getBussinesses()
    getPosts()
})

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
        console.log(err)
        window.location.href='../registrationTemplates/login.html';
    }
}


let access = JSON.parse(localStorage.getItem('access_token'));
tosend = `Bearer ${access}`;

let username = localStorage.getItem('username');
let getUserHood = () => {
    if(username === null){
        window.location.href = '../registrationTemplates/login.html';
    }
    fetch('https://hood-drf.herokuapp.com/api/v1/profile/' + username, {
        method: 'GET',
        headers: {
            'Authorization': tosend
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if(data.hood === null){
            window.location.href = '../hoodTemplates/hoods.html';
        }
        localStorage.setItem('user_profile_hood', data.hood)
        return data.hood
    })
}


let getServices = () => {
    hood = getUserHood();
    user_hood = localStorage.getItem('user_profile_hood');
    fetch('https://hood-drf.herokuapp.com/api/v1/services/' + user_hood, {
        method: 'GET',
        headers: {
            'Authorization': tosend
        }
    })
    .then((res) => res.json())
    .then((data) => {
        let output = '<h5>Emergency Services</h5>';
        data.forEach((service) => {
            output += `
            <hr style="height:1px;border:none;color:rgb(145, 140, 140);background-color:#333;width: 630px;" />
            <div class="row">
                <div class="col-md-5">
                    <div style="text-decoration: underline;">${service.name}</div>
                    Contact Information:
                    <div class="text-center">
                        Phone: ${service.contact_number}
                        Email: ${service.email}
                    </div>
                    Description
                    <p>${service.description}</p>
                    Department Id: <span>${service.department}</span>
                </div>
            </div>
            `
        })
        document.getElementById('serviceslist').innerHTML = output
    })
    .catch((err) => {
        let output = '<h5>Emergency Services</h5>';
        output +=  `
        <div>
            <p>There are currently no emergency services</p>
        </div>
        `
        document.getElementById('serviceslist').innerHTML = output    
        // window.location.href = '../registrationTemplates/login.html';
    })
}

let getBussinesses = () => {
    let hood = getUserHood()
    user_hood = localStorage.getItem('user_profile_hood');
    fetch('https://hood-drf.herokuapp.com/api/v1/bussinesses/' + user_hood, {
        method: 'GET',
        headers: {
            'Authorization': tosend
        }
    })
    .then((res) => res.json())
    .then((data) => {
        let output = '<h5>Bussinesses</h5>';
        data.forEach((bussiness) => {
            output += `
            <hr style="height:1px;border:none;color:rgb(145, 140, 140);background-color:#333;width: 630px;" />
            <div class="row">
                <div class="col-md-5">
                    <div style="text-decoration: underline;">${bussiness.name}</div>
                     Contact Information: ${bussiness.email}
                     Description
                    <p>${bussiness.description}</p>
                </div>
            </div>
            `
        })

        document.getElementById('bussinesseslist').innerHTML = output
    })
    .catch((err) => {
        let output = '<h5>Bussinesses</h5>';
        output +=  `
        <div>
            <p>There are currently no Bussinesses Listed</p>
        </div>
        `
        document.getElementById('bussinesseslist').innerHTML = output
        // window.location.href = '../registrationTemplates/login.html';
    })
}

let getPosts = () => {
    let hood = getUserHood()
    user_hood = localStorage.getItem('user_profile_hood');
    fetch('https://hood-drf.herokuapp.com/api/v1/posts/' + user_hood, {
        method: 'GET',
        headers: {
            'Authorization': tosend
        }
    })
    .then((res) => res.json())
    .then((data) => {
        let output = '<h5>Posts by Users</h5>';
        data.forEach((post) => {
            output += `
            <div class="card col-md-6">
                <div class="card-header">${post.post_title}</div>
                <img class="card-img-top" src="${post.post_image}" alt="Card image cap">
                <div class="card-body">
                    <p class="card-text">${post.post_content}</p>
                    <div class="card-footer text-muted">
                    Post by ${post.user} on ${post.pub_date}
                    </div>
                </div>
            </div>
            `
        })

        document.getElementById('postslist').innerHTML = output
    })
    .catch((err) => {
        let output = '<h5>User posts</h5>';
        output +=  `
        <div>
            <p>There are currently no posts</p>
        </div>
        `
        document.getElementById('postslist').innerHTML = output
        // window.location.href = '../registrationTemplates/login.html';
    })
}