/*-------------------------------*
 * GAME JAVASCRIPT for game.html *
 *-------------------------------*/

function submitGuess() {
  // function activated on submit of guess
  let guessWord = document.getElementById("guessWord").value;
  //let secretLength = Number.parseInt('{{ length|safe }}');
  let secretLength = sLength;
  console.log("Secret length: " + secretLength);
  console.log(typeof secretLength);    
  if (secretLength == guessWord.length){
    $.ajax({
      type: "POST",
      url: "http://localhost:5000/process_guess",
      data: JSON.stringify({guess_word: guessWord}),
      contentType: "application/json; charset=utf-8",
      success: function(response) {
        console.log('Response:', response);
        playGame(guessWord, response)
      },
      error: function(xhr, status, error) {
        console.error('Error:', error);
      }
    });
  } else {
    alert("Guess word must be " + secretLength + " characters long!");
  }
  }
 
function playGame(guessWord, response) {
  let resultArr = response.pattern;
  let guessesRemain = response.guesses_remain;
  let secretLength = response.secret_length;
  let gameWon = response.game_won;
  let gamePoints = response.game_points;
  createTable(guessWord, resultArr, guessesRemain, secretLength, gameWon, gamePoints);
  updateWordleTable(guessWord, resultArr)
  document.getElementById("gamePoints").innerHTML = "Total Remaining Points: " + gamePoints;
  document.getElementById("gameGuesses").innerHTML = "(Guesses Remaining: " + guessesRemain + ")";
  if (guessesRemain == 0) {
    document.getElementById("guessInput").innerHTML = '<h3 id="overGame">Game Over!</h3>';
  }
  if (gameWon) {
    document.getElementById("guessInput").innerHTML = '<h3 id="wonGame">You Won!</h3>';
  }    
}

function updateWordleTable(guessWord, resultArr) {
  let table = document.getElementById("wordleTable");
  let tbody = table.tBodies[0];
  let row = tbody.rows[0]; // only get first rom
  for (let i = 0; i < guessWord.length; i++) {
    if (resultArr[i] == 2) {
      let cell = row.cells[i];
      cell.textContent = guessWord[i].toUpperCase();
      cell.className = 'correctTag';
    }
  }
}

function createTable(guessWord, resultArr, guessesRemain, secretLength, gameWon, gamePoints) {
  let table;
  // Only create a new table on the very first guess
  if ((gameWon && guessesRemain == secretLength) || (!gameWon && guessesRemain == secretLength - 1)) {
    table = document.createElement('table');
    let tbody = table.createTBody();
    document.getElementById('guessTableNode').appendChild(table);
  } else {
    // If not the first guess, reuse the existing table
    table = document.querySelector('#guessTableNode table');
  }
  prependRow(table, guessWord, resultArr, guessesRemain, secretLength, gameWon);    
}

function prependRow(table, guessWord, resultArr, guessesRemain, secretLength, gameWon) {
  let tbody = table.tBodies[0];
  let row = tbody.insertRow(0);
  let cell = row.insertCell();
  let guessNumber = tbody.rows.length;
  cell.textContent = "Guess " + guessNumber;
  cell.className = 'guessTag';
    for (let i = 0; i < secretLength; i++) {
      cell = row.insertCell();
      cell.textContent = guessWord.at(i);
      switch (resultArr[i]) {
        case 2:
          cell.className = 'correctTag';
          break;
        case 1:
          cell.className = 'misplacedTag';
          break;
        default:
          cell.className = 'incorrectTag';
      }
    }
}

