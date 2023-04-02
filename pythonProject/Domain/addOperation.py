from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class AdaugareOperatie(UndoRedoOperation):
    def __init__(self,
                 reposiotry: Repository,
                 obiectAdaugat: Entity):
        self.repository = reposiotry
        self.obiectAdaugat = obiectAdaugat

    def undo(self):
        self.repository.sterge(self.obiectAdaugat.id_entity)

    def redo(self):
        self.repository.adauga(self.obiectAdaugat)
