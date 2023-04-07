from dao.model.genre import Genre


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = self.session.query(Genre).all()
        return genres

    def get_one(self, id):
        genre = self.session.query(Genre).get(id)
        return genre