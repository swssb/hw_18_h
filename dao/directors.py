from dao.model.director import Director

class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def get_one(self, id):
        director = self.session.query(Director).get(id)
        return director