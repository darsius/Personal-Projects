from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class CardClient(Entity):
    """
    Obiectul card:
    - id_card: id-ul cardului
    - nume: nume client
    - prenume: prenume client
    - cnp: cnp client
    - data_nasterii: data nasterii clientului
    - data_inregistrarii: data inregistrarii cardului
    """
    nume: str
    prenume: str
    cnp: str
    data_nasterii: str
    data_inregistrarii: str
