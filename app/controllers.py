import random
from app import flaskApp, db  # delete flaskApp if not required
from app.model import Person, Theme, GuessedWord


###########################################################
# Functions for new_user, password
#

def check_password_hash(email, password):
    # return True if password matches, False otherwise
    user = Person.query.filter_by(email=email).first()
    return user.check_password(password, user.salt)

def add_new_user(username, email, password):
    # create a new Person instance
    new_user = Person(username=username, email=email)
    # create random salt using random_salt method
    salt = Person.random_salt()
    # set salt attribute for Person instance
    new_user.salt = salt
    # set password_salt_hash attribute for Person instance
    new_user.set_password(password, salt)
    db.session.add(new_user)
    # abort on database error
    try:
       db.session.commit()
    except:
        db.session.rollback()

def check_email_exists(email):
    # return True if email exists, False otherwise
    user = Person.query.filter_by(email=email).first()
    return user is not None

def check_username_exists(username):
    # return True if username exists, False otherwise
    user = Person.query.filter_by(username=username).first()
    return user is not None

def get_userid(email):
    # return user id for email
    user = Person.query.filter_by(email=email).first()
    return user.id

def get_username(email):
    # return username for email
    user = Person.query.filter_by(email=email).first()
    return user.username

def get_username_by_id(id):
    # return username for id
    user = Person.query.filter_by(id=id).first()
    return user.username


###########################################################
# Functions for game and database
#

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
    temp_list = theme_words_list # theme words list
    i = len(theme_words_list)
    # remove previously guessed words from theme list
    for theme_words in theme_words_list:
        i -= 1  # reverse index
        for guessed_word, in guessed_words:
            if guessed_word == theme_words_list[i] and len(temp_list) != 0:
                del temp_list[i] # remove guessed word from theme words list

    random_word = None
    guessed_already = False
    if len(temp_list) != 0:
        random_word = random.choice(temp_list)
    else:
        random_word = random.choice(theme_words_list)
        guessed_already = True

    return random_word, guessed_already
