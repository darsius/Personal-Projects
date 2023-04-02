from typing import Protocol

from Domain.entity import Entity


class Repository(Protocol):
    def read(self, id_entitate=None):
        ...

    def adauga(self, entitate: Entity):
        ...

    def sterge(self, id_entitate):
        ...

    def modifica(self, entitate: Entity):
        ...
