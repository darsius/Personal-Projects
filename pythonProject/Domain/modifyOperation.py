from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class ModificareOperatie(UndoRedoOperation):
    def __init__(self,
                 repository: Repository,
                 obiectVechi: Entity,
                 obiectNou: Entity):
        self.reposiotory = repository
        self.obiectVechi = obiectVechi
        self.obiectNou = obiectNou

    def undo(self):
        self.reposiotory.modifica(self.obiectVechi)

    def redo(self):
        self.reposiotory.modifica(self.obiectNou)
