from Domain.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, id_entitate=None):
        if id_entitate is None:
            return list(self.entitati.values())

        if id_entitate in self.entitati:
            return self.entitati[id_entitate]
        else:
            return None

    def adauga(self, entitate: Entity):
        if self.read(entitate.id_entity) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat")
        self.entitati[entitate.id_entity] = entitate

    def sterge(self, id_entitate):
        if self.read(id_entitate) is None:
            raise KeyError("Nu exista nicio entiate cu id-ul dat")
        del self.entitati[id_entitate]

    def modifica(self, entitate: Entity):
        if self.read(entitate.id_entity) is None:
            raise KeyError("Nu exista nicio entiate cu id-ul dat")
        self.entitati[entitate.id_entity] = entitate
