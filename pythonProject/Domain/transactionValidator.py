from Domain.transaction import Tranzactie
from Domain.transactionError import TranzactieError


class TranzactieValidator:

    @staticmethod
    def valideaza(tranzactie: Tranzactie):
        """
        Verifica ca datele introduse de utilizator sa fie valide
        :param tranzactie: obiectul tranzactie
        :return: lista cu eventualele erori
        """
        erori = []
        if tranzactie.suma_manopera < 0:
            erori.append("Suma manoperei nu poate fi negativa! ")
        if tranzactie.suma_piese < 0:
            erori.append("Suma pieselor nu poate fi negativa! ")
        if len(erori) > 0:
            raise TranzactieError(erori)
