
from flask_restx import Namespace, Resource
from dao.model.director import DirectorSchema
from implemented import directors_service

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = directors_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200

@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = directors_service.get_one(id)
        return DirectorSchema().dump(director), 200