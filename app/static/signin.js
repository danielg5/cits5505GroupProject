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

// check if user name available
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

// check if password match previous one
function checkPasswordsMatch() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var message = document.getElementById('matchMessage');

    if (password === confirmPassword) {
        message.textContent = 'Passwords match.';
        message.style.color = 'green';
    } else {
        message.textContent = 'Passwords do not match.';
        message.style.color = 'red';
    }
}



 




