import random
from app import db
from app.model import Person, Theme, GuessedWord

def get_player():
    # get player username
    # TODO: get username for player
    player = 'daniel'
    return player

def add_loss(player):
    # add 1 to loss_total in database for player
    player = Person.query.filter_by(username=player).first()
    if player.loss_total is None:
        player.loss_total = 1  # cannot add 1 to None
    else:
        player.loss_total += 1
    db.session.commit()

def add_win(player):
    # add 1 to win_total in database for player
    # subtract 1 from loss_total in database for player
    player = Person.query.filter_by(username=player).first()
    if player.win_total is None:
        player.win_total = 1  # cannot add 1 to None
    else:
        player.win_total += 1
    player.loss_total += 1
    db.session.commit()

def add_points(player, points):
    # add points to points_total in database for player
    player = Person.query.filter_by(username=player).first()
    if player.points_total is None:
        player.points_total = points  # cannot add points to None
    else:
        player.points_total += points
    db.session.commit()

def add_guess_word(player, guess_word):
    # add new guessed word to database for player
    person = Person.query.filter_by(username=player).first()
    new_guessed_word = GuessedWord(person_id=person.id, guessed_word=guess_word)
    db.session.add(new_guessed_word)  # Add the new guessed word to the session
    db.session.commit()

def get_guessed_words(player):
    # get all guessed words (tuple list) for player
    guessed_words = GuessedWord.query.\
        join(Person).\
        filter(Person.username == player).all()
    return guessed_words

def get_creators_and_themes_list():
   # use database to get all theme creators and themes
   # list in search.html
   # return username and theme
   return None

def get_theme_words(creator, theme):
   # get theme words matches creator and theme
   # TODO: theme should be unique per creator 
   # TODO: creator cannot have two themes with the same name)
   # get theme words (tuple list)
   # use .first() as theme is duplicated with creator
    theme_words = Theme.query.\
         join(Person).\
         filter(Person.username == creator).\
         filter(Theme.theme == theme).first() 
    theme_words_list = [
        theme_words.word1, theme_words.word2, theme_words.word3,
        theme_words.word4, theme_words.word5, theme_words.word6,
        theme_words.word7, theme_words.word8, theme_words.word9,
        theme_words.word10]
    return theme_words_list

def get_random_theme():
    # get a random theme, return creator and theme
    # TODO: theme should be unique per creator 
    # TODO: creator cannot have two themes with the same name)
    random_theme = Theme.query.\
    join(Person).\
    order_by(db.func.random()).first()
    return random_theme.person.username, random_theme.theme

def get_random_word(player, creator, theme):
    # get a random word from the theme words not guessed before
    # if all words guessed, pick any word from the theme words
    theme_words_list = get_theme_words(creator, theme)
    guessed_words = get_guessed_words(player)
    temp_list = theme_words_list[:] # make a shallow copy of theme words list
    # remove previously guessed words from theme list
    for theme_word in theme_words_list:
        for guessed_word in guessed_words:
            if guessed_word == theme_word and temp_list:
                temp_list.remove(theme_word) # remove guessed word from theme words list
    random_word = None
    guessed_already = False
    if temp_list:
        random_word = random.choice(temp_list)
    else:
        random_word = random.choice(theme_words_list)
        guessed_already = True
    return random_word, guessed_already
