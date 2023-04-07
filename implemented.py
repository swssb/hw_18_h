# файл для создания DAO и сервисов чтобы импортировать их везде


from setup_db import db
from dao.movies import MoviesDAO
from dao.directors import DirectorsDAO
from dao.genres import GenresDAO
from service.movies import MoviesService
from service.genres import GenresService
from service.directors import DirectorsService

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao=movies_dao)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao=directors_dao)

genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao=genres_dao)