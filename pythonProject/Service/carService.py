from random import random, randrange
import random

from Domain.addOperation import AdaugareOperatie
from Domain.car import Masina
from Domain.carValidator import MasinaValidator
from Domain.modifyOperation import ModificareOperatie
from Domain.deleteOperation import StergereOperatie

from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class MasinaService:
    def __init__(self, masinaRepository: Repository,
                 masinaValidator: MasinaValidator,
                 undoRedoService: UndoRedoService):
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator
        self.__undoRedoService = undoRedoService

    def get_all(self):
        """
        Afiseaza obiectele masini.
        :return: obiectele masini.
        """
        return self.__masinaRepository.read()

    def adauga(self, id_masina, model, an_achizitie, nr_km, in_garantie):
        """
        Adauga obiectul masina.
        :param id_masina: id-ul masinii
        :param model: modelul masinii
        :param an_achizitie: anul achizitiei masinii
        :param nr_km: numarul de kilometri ai masinii
        :param in_garantie: daca e sau nu in garantie; da/nu
        :return: obiectul masina
        """
        masina = Masina(id_masina, model, an_achizitie, nr_km, in_garantie)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.adauga(masina)

        self.__undoRedoService.clearRedo()
        adaugaOperatie = AdaugareOperatie(self.__masinaRepository, masina)
        self.__undoRedoService.addToUndo(adaugaOperatie)

    def modifica(self, id_masina, model, an_achizitie, nr_km, in_garantie):
        """
        Modifica obiectul masina.
        :param id_masina: id-ul masinii de modificat
        :param model: noul model
        :param an_achizitie: noul an al achizitiei
        :param nr_km: noul numar de kilometri
        :param in_garantie: noua garantie
        :return: noua masina
        """
        masinaVeche = self.__masinaRepository.read(id_masina)
        masina = Masina(id_masina, model, an_achizitie, nr_km, in_garantie)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.modifica(masina)

        self.__undoRedoService.clearRedo()
        modificaOperatie = ModificareOperatie(self.__masinaRepository,
                                              masinaVeche,
                                              masina)
        self.__undoRedoService.addToUndo(modificaOperatie)

    def sterge(self, id_masina):
        """
        Sterge o masina
        :param id_masina: id-ul masinii de sters
        :return: dictionarul fara masina respectiva..
        """
        masinaStersa = self.__masinaRepository.read(id_masina)

        self.__masinaRepository.sterge(id_masina)

        self.__undoRedoService.clearRedo()
        stergereOperatie = StergereOperatie(self.__masinaRepository,
                                            masinaStersa)
        self.__undoRedoService.addToUndo(stergereOperatie)

    def generareMasini(self, n):
        """
        Genereaza n masini.
        :param n: numarul de masini.
        :return: n masini random create.
        """
        i = 1
        while i <= n:
            id_masina = str(randrange(100))

            lstmodel = ["ford", "audi", "mercedes", "vw"]
            model = random.choice(lstmodel)

            lstan = [2000, 2001, 2009, 2008, 2003, 2020]
            an_achizitie = random.choice(lstan)

            lstnr_km = [100, 3, 0, 1000, 23.6, 34, 3]
            nr_km = random.choice(lstnr_km)

            lstin_garantie = ["da", "nu"]
            in_garantie = random.choice(lstin_garantie)

            masina = Masina(id_masina,
                            model,
                            an_achizitie,
                            nr_km,
                            in_garantie)

            if self.__masinaRepository.read(id_masina) is None:
                self.__masinaRepository.adauga(masina)
                i = i + 1
            else:
                i = i - 1

    def actualizareGarantie(self):
        """
        Actualizarea garanției la fiecare mașină: o mașină este în garanție
        dacă și numai dacă are maxim `3` ani de la achiziție și
        maxim `60 000` de km.
        :return: masinile cu garantia modificata.
        """
        for masina in self.__masinaRepository.read():
            if masina.nr_km <= 60000 and 2021 - masina.an_achizitie <= 3:
                masina.in_garantie = "da"
            else:
                masina.in_garantie = "nu"
            self.__masinaRepository.modifica(masina)
