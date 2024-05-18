
/* 
menu.js

JavaScript functionality for menu.html

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


// Function for Dice Animation
function setupDiceAnimation() {
    let diceInterval;

    function getRandomDegree() {
        const randomDegree = Math.floor(Math.random() * 360); // Random degree from 0 to 359
        return randomDegree;
    }

    function changeDiceIcon() {
        const diceIcon = diceIcons[Math.floor(Math.random() * diceIcons.length)];
        const diceElement = document.getElementById('diceIcon');
        diceElement.innerHTML = diceIcon;
        // Rotate dice icon randomly
        const rotateDirection = Math.random() > 0.5 ? 1 : -1; // Randomly choose clockwise or counterclockwise
        const rotationDegrees = getRandomDegree();
        diceElement.style.transform = `rotate(${rotateDirection * rotationDegrees}deg)`;
        diceElement.style.transition = 'transform 0.9s ease';
    }

    const playButton = document.getElementById('playButton');
    if (playButton) {
        // Start on page load
        diceInterval = setInterval(changeDiceIcon, 300);

        // On hover, stop animation
        playButton.addEventListener('mouseover', () => {
            clearInterval(diceInterval);
        });

        // Off hover, Start animation
        playButton.addEventListener('mouseout', () => {
            diceInterval = setInterval(changeDiceIcon, 300);
        });

        // On click, stop animation and redirect to /random
        playButton.addEventListener('click', () => {
            clearInterval(diceInterval);
            location.href = '/random';
        });
    }
}


// Event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    initTooltips();
    fetchUsername(); // get username
    setupSuperWordleAnimation();
    setupDiceAnimation();
    document.querySelector('.logout-button btn btn-primary')?.addEventListener('click', logout); // logout
});
