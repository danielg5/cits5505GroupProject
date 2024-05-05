/* Moving this file to 'app/template/' directory 
 * to utilise flask app features
 *------------------------------*/

/* GAME JAVASCRIPT for game.html
 *------------------------------*/

function wordle (word1, word2) {
  // Find all matches of word2 letters in word1.
  // Repeated letters in word2 cannot be matched more times than it
  // appears in word1. For example: word1 = "craze" and word2 = "trees",
  // the second 'e' in word2 is ignored as 'e' only appears once in word1.
    
  const word1Arr = word1.split("");
    
  // create an array to store matches in word2
  const word2MatchArr = [];

  // Step 1, find all matches in same position.
  // Cannot combined boths steps in a nested 'for' loop
  // because step 1 needs to complete before step 2.
  for (let i = 0; i < word2.length; i++) {
    if (word2.at(i) == word1.at(i)) {
        word2MatchArr[i] = 2;
        // remove matched letter (required for second step)
        word1Arr[i] = '_'; 
    } else {
        word2MatchArr[i] = 0;
    }
  }

  // Step 2, find all matches in different position.
  // Separate loop to account for wordle treatment of duplicate letters,
  // where duplicated matches from letters repeated in word2 are ignored
  for (let i = 0; i < word2.length; i++) {
    for (let j = 0; j < word1.length; j++) {
      if (word2.at(i) == word1Arr[j] && word2MatchArr[i] != 2){
          word2MatchArr[i] = 1;
          // remove matched letter
          word1Arr[j] = '_'; 
        } 
      }
    }
  // TODO: remove this printout when gameplay troubleshooting complete
  console.log(word2MatchArr.toString());

  // TODO: remove this printout when gameplay troubleshooting complete
  //$("#printGuess").html('<p>' + 'Your word guess: ' + word2 + '; The secret word was: ' + word1 + '; Wordle function output: ' + word2MatchArr.toString() + '<p>');

  return word2MatchArr;
  }

function drawGuessTable() {

}

function createTable() {
// Create a node for table element (see Reference 1)
var table = document.createElement('table');
//table.style.width = '12%';

let word1 = "craze"
const wordle1 = [2,2,2,2,2]
// Create a tbody element in table element (see Reference 2)
var tbody = table.createTBody();
// Insert a single row (a <tr> element) in the tbody (see Reference 3)
row = tbody.insertRow();
// Insert a cell (a <td> element) in the row (see Reference 4)
var cell = row.insertCell();
cell.textContent = "Guess 1";
cell.className = 'guessTag';
for (var j = 0; j < word1.length; j++) {
  //var cell = row.insertCell();
  cell = row.insertCell();
  cell.textContent = word1.at(j);
  if (wordle1[j] == 2) {
    //cell.style.backgroundColor = 'green';
    cell.className = 'correctTag';
  } else if (wordle1[j] == 1) {
    //cell.style.backgroundColor = 'yellow';
    cell.className = 'misplacedTag';
  } else {
    //cell.style.backgroundColor = 'lightgray';
    cell.className = 'incorrectTag';
  }
}


// Find the existing element and append with the new element (see Reference 1)
document.getElementById('guessTableNode').appendChild(table);

// Prepend row at top of table
prependRow(table);

}

function prependRow(table) {
// Access the first tbody (at index 0) in table (see Reference 5)
var tbody = table.tBodies[0];  
let word2 = "trees"
const wordle2 = [0,2,1,0,0]
// Insert a row (a <tr> element at index 0) at top of tbody
var row = tbody.insertRow(0); 
var cell = row.insertCell();
cell.textContent = "Guess 2";
cell.className = 'guessTag';
for (var j = 0; j < word2.length; j++) {
  // Insert a cell (a <td> element) in the row
  var cell = row.insertCell();
  // Add text content of cell
  cell.textContent = word2.at(j);
  // Set classes for cell according to wordle match
  if (wordle2[j] == 2) {
    //cell.style.backgroundColor = 'green';
    cell.className = 'correctTag';
    } else if (wordle2[j] == 1) {
    //cell.style.backgroundColor = 'yellow';
    cell.className = 'misplacedTag';
    } else {
    //cell.style.backgroundColor = 'lightgray';
    cell.className = 'incorrectTag';
    }
  }

}

// Call the function to create the table
//createTable();



function initialiseGame() {
  let guessWord = document.getElementById("guessWord").value.toUpperCase();
  let secretWord = "CRAZE";
  // Create a mutable array to assign returned array from wordle() function
  let guessMatch = [];

  if (secretWord.length == guessWord.length) {
    // alert("Using wordle() function");
    guessMatch = wordle(secretWord, guessWord).slice();
    $("#printGuess").html('<p>' + 'Your word guess: ' + guessWord + '; The secret word was: ' + secretWord + '; Wordle function output: ' + guessMatch.toString() + '<p>');
    //wordle(secretWord, guessWord);
  } else {
    alert("Word length must be " + secretWord.length + " characters long. Please try again.");
  }
    
  createTable();
        
  }

/*
  TODO: Remove references if not required
  Reference:
  1. https://www.w3schools.com/js/js_htmldom_nodes.asp
  2. https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableElement/createTBody
  3. https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableElement/insertRow
  4. https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableRowElement/insertCell
  5. https://www.w3schools.com/jsref/coll_table_tbodies.asp
  
  
 */
