$(document).ready(() => {
    refreshToken()
    getUserProfile();
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

let getUserProfile = () => {
    try {
        let username = localStorage.getItem('username');
        let access = JSON.parse(localStorage.getItem('access_token'));
        tosend = `Bearer ${access}`;

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
        .then((profile) => {
            let output = '';
            
            if(profile.hood === null){
                profile.hood = 'You have not joined a hood yet';
            }
            output += `
            <h3 class="text-center">Profile</h3>
            <div>
                <div class="text-center">
                    <img src="https://res.cloudinary.com/mutugiii/image/upload/v1585139495/ben-sweet-2LowviVHZ-E-unsplash_gynjx7.jpg" id="avatar">
                    <br>
                    ${profile.name}
                    <br><br>
                    <div>
                        Location: <span style="font-weight: bolder;">${profile.location}</span> </br>
                        Hood: <span style="font-weight: bolder;">${profile.hood}</span>
                    </div>
                    <br>
                    <span style="font-weight: 900;">Bio:</span>
                    <div>
                        ${profile.bio}
                    </div>
                </div>
            </div>
            `
            document.getElementById('userprofile').innerHTML = output
        })
        .catch((err) => 
        {
            console.log(err)
            window.location.href = '../profileTemplates/createProfile.html'; 
        })
        
    } 
    catch(err) {
        console.log(err)
        window.location.href = '../registrationTemplates/login.html';
    }
}