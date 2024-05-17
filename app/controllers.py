import random
from app import flaskApp, db  # delete flaskApp if not required
from app.model import Person, Theme, GuessedWord
import logging

# logging guessed_already flag
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
    #salt = '0123456789123456'
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
    player.loss_total -= 1
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
   # TODO: theme should be unique per creator, need validate in create.html 
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
    # TODO: theme should be unique per creator, need validate in create.html 
    # TODO: creator cannot have two themes with the same name)
    random_theme = Theme.query.\
    join(Person).\
    order_by(db.func.random()).first()
    return random_theme.person.username, random_theme.theme

def get_random_word(player, creator, theme):
    theme_words_list = get_theme_words(creator, theme)
    guessed_words = get_guessed_words(player)
    
    guessed_list = [] # list of guessed words
    for guessed_word in guessed_words:
        guessed_list.append(guessed_word.guessed_word)

    temp_list = theme_words_list[:] # make a shallow copy of theme words list
    # Remove previously guessed words from temp_list
    for theme_word in theme_words_list:
        for guessed_word in guessed_list:
            #if theme_word == guessed_word and temp_list:
            if theme_word == guessed_word:
                try:
                    # remove guessed word from theme words list
                    temp_list.remove(theme_word) 
                except:
                    logging.debug(f"Already removed {theme_word} from temp_list")
    
    random_word = None
    guessed_already = False
    if temp_list:
        random_word = random.choice(temp_list)
    else:
        random_word = random.choice(theme_words_list)
        guessed_already = True

    return random_word, guessed_already