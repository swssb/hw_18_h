# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api
#
from config import Config
from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    # create_data(app, db)

# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#         m1 = Movie(id=1, title='Rising Sun', description='Nice sun',trailer='youtu.be/j2Hs2', year=2009,
#                    rating=5, genre_id=1, director_id=1)
#         m2 = Movie(id=2, title='Transpeople', description='Old republic of humans', trailer='youtu.be/Ulss2',
#                    year=2022, rating=6, genre_id=1, director_id=2)
#         m3 = Movie(id=3, title='Liquid Card', description='The card are going to hell', trailer='youtu.be/L5J0o',
#                    year=2017, rating=10, genre_id=2, director_id=1)
#         g1 = Genre(id=1, name='Drama')
#         g2 = Genre(id=2, name='Comedy')
#         d1 = Director(id=1, name='Grigoriy')
#         d2 = Director(id=2, name='Anatoliy')
#         with db.session.begin():
#             db.session.add_all([m1, m2, m3, g1, g2, d1, d2])

app = create_app(Config())
app.debug = True
#
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
