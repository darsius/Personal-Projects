from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class StergereMultipleOperatie(UndoRedoOperation):
    def __init__(self,
                 repository: Repository,
                 obiecteSterse: list):
        self.repository = repository
        self.obiecteSterse = obiecteSterse

    def undo(self):
        for entitate in self.obiecteSterse:
            self.repository.adauga(entitate)

    def redo(self):
        for entitate in self.obiecteSterse:
            self.repository.sterge(entitate.id_entity)
