document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.getElementById('csrf_token').value;

    // Common function to check email existence
    function checkEmail(emailInput, feedbackElement) {
        const email = emailInput.value;
        if (email) {
            fetch('/check_email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ email: email })
            })
            .then(response => response.json())
            .then(data => {
                if (!data.exists) {
                    feedbackElement.style.display = 'block';
                    emailInput.classList.add('is-invalid');
                } else {
                    feedbackElement.style.display = 'none';
                    emailInput.classList.remove('is-invalid');
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }

    // Check email existence on index page
    const loginEmailInput = document.getElementById('user_email');
    if (loginEmailInput) {
        loginEmailInput.addEventListener('blur', function() {
            const feedback = document.getElementById('email-feedback');
            checkEmail(loginEmailInput, feedback);
        });
    }

    // Check email existence and other validations on signup page
    const signupEmailInput = document.getElementById('email');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');

    if (signupEmailInput) {
        signupEmailInput.addEventListener('blur', function() {
            const emailWarning = document.getElementById('emailWarning');
            checkEmail(signupEmailInput, emailWarning);
        });

        usernameInput.addEventListener('blur', function() {
            const username = usernameInput.value;
            if (username) {
                fetch('/check_username', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify({ username: username })
                })
                .then(response => response.json())
                .then(data => {
                    const usernameWarning = document.getElementById('usernameWarning');
                    if (data.exists) {
                        usernameWarning.textContent = 'This username is already taken.';
                    } else {
                        usernameWarning.textContent = '';
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });

        confirmPasswordInput.addEventListener('keyup', function() {
            const matchMessage = document.getElementById('matchMessage');
            if (passwordInput.value !== confirmPasswordInput.value) {
                matchMessage.textContent = 'Passwords do not match.';
            } else {
                matchMessage.textContent = '';
            }
        });
    }
});
