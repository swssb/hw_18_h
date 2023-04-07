

class DirectorsService:
    def __init__(self, directors_dao):
        self.directors_dao = directors_dao

    def get_all(self):
        return self.directors_dao.get_all()

    def get_one(self, id):
        return self.directors_dao.get_one(id)