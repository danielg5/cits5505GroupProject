
/* 
menu.js

JavaScript functionality for menu.html

*/



/* Initialise tooltips for all elements with titles */
const initTooltips = () => {
    const tooltipTriggerList = Array.from(document.querySelectorAll('[title]'));
    tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
};

/* Handle user logout

TO DO: Placeholder

*/
const logout = () => {
    // TO DO: Add cleanup operations before logout - clear cookies
    window.location.href = 'index.html';  // Redirect to index.html page after logout
};

/* Set username

TO DO : Placeholder

*/ 
const setUsername = () => {
    const usernameElement = document.getElementById('username');
    if (usernameElement) {
        usernameElement.textContent = 'YourUsername'; // TODO: Replace 'YourUsername' from database
    }
};

/* SuperWordle animation */
const setupSuperWordleAnimation = () => {
    const gridContainer = document.getElementById('wordle-grid');
    if (!gridContainer) return;

    const word = 'SUPERWORDLE';
    const rows = 1;  // Display word in one row

    // Create grid
    for (let i = 0; i < rows; i++) {
        const row = document.createElement('div');
        row.className = 'd-flex justify-content-center';
        for (let j = 0; j < word.length; j++) {
            const tile = document.createElement('div');
            tile.className = 'tile empty';
            row.appendChild(tile);
        }
        gridContainer.appendChild(row);
    }

    // Animate tiles to reveal word
    document.querySelectorAll('.tile').forEach((tile, index) => {
        setTimeout(() => {
            tile.classList.remove('empty');
            tile.textContent = word[index];
        }, 200 * index);  // Animation delay
    });
};

/* Play a Random Game Dice Icon animation */

// SVGs for dice Icons
const diceIcons = [
    `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-dice-1-fill" viewBox="0 0 16 16">
    <path d="M3 0a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V3a3 3 0 0 0-3-3zm5 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
    </svg>`,
    `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-dice-2-fill" viewBox="0 0 16 16">
    <path d="M0 3a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H3a3 3 0 0 1-3-3zm5.5 1a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0m6.5 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/>
    </svg>`,
    `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-dice-3-fill" viewBox="0 0 16 16">
    <path d="M3 0a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V3a3 3 0 0 0-3-3zm2.5 4a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m8 8a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0M8 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
    </svg>`,
    `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-dice-4-fill" viewBox="0 0 16 16">
    <path d="M3 0a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V3a3 3 0 0 0-3-3zm1 5.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m8 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m1.5 6.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0M4 13.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
    </svg>`,
    `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-dice-5-fill" viewBox="0 0 16 16">
    <path d="M3 0a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V3a3 3 0 0 0-3-3zm2.5 4a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0m8 0a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0M12 13.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3M5.5 12a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0M8 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
    </svg>`    
];


// function for Dice Animation
function setupDiceAnimation() {
    let diceInterval;

    function changeDiceIcon() {
        const diceIcon = diceIcons[Math.floor(Math.random() * diceIcons.length)];
        document.getElementById('diceIcon').innerHTML = diceIcon;
    }

    const playButton = document.getElementById('playButton');
    if (playButton) {
        // Start changing icons on page load
        diceInterval = setInterval(changeDiceIcon, 300);

        // Stop changing when hovering over button
        playButton.addEventListener('mouseover', () => {
            clearInterval(diceInterval);
        });

        // Start changing again when mouse stops hovering
        playButton.addEventListener('mouseout', () => {
            diceInterval = setInterval(changeDiceIcon, 300);
        });

        // Stop changing and redirect when button is clicked
        playButton.addEventListener('click', () => {
            clearInterval(diceInterval);
            location.href = 'game.html?type=random'; // TO DO: Needs to be handled in JavaScript (AJAX request, Flask routes and views.py)
        });
    }
}


// Event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    initTooltips();
    setUsername();
    setupSuperWordleAnimation();
    setupDiceAnimation();
    document.querySelector('.logout-button')?.addEventListener('click', logout);
});
