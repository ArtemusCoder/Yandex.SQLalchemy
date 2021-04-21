from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "password"

    user1 = User()
    user1.surname = "Ivanov"
    user1.name = "Artemii"
    user1.age = 17
    user1.position = "pilot"
    user1.speciality = "research engineer"
    user1.address = "module_pilot"
    user1.email = "ivanov_artemii@mars.org"
    user1.hashed_password = "password"

    user2 = User()
    user2.surname = "Andy"
    user2.name = "Will"
    user2.age = 25
    user2.position = "pilot"
    user2.speciality = "research engineer"
    user2.address = "module_pilot"
    user2.email = "andy_will@mars.org"
    user2.hashed_password = "password"

    user3 = User()
    user3.surname = "Sean"
    user3.name = "Bean"
    user3.age = 20
    user3.position = "engineer"
    user3.speciality = "research engineer"
    user3.address = "module_engineer"
    user3.email = "sean_bean@mars.org"
    user3.hashed_password = "password"

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()


if __name__ == '__main__':
    main()
