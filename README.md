#***CITS5505 Agile Web Development Group Project (Semester 1, 2024)***

**README Contents**
1. Description of Application
2. Contributors
3. Summary of Application Architecture
4. Instructions to Launch Application
5. Instructions for Running Tests on Application
---

***1. Description of Application***
This application is a Wordle-like game, where a user (the player) guesses a word from a set of words created by another user (the creator). In essence, the creator "creates requests" for a player to guess a word, and the player "finds requests" and accepts the request by answering with a word guess.

The web application includes:
- an "introductory" view, a webpage (index.html) where a user is allowed to create an account or log in.
- a "create request" view, a webpage (create.html) where a user can create a request for other users to answer.
- a "find request" view, a webpage (search.html) where a user can search and accept any request. 

Users can create a list of ten words with a specific theme, e.g. beach theme [shells, sun, sand, surfboard,fish, starfish, seaweed, towels, waves, umbrella]. Users can choose any theme created by another user (e.g. beach), and the server will randomly choose a word from the beach list (e.g. shells) for the player to solve in a single-player Wordle-like game. The game play of the player is recorded and displayed in a leaderboard that features player statistics. 


***2. Contributors***

**Table of Contributors**
| UWA ID | Name | GitHub username |
|---|---|---|
| 21211711 | Asad Maza | asadmaza |
| 23740534 | Chung Hei Tse | maxchtse |
| 23277398 | Daniel Gal | danielg5|
| 23189834 | Shuyu Ding | FakeVeronica |


***3. Summary of Application Architecture***
The application consists of:
1. Index page, to login with previously registered account.
2. Signup page, to register a new account.
3. Menu page, provide links to: 
       - random game, from a random theme from any user
       - view leaderboard of player scores
       - search themes created by users
       - create a theme for users to play
4. Profile page, provide access to themes created by user or words previously guessed, or to change email or password. 
5. Leaderboard (High Scores) page to view player statistics.
6. Create page, to create custom theme of ten thematic words (up to 12 characters in length) for other users to play.
7. Search page, to search in terms of user or theme names to play.
8. Game page to play Wordle game. If the game is over or won, a new game will be started if the browser is refreshed. The game randomly selects words from the theme list that the player has not previously guessed. When a secret word is guessed, the word is saved to the player's list of previously guessed words. This is to ensure that points are not awarded for guessing the same word repeatedly. If the player has guessed words for all the words in the theme, then a "word previously guessed" game begins where no points are awarded, and player can continue to play to win or lose game. Each letter of secret word is worth a point and guess.

User data is stored in an SQLite database. Temporary gameplay data for each user is stored as a text file (one for each player) in 'app/temp/' which is over-writtten on the start of player's game.


***4. Instructions to Launch Application***
1. After completing a git pull of repository. 

2. Create a Python environment in Ubuntu 22.04: 
sudo apt-get install python3-pip
sudo apt-get install python3-venv
python3 -m venv venv_project2. 

3. Activate Python environment: 
source venv_project2/bin/activate

4. Install required programs:
pip install -r requirements.txt

5. Install Flask secret key in Ubuntu terminal:
export FLASK_SECRET_KEY='insert_your_custom_string_between_the_single_quotes'

6. Verify SECRET_KEY in flask shell:
print(app.config['SECRET_KEY'])

7. Create 'app.db' database. In parent directory of 'app/', enter commands using terminal:
flask db init
flask db migrate -m "Create Person, GuessedWord and Theme Tables"
flask db upgrade

8. Populate 'app.db' with instances of test data from test_data.py. In parent directory of 'app/', run flask shell and enter command:
import app.test_data

9. Test in Flask development server:
flask run

10. Open local host server:
http://127.0.0.1:5000

11. Register a new user account on the signup page (e.g. email: bob@email.com, password: password, user: bob) to gain access to the web application. The new user account can be used for subsequent login sessions.


***5. Instructions for Running Tests on Application***

1. Run the following script using the following command in root directory:
python -m unittest tests/test_route.py

