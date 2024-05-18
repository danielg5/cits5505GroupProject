/* 
profile.js

Used for JavaScript functionality for profile.html

*/

// Initialize tooltips for all elements with titles
const initTooltips = () => {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[title]'));
    const tooltipList = tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
};


// Handle animation "SUPERWORDLE"
const animateWord = () => {
    const gridContainer = document.getElementById('wordle-grid');
    const word = 'SUPERWORDLE';
    const rows = 1;
    const cols = word.length;

    for (let i = 0; i < rows; i++) {
        const row = document.createElement('div');
        row.className = 'd-flex justify-content-center';
        for (let j = 0; j < cols; j++) {
            const tile = document.createElement('div');
            tile.className = 'tile empty';
            row.appendChild(tile);
        }
        gridContainer.appendChild(row);
    }

    const tiles = document.querySelectorAll('.tile');
    tiles.forEach((tile, index) => {
        setTimeout(() => {
            tile.classList.remove('empty');
            tile.textContent = word[index];
        }, 200 * index);
    });
};

// Fetch and update email functionality
const setupEmailForm = () => {
    const emailForm = document.getElementById('changeEmailForm');
    const newEmailInput = document.getElementById('newEmail');

    $('#emailModal').on('show.bs.modal', () => {
        fetch('/get-current-email')
            .then(response => response.json())
            .then(data => {
                document.getElementById('userEmail').value = data.email;
            })
            .catch(error => console.error('Error fetching email:', error));
    });

    emailForm.addEventListener('submit', event => {
        event.preventDefault();
        if (!newEmailInput.checkValidity()) {
            newEmailInput.classList.add('is-invalid', 'invalid-shake');
            setTimeout(() => newEmailInput.classList.remove('invalid-shake'), 500);
            return;
        }
        newEmailInput.classList.remove('is-invalid');
        fetch('/update-email', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({email: newEmailInput.value})
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            $('#emailModal').modal('hide');
        })
        .catch(error => console.error('Error updating email:', error));
    });
};

// Setup password change functionality
const setupPasswordForm = () => {
    const passwordModalButton = document.querySelector("[title='Change your password']");
    const passwordForm = document.getElementById('changePasswordForm');
    const newPasswordInput = document.getElementById('newPassword');
    const confirmNewPasswordInput = document.getElementById('confirmNewPassword');

    passwordModalButton.addEventListener('click', () => $('#passwordModal').modal('show'));

    passwordForm.addEventListener('submit', event => {
        event.preventDefault();
        const currentPassword = document.getElementById('currentPassword').value;
        const newPassword = newPasswordInput.value;
        const confirmNewPassword = confirmNewPasswordInput.value;

        // Check if new password and confirm new password match
        if (newPassword !== confirmNewPassword) {
            alert('The new passwords do not match. Please try again.');
            confirmNewPasswordInput.classList.add('is-invalid');
            return; // Stop the form submission
        }

        // Remove the invalid class if it was added previously
        confirmNewPasswordInput.classList.remove('is-invalid');

        // Proceed with submitting the password update request
        fetch('/update-password', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({currentPassword: currentPassword, newPassword: newPassword})
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            $('#passwordModal').modal('hide');
        })
        .catch(error => console.error('Error updating password:', error));
    });
};

// TO DO - Setup function for the My Themes button
function setupMyThemesButton() {
    const myThemesButton = document.getElementById('myThemesButton');
    myThemesButton.addEventListener('click', function() {
        try {
            const username = sessionStorage.getItem('username'); // TO DO: Retrieve username from session storage
            if (username) {
                window.location.href = `search.html?username=${encodeURIComponent(username)}`;
            } else {
                alert('You must be logged in to see your themes.');
            }
        } catch (error) {
            console.error("Failed to redirect:", error);
        }



    });
}


// TO DO: Word Completed Button functions
function setupWordsCompletedButton() {
    const wordsCompletedButton = document.getElementById("wordsCompletedButton");
    if (wordsCompletedButton) {
        wordsCompletedButton.addEventListener('click', function() {
            fetchWordsCompleted();
            new bootstrap.Modal(document.getElementById('wordsCompletedModal')).show();
        });
    }
}

function fetchWordsCompleted() {
    fetch('/path/to/your/flask/endpoint')
    .then(response => response.json())
    .then(data => {
        populateWordsList(data);
    })
    .catch(error => console.error('Error fetching words:', error));
}

function populateWordsList(words) {
    const wordsList = document.getElementById("wordsList");
    wordsList.innerHTML = ''; // Clear previous entries
    words.forEach(word => {
        const item = document.createElement("div");
        item.classList.add("p-2"); // Bootstrap padding class for spacing
        item.textContent = word;
        wordsList.appendChild(item);
    });
}


// Event listeners for DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {
    initTooltips();
    animateWord();
    setupEmailForm();
    setupPasswordForm();
    document.querySelector('.logout-button btn btn-primary').addEventListener('click', logout); // logout
    document.querySelector('."back-button btn btn-primary').addEventListener('click', menu); // back to menu
    setupMyThemesButton(); // TO DO
    setupWordsCompletedButton(); // TO DO
    document.getElementById('username').textContent = 'YourUsername'; // TODO Placeholder: Replace 'YourUsername' with database data
});