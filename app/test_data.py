from app import db
from app.model import *

i1 = Person(username='asad', email='asad@email.com', password_salt_hash='passworD123', salt='salt', win_total=3, loss_total=0, points_total=7)
i2 = Person(username='daniel', email='daniel@email.com', password_salt_hash='passworD123', salt='salt', win_total=0, loss_total=1, points_total=0)
i3 = Person(username='max', email='max@email.com', password_salt_hash='passworD123', salt='salt', win_total=2, loss_total=2, points_total=8)
i4 = Person(username='shuyu', email='shuyu@email.com', password_salt_hash='passworD123', salt='salt', win_total=1, loss_total=3, points_total=9)
i5 = Theme(person_id=1, theme='beach', word1='shell', word2='sun', word3='sand', word4='surfboard', word5='fish', word6='starfish', word7='seaweed', word8='towel', word9='wave', word10='umbrella')
i6 = Theme(person_id=1, theme='food', word1='pavova', word2='cheesecake', word3='lasagna', word4='spaghetti', word5='hamburger', word6='biscuit', word7='croissant', word8='baguette', word9='avocado', word10='cantaloupe')
i7 = Theme(person_id=1, theme='country', word1='australia', word2='china', word3='brazil', word4='mexico', word5='malaysia',word6='germany', word7='france', word8='portugal', word9='spain', word10='indonesia')
i8 = Theme(person_id=2, theme='nuts', word1='peanut', word2='almond', word3='cashew', word4='hazelnut', word5='walnut', word6='macadamia', word7='pecan', word8='pistachio', word9='bunya', word10='acorn')
i9 = Theme(person_id=2, theme='cars', word1='mustang', word2='commodore', word3='ferrari', word4='ford', word5='holden', word6='limousine', word7='tesla', word8='opel', word9='toyota', word10='corolla')
i10 = Theme(person_id=3, theme='fruit', word1='soursop', word2='pawpaw', word3='guava', word4='fig', word5='strawberry', word6='watermelon', word7='grape', word8='blueberry', word9='orange', word10='raspberry')
i11 = Theme(person_id=4, theme='fruit', word1='banana', word2='apple', word3='lemon', word4='citrus', word5='strawberry', word6='watermelon', word7='grape', word8='blueberry', word9='orange', word10='raspberry')
i12 = Person(username='test', email='test@email.com', password_salt_hash='passworD123', salt='salt', win_total=0, loss_total=0, points_total=0)
i13 = GuessedWord(person_id=1, guessed_word='shell')
i14 = GuessedWord(person_id=1, guessed_word='sun')
i15 = GuessedWord(person_id=1, guessed_word='sand')
i16 = GuessedWord(person_id=3, guessed_word='pavlova')
i17 = GuessedWord(person_id=3, guessed_word='cantaloupe')
i18 = GuessedWord(person_id=4, guessed_word='macadamia')
db.session.add_all([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18])
db.session.commit()