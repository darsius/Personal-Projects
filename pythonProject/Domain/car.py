from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Masina(Entity):
    """
    Obiectul masina :
    - id_masina : id-ul masinii
    - model: modelul masinii
    - an_achizite: anul achizitiei masinii
    - nr_km: numarul de km al masinii
    - in_garantie: True, daca masina e in garantie, Fals in caz contrar
    """
    model: str
    an_achizitie: int
    nr_km: float
    in_garantie: str
