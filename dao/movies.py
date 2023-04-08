# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.movie import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session
    def get_all(self):
        movies = self.session.query(Movie).all()
        return movies

    def get_one(self, id):
        movie = self.session.query(Movie).get(id)
        return movie

    def get_by_director(self, director_id):
        movie = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return movie

    def get_by_genre(self, genre):
        movie = self.session.query(Movie).filter(Movie.genre_id == genre).all()
        return movie

    def get_by_year(self, year):
        movie = self.session.query(Movie).filter(Movie.year == year).all()
        return movie


    def add_movie(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        self.session.close()
        return new_movie


    def change_movie(self, movie):

        self.session.add(movie)
        self.session.commit()
        self.session.close()
        return movie

    def delete_movie(self, id):
        movie = self.session.query(Movie).get(id)
        self.session.delete(movie)
        self.session.commit()
        self.session.close()
        return movie