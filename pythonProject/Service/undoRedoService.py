from Domain.undoRedoOperation import UndoRedoOperation


class UndoRedoService:
    def __init__(self):
        self.undoList = []
        self.redoList = []

    def doUndo(self):
        if self.undoList:
            topOperation = self.undoList.pop()
            topOperation.undo()
            self.redoList.append(topOperation)

    def doRedo(self):
        if self.redoList:
            topOperation = self.redoList.pop()
            topOperation.redo()
            self.undoList.append(topOperation)

    def clearRedo(self):
        self.redoList.clear()

    def addToUndo(self, operation: UndoRedoOperation):
        self.undoList.append(operation)
