// menu.js
function showInfoModal() {
    alert("Menu options include: Username, Play a Random Game, High Scores, Search for a Theme, Create a Theme.");
}

function logout() {
    // TODO - Add necessary cleanup operations before logout
    // TODO - Redirect to index.html page after logout
    window.location.href = 'index.html';
}

document.getElementById('username').textContent = 'YourUsername'; // TODO - Replace 'YourUsername' with dynamic data if available
document.querySelector('.logout-button').addEventListener('click', logout);
