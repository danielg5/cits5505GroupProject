import random
from app import flaskApp, db  # delete if not required
from app.model import Person, Theme, GuessedWord

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
    theme_words = Theme.query.\
         join(Person).\
         filter(Person.username == creator).\
         filter(Theme.theme == theme).first()
    return theme_words

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
    theme_words = get_theme_words(creator, theme)
    guessed_words = get_guessed_words(player)
    temp_list = list(theme_words) # theme words list
    i = len(theme_words)
    # remove previously guessed words from theme list
    for theme_words, in theme_words:
        i -= 1  # reverse index
        for guessed_word, in guessed_words:
            if guessed_word == theme_words[i] and len(temp_list) != 0:
                del temp_list[i] # remove guessed word from theme words list

    random_word = None
    guessed_already = False
    if len(temp_list) != 0:
        random_word = random.choice(temp_list)
    else:
        random_word = random.choice(theme_words)
        guessed_already = True

    return random_word, guessed_already
