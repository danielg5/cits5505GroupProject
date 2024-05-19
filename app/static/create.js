
/* 
create.js

JavaScript functionality for create.html

*/



/* Initialise tooltips for all elements with titles */
const initTooltips = () => {
    const tooltipTriggerList = Array.from(document.querySelectorAll('[title]'));
    tooltipTriggerList.forEach(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
};

/* Get username*/ 
const fetchUsername = () => {
    fetch('/get_username')
        .then(response => response.json())
        .then(data => {
            const usernameElement = document.getElementById('username');
            if (usernameElement && data.username) {
                usernameElement.textContent = data.username;
            }
        })
        .catch(error => console.error('Error fetching username:', error));
};

/* SuperWordle animation */
const setupSuperWordleAnimation = () => {
    const gridContainer = document.getElementById('wordle-grid');
    if (!gridContainer) return;

    const word = 'SUPERWORDLE';
    const rows = 1;  // Display word in one row

    // Clear content
    gridContainer.innerHTML = '';

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

    const tiles = document.querySelectorAll('.tile');
    const animationDelay = 200;
    const totalAnimationTime = word.length * animationDelay;

    // Function animates tiles forward
    const revealWord = () => {
        tiles.forEach((tile, index) => {
            setTimeout(() => {
                tile.classList.remove('empty');
                tile.textContent = word[index];
            }, animationDelay * index);  // Animation delay
        });
    };

    // Function animates tiles backward
    const hideWord = () => {
        Array.from(tiles).reverse().forEach((tile, index) => {
            setTimeout(() => {
                tile.classList.add('empty');
                tile.textContent = '';
            }, animationDelay * index);  // Animation delay
        });
    };

    // Initial call to start animation
    revealWord();

    // Set up interval to repeat the animation sequence
    setInterval(() => {
        // Schedule the hide animation after the reveal completes and waits 1 second
        setTimeout(hideWord, totalAnimationTime + 1000);

        // Schedule the reveal to start again after the hide completes and waits another second
        setTimeout(revealWord, 2 * totalAnimationTime + 2000);
    }, 2 * totalAnimationTime + 2500);  // Total duration of a full cycle
};

// Event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    initTooltips();
    fetchUsername(); // get username
    setupSuperWordleAnimation();
    document.querySelector('.logout-button btn btn-primary')?.addEventListener('click', logout); // logout
});