// menu.js

// Initialise tooltips for all elements with titles
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[title]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

function logout() {
    // TODO - Add necessary cleanup operations before logout
    // TODO - Redirect to index.html page after logout
    window.location.href = 'index.html';
}


document.getElementById('username').textContent = 'YourUsername'; // TODO - Replace 'YourUsername' with dynamic data if available
document.querySelector('.logout-button').addEventListener('click', logout); // TODO - logout



// SuperWordle animation
document.addEventListener("DOMContentLoaded", function() {
    const gridContainer = document.getElementById('wordle-grid');
    const word = 'SUPERWORDLE';
    const rows = 1;  // Display word in one row
    const cols = word.length;

    // Create grid
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

    // Animate tiles to reveal word
    function animateWord() {
        const tiles = document.querySelectorAll('.tile');
        tiles.forEach((tile, index) => {
            setTimeout(() => {
                tile.classList.remove('empty');
                tile.textContent = word[index];
            }, 200 * index);  //Animation delay
        });
    }

    // Start animation
    animateWord();
});
