function checkEmail() {
    var email = document.getElementById('email').value;
    var warningText = document.getElementById('emailWarning');

    fetch(`/check_email?email=${encodeURIComponent(email)}`)
    .then(response => response.json())
    .then(data => {
        if(data.status === 'taken') {
            warningText.textContent = 'This email is already registered, please use a different email.';
        } else {
            warningText.textContent = '';
        }
    })
    .catch(error => {
        console.error('Request failed:', error);
        warningText.textContent = 'Request error, please try again later.';
    });
}


function checkUsername() {
    var username = document.getElementById('username').value;
    var usernameWarning = document.getElementById('usernameWarning');

    fetch(`/check_username?username=${encodeURIComponent(username)}`)
    .then(response => response.json())
    .then(data => {
        if(data.status === 'taken') {
            usernameWarning.textContent = 'This username is already taken, please choose a different one.';
        } else {
            usernameWarning.textContent = '';
        }
    })
    .catch(error => {
        console.error('Request failed:', error);
        usernameWarning.textContent = 'Request error, please try again later.';
    });
}
