// profile.js
/* 
Used for JavaScript functionality for profile.html
*/

// Initialize tooltips for all elements with titles
const initTooltips = () => {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[title]'));
    const tooltipList = tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
};

// TO DO: Handle user logout
const logout = () => {
    // Perform cleanup operations if necessary (clearing cookies)
    // Redirect to index.html page after logout
    window.location.href = 'index.html';
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

    passwordModalButton.addEventListener('click', () => $('#passwordModal').modal('show'));

    passwordForm.addEventListener('submit', event => {
        event.preventDefault();
        const currentPassword = document.getElementById('currentPassword').value;
        const newPassword = document.getElementById('newPassword').value;

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

// Event listeners for DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {
    initTooltips();
    animateWord();
    setupEmailForm();
    setupPasswordForm();
    document.querySelector('.logout-button').addEventListener('click', logout);
    document.getElementById('username').textContent = 'YourUsername'; // TODO Placeholder: Replace 'YourUsername' with database data
});