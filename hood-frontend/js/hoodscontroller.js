$(document).ready(() => {
    refreshToken()
    getHoods()
})

access = JSON.parse(localStorage.getItem('access_token'));
tosend = `Bearer ${access}`;

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

let joinHoods = (hood, user) => {
    try {
        fetch('https://hood-drf.herokuapp.com/api/v1/join/' + hood + '/' + user, {
            method: 'PUT',
            headers: {
                'Authorization': tosend
            }
        })
        .then((res) => {
            if(res.status === 500){
                window.location.href = '../profileTemplates/createProfile.html'
            } else {
                window.location.href = '../hoodTemplates/hood.html';
            }
        })
        .catch((err) => {
            window.location.href = '../registrationTemplates/login.html';
        })
    }
    catch(err){
        window.location.href = '../registrationTemplates/login.html';
    }
}


let getHoods = () => {
    try{
        fetch('https://hood-drf.herokuapp.com/api/v1/hoods/', {
            method: 'GET',
            headers: {
                'Authorization': tosend
            }
        })
        .then((res) => res.json())
        .then((data) => {
            let output = '<h2 class="text-center">Hoods</h2>';
            data.forEach((hood) => {
                userhood = hood.hood_name
                if(hood.admin === null){
                    hood.admin = 'The Hood currently has no admin'
                }
                output += `
                <hr style="height:1px;border:none;color:rgb(145, 140, 140);background-color:#333;" />
                <div class="row">
                    <div class="col-md-6">
                        <div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title" id='hoodname'>${hood.hood_name}</h5>
                                <small class="card-subtitle mb-2 text-muted">${hood.location}</small>
                                </br> </br>
                                <p class="card-text">
                                    Number of occupants: ${hood.occupants_count} </br>
                                    ${hood.admin}
                                </p>
                                <a id='hoodjoin' class="card-link text-primary">Join Hood</a>
                            </div>
                        </div>
                    </div>
                </div>
                `;
            });

            document.getElementById('hoodslist').innerHTML = output;
            document.getElementById('hoodjoin').addEventListener('click', () => {
                hoodname  = document.getElementById('hoodname').innerHTML;
                username = localStorage.getItem('username')
                joinHoods(hoodname, username)
            });
        })
        .catch((err) => 
        {
            window.location.href = '../registrationTemplates/login.html';
        })
    }
    catch(err){
        window.location.href = '../registrationTemplates/login.html';
    }
}