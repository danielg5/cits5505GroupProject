from flask import request, jsonify
from app import flaskApp
from flask_login import current_user, login_required
from app.controllers import *
import json 

# start game (on first guess) as a loss to address players quiting game before using all guesses
# with first guess and if guessed_already = False, add 1 to loss_total
# which will be corrected on win, subtract 1 from loss_total and add 1 to win_total

@flaskApp.route('/process_guess', methods=['POST'])
#@login_required
def process_guess():
    # TODO: get username(player)
    #player = current_user.username
    player = 'daniel'
    # file created on game initialisation when '/game' route is used (route.py)
    filename = get_filename()
    # read player data dictionary
    data = read_file(filename) 
    if request.is_json:
        dataReceived = request.get_json()
        guess_word = dataReceived['guess_word']
        # on game start and on first guess only
        if data['guesses_remain'] == len(data['secret']):
           # on first guess, add 1 to loss_total
           add_loss(player) # start game as lost
        # on game win
        if guess_word == data['secret']:
           data['game_won'] = True # set game_won flag in data dictionary to True
           # add 1 to win_total and subtract 1 from loss_total
           add_win(player)
           # add points to points_total in database
           add_points(player, data['game_points'])
           # add guessed word to database
           add_guess_word(player, guess_word)
        else: 
           data['guesses_remain'] = data['guesses_remain'] - 1
           if not data['guessed_already']:
               # only subtract game point with guess if word not guessed already
               data['game_points'] = data['game_points'] - 1
        write_file(filename, data)
    else:
        guess_word = request.form.get('guess_word', 'No word received')
    return jsonify({
        #'message': 'guessed received',
        #'received_word': guess_word,
        'pattern': wordle(data['secret'], guess_word),
        'theme': data['theme'],
        #'secret_word': secret_word,
        'secret_length': len(data['secret']),
        'guesses_remain': data['guesses_remain'],
        'game_points': data['game_points'],
        'game_won': data['game_won']
    })

def get_filename():
    # TODO: get username(player)
    #player = current_user.username
    player = 'daniel'
    filename = './app/temp/' + player + '.txt'
    return filename

def read_file(filename):
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data

def write_file(filename, data):
    f = open(filename, 'w')
    json.dump(data, f)
    f.close()
    
def wordle(secret_word, guess_word):
    # find character matches between two words, return match pattern
    # matches must not be duplicated
    pattern = [0]*len(guess_word)  # set match pattern of guess to 0
    secretArr = list(secret_word)  # use to remove a matched character from secret word
    for i, g in enumerate(guess_word):  # find perfect matches
        if g == secret_word[i]:
            pattern[i] = 2
            secretArr[i] = '_'
    for i, g in enumerate(guess_word):  # find misplaced matches
        for j, s in enumerate(secretArr):
            if g == s and pattern[i] != 2: 
                pattern[i] = 1
                secretArr[j] = '_'
    return pattern

