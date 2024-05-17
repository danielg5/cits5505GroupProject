document.getElementById('email').addEventListener('blur', function() {
    const email = this.value;
    fetch('/check_email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken  
        },
        body: new URLSearchParams({
            'email': email
        })
    })
    .then(response => response.json())
    .then(data => {
        const emailWarning = document.getElementById('emailWarning');
        if (data.exists) {
            emailWarning.textContent = 'Email is already registered.';
        } else {
            emailWarning.textContent = '';
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('confirmPassword').addEventListener('keyup', function() {
    const password = document.getElementById('password').value;
    const confirmPassword = this.value;
    const matchMessage = document.getElementById('matchMessage');

    if (password === confirmPassword) {
        matchMessage.textContent = 'Passwords match.';
        matchMessage.style.color = 'green';
    } else {
        matchMessage.textContent = 'Passwords do not match.';
        matchMessage.style.color = 'red';
    }
});

document.getElementById('username').addEventListener('blur', function() {
    const username = this.value;
    fetch('/check_username', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken  
        },
        body: new URLSearchParams({
            'username': username
        })
    })
    .then(response => response.json())
    .then(data => {
        const usernameWarning = document.getElementById('usernameWarning');
        if (data.exists) {
            usernameWarning.textContent = 'Username is already taken.';
        } else {
            usernameWarning.textContent = '';
        }
    })
    .catch(error => console.error('Error:', error));
});
