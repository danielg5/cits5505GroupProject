document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.querySelector('input[name="csrf_token"]').value;

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

    // Common function to check username existence
    function checkUsername(usernameInput, feedbackElement) {
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
                if (data.exists) {
                    feedbackElement.style.display = 'block';
                    usernameInput.classList.add('is-invalid');
                } else {
                    feedbackElement.style.display = 'none';
                    usernameInput.classList.remove('is-invalid');
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }

    // Check email existence on index page
    const loginEmailInput = document.getElementById('email');
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
    const confirmPasswordInput = document.getElementById('confirm_password');

    if (signupEmailInput) {
        signupEmailInput.addEventListener('blur', function() {
            const emailWarning = document.getElementById('emailWarning');
            checkEmail(signupEmailInput, emailWarning);
        });

        usernameInput.addEventListener('blur', function() {
            const usernameWarning = document.getElementById('usernameWarning');
            checkUsername(usernameInput, usernameWarning);
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
