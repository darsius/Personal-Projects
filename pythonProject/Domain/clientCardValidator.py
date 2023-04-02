from Domain.clientCard import CardClient
from Domain.clientCardError import CardError


class CardClientValidator:
    @staticmethod
    def valideaza(card: CardClient):
        """
        Verifica ca datele introduse de utilizator sa fie valide
        :param card: obiectul card client
        :return: erorile
        """
        erori = []
        if int(card.cnp) < 0:
            erori.append("Cnp-ul trebuie sa fie pozitiv! ")
        if card.nume != str(card.nume):
            erori.append("Numele trebuie sa fie un string!")
        if card.prenume != str(card.prenume):
            erori.append("Preumele trebuie sa fie un string!")
        if len(erori) > 0:
            raise CardError("Cnp-ul trebuie sa fie pozitiv!")
