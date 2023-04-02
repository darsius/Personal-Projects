from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Tranzactie(Entity):
    """
    Obiectul tranzactie:
    - id_tranzactie: id-ul tranzactiei
    - id_masina: id-ul masinii
    - id_card: id-ul cardului client
    - suma_piese: suma pieselor
    - suma_manopera: suma manoperei
    - data: data si ora la care s-a facut tranzactia
    """
    id_masina: str
    id_card: str
    suma_piese: float
    suma_manopera: float
    data: str
