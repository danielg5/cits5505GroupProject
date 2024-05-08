
/* 
leaderboard.js

JavaScript functionality for leaderboard.html

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


/* Get leaderboard data - placeholders*/
function fetchLeaderboardData() {
    fetch('path/to/your/api/endpoint')
    .then(response => response.json())
    .then(data => populateLeaderboard(data))
    .catch(error => console.error('Failed to fetch leaderboard data:', error));
}

function populateLeaderboard(data) {
    const leaderboardTable = document.getElementById("leaderboardData");
    leaderboardTable.innerHTML = ''; // Clear existing entries

    data.forEach((item, index) => {
        const row = leaderboardTable.insertRow();
        const rankCell = row.insertCell(0);
        const userCell = row.insertCell(1);
        const pointsCell = row.insertCell(2);
        const winRateCell = row.insertCell(3);
        const gamesPlayedCell = row.insertCell(4);

        rankCell.textContent = index + 1; // Assuming `data` sorted by rank
        userCell.textContent = item.username;
        pointsCell.textContent = item.points;
        winRateCell.textContent = `${item.winRate}%`;
        gamesPlayedCell.textContent = item.totalGames;
    });
}

// Back button function
function goBack() {
    window.history.back(); // Browser's history stack to go back
}


// Event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    initTooltips();
    setUsername();
    setupSuperWordleAnimation();
    fetchLeaderboardData();
    document.querySelector('.logout-button')?.addEventListener('click', logout);
});