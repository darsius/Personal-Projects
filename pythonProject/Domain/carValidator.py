from Domain.car import Masina
from Domain.carError import MasinaError


class MasinaValidator:

    @staticmethod
    def valideaza(masina: Masina):
        """
        Verifica ca datele introduse de utilizator sa fie valide
        :param masina: obiectul masina
        :return: lista cu eventualele erori
        """
        erori = []
        if masina.nr_km < 0:
            erori.append("Km masinii trebuie sa fie stricti pozitivi.")
        if masina.an_achizitie < 0:
            erori.append("Anul aparitiei masinii trebuie "
                         "sa fie strict pozitiv.")
        if masina.in_garantie not in ["da", "nu"]:
            erori.append("Statusul garantiei poate fi doar da/nu.")
        if len(erori) > 0:
            raise MasinaError(erori)
