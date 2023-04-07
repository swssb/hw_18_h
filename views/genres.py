from flask_restx import Namespace, Resource
from dao.model.genre import GenreSchema
from implemented import genres_service

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_service.get_all()
        return GenreSchema(many=True).dump(genres), 200

@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genres_service.get_one(id)
        return GenreSchema().dump(genre), 200