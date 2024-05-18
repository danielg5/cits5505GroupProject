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
TODO To complete
The application consists of:
1. index - login page, to login with previously registered account
2. signup - signup page, to register a new account
3. menu - menu page, provide option to: (i) start a random game, from any user and theme; (ii) view leaderboard of player scores; (iii) search themes created by other users to play; (iv) create a theme for other players to play.


***4. Instructions to Launch Application***
TODO To complete
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

7. Test in Flask development server:
flask run

8. Open local host server:
http://127.0.0.1:5000


***5. Instructions for Running Tests on Application***
TODO To complete
