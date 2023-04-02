from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class StergereOperatie(UndoRedoOperation):
    def __init__(self,
                 repository: Repository,
                 obiectSters: Entity):
        self.repository = repository
        self.obiectSters = obiectSters

    def undo(self):
        self.repository.adauga(self.obiectSters)

    def redo(self):
        self.repository.sterge(self.obiectSters.id_entity)
