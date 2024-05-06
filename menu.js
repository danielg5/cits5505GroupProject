
/* 
menu.js

JavaScript functionality for menu.html

*/

// Initialise tooltips for all elements with titles
const initTooltips = () => {
    const tooltipTriggerList = Array.from(document.querySelectorAll('[title]'));
    tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
};

// Handle user logout
const logout = () => {
    // TO DO: Add cleanup operations before logout - clear cookies
    window.location.href = 'index.html';  // Redirect to index.html page after logout
};

// Set username
const setUsername = () => {
    const usernameElement = document.getElementById('username');
    if (usernameElement) {
        usernameElement.textContent = 'YourUsername'; // TODO: Replace 'YourUsername' from database
    }
};

// SuperWordle animation
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

// Event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    initTooltips();
    setUsername();
    setupSuperWordleAnimation();
    document.querySelector('.logout-button')?.addEventListener('click', logout);
});
