# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.


class MoviesService:
    def __init__(self, movies_dao):
        self.movies_dao = movies_dao

    def get_all(self, filters):
        if filters.get("director_id_arg") is not None:
            return self.movies_dao.get_by_director(filters.get("director_id_arg"))
        elif filters.get("genre_id_arg") is not None:
            return self.movies_dao.get_by_genre(filters.get("genre_id_arg"))
        elif filters.get("year_arg") is not None:
            return self.movies_dao.get_by_year(filters.get("year_arg"))
        else:
            return self.movies_dao.get_all()

    def get_one(self, id):
        return self.movies_dao.get_one(id)

    def add_movie(self, data):
        return self.movies_dao.add_movie(data)

    def change_movie(self, data):
        id = data.get('id')
        movie = self.movies_dao.get_one(id)
        movie.name = data.get('name')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.movies_dao.change_movie(movie)

    def delete_movie(self, id):
        return self.movies_dao.delete_movie(id)
