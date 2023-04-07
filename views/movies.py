# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import Movie, MovieSchema
from implemented import movies_service
from setup_db import db

movie_ns = Namespace('movies')



@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            "director_id_arg": director_id,
            "genre_id_arg": genre_id,
            "year_arg": year
        }
        movies = movies_service.get_all(filters)
        return MovieSchema(many=True).dump(movies), 200
    
    def post(self):
        data = request.get_json()
        movie = movies_service.add_movie(data)
        return "", 201


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = movies_service.get_one(id)
        return MovieSchema().dump(movie), 200


    def put(self, id):
        data = request.get_json()
        movie = movies_service.change_movie(data)
        return "", 204

    def delete(self, id):
        movie = movies_service.delete_movie(id)
        return "", 204