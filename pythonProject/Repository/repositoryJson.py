import jsonpickle

from Domain.entity import Entity
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati, indent=2))

    def read(self, id_entitate=None):
        self.entitati = self.__readFile()
        return super().read(id_entitate)

    def adauga(self, entitate: Entity):
        self.entitati = self.__readFile()
        super().adauga(entitate)
        self.__writeFile()

    def sterge(self, id_entitate):
        self.entitati = self.__readFile()
        super().sterge(id_entitate)
        self.__writeFile()

    def modifica(self, entitate: Entity):
        self.entitati = self.__readFile()
        super().modifica(entitate)
        self.__writeFile()
