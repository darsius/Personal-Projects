from Domain.addOperation import AdaugareOperatie
from Domain.modifyOperation import ModificareOperatie
from Domain.deleteMultipleOperation import StergereMultipleOperatie
from Domain.deleteOperation import StergereOperatie
from Domain.transaction import Tranzactie
from Domain.transactionValidator import TranzactieValidator
from Repository.repository import Repository

import datetime

from Service.undoRedoService import UndoRedoService


class TranzactieService:
    def __init__(self,
                 masinaRepository: Repository,
                 cardClientRepository: Repository,
                 tranzactieRepository: Repository,
                 tranzactieValidator: TranzactieValidator,
                 undoRedoService: UndoRedoService):
        self.__masinaRepository = masinaRepository
        self.__cardClientRepository = cardClientRepository
        self.__tranzactieRepository = tranzactieRepository
        self.__tranzactieValidator = tranzactieValidator
        self.__undoRedoService = undoRedoService

    def get_all(self):
        """
        Afiseaza obiectele tranzactie
        :return: obiectele tranzactie.
        """
        return self.__tranzactieRepository.read()

    def adauga(self,
               id_tranzactie,
               id_masina,
               id_card,
               suma_piese,
               suma_manopera,
               data):
        """
        Adauga o tranzactie.
        Dacă există un card client, atunci aplicați o reducere de `10%`
            pentru manoperă.
        Dacă mașina este în garanție, atunci piesele sunt gratis.
        Se tipărește prețul plătit și reducerile acordate.
        :param id_tranzactie: id-ul tranzactiei
        :param id_masina: id-ul masinii
        :param id_card: id-ul cardului client
        :param suma_piese: suma pieselor masinii
        :param suma_manopera: suma manoperei pentru masina
        :param data: data si ora tranzactiei
        :return: tranzactia adaugata in dicitonarul de tranzactii.
        """

        if self.__masinaRepository.read(id_masina) is None:
            raise KeyError("Nu exista masina cu id-ul dat")

        exista_id_card = self.__cardClientRepository.read(id_card)

        if exista_id_card:
            suma_manopera = suma_manopera - 0.1 * suma_manopera
        print(f"Ati platit {suma_manopera} pentru manopera. ")

        masina = self.__masinaRepository.read(id_masina)

        if masina.in_garantie == "da":
            suma_piese = 0
            print("Masina este in garantie si piesele sunt gratis. ")
        else:
            print(f"Ati platit {suma_piese} pentru piese. ")

        tranzactie = Tranzactie(
            id_tranzactie,
            id_masina,
            id_card,
            suma_piese,
            suma_manopera,
            data)

        self.__tranzactieValidator.valideaza(tranzactie)
        self.__tranzactieRepository.adauga(tranzactie)

        self.__undoRedoService.clearRedo()
        adaugaOperatie = \
            AdaugareOperatie(self.__tranzactieRepository, tranzactie)
        self.__undoRedoService.addToUndo(adaugaOperatie)

    def sterge(self, id_tranzactie):
        """
        Sterge o tranzactie.
        :param id_tranzactie: id-ul tranzactiei de sters.
        :return: Dictionarul de tranzactii fara tranzatia respectiva.
        """
        tranzactieStearsa = self.__tranzactieRepository.read(id_tranzactie)

        self.__tranzactieRepository.sterge(id_tranzactie)

        self.__undoRedoService.clearRedo()
        stergereOperatie = StergereOperatie(self.__tranzactieRepository,
                                            tranzactieStearsa)
        self.__undoRedoService.addToUndo(stergereOperatie)

    def modifica(self,
                 id_tranzactie,
                 id_masina,
                 id_card,
                 suma_piese,
                 suma_manopera,
                 data):
        """
        Modifica o tranzactie.
        Dacă există un card client, atunci aplicați o reducere de `10%`
            pentru manoperă.
        Dacă mașina este în garanție, atunci piesele sunt gratis.
        Se tipărește prețul plătit și reducerile acordate.
        :param id_tranzactie: id-ul tranzactiei de modificat
        :param id_masina: id-ul noii masini
        :param id_card: id-ul noului card client
        :param suma_piese: noua suma a pieselor
        :param suma_manopera: noua suma a manoperei
        :param data: noua data a tranzactei
        :return: tranzactia modificata in dictionarul de tranzactii.
        """
        if self.__masinaRepository.read(id_masina) is None:
            raise KeyError("Nu exista masina cu id-ul dat")

        exista_id_card = self.__cardClientRepository.read(id_card)

        if exista_id_card:
            suma_manopera = suma_manopera - 0.1 * suma_manopera
        print(f"Ati platit {suma_manopera} pentru manopera. ")

        masina = self.__masinaRepository.read(id_masina)

        if masina.in_garantie == "da":
            suma_piese = 0
            print("Masina este in garantie si piesele sunt gratis. ")
        else:
            print(f"Ati platit {suma_piese} pentru piese. ")

        tranzactieVeche = self.__tranzactieRepository.read(id_tranzactie)

        tranzactie = Tranzactie(
            id_tranzactie,
            id_masina,
            id_card,
            suma_piese,
            suma_manopera,
            data)

        self.__tranzactieValidator.valideaza(tranzactie)
        self.__tranzactieRepository.modifica(tranzactie)

        self.__undoRedoService.clearRedo()
        modificaOperatie = ModificareOperatie(self.__tranzactieRepository,
                                              tranzactieVeche,
                                              tranzactie)
        self.__undoRedoService.addToUndo(modificaOperatie)

    def afisareTranzactiiInInterval(self, a, b):
        """
        Afișarea tuturor tranzacțiilor cu suma cuprinsă într-un interval dat.
        :param a: marginea inferioara a intervalului
        :param b: marginea superioara a intervalului
        :return: tranzactiile care au suma cuprinsa in intervalul [a,b]
        """
        lista = []
        for tranzactie in self.__tranzactieRepository.read():
            if a <= tranzactie.suma_manopera + tranzactie.suma_piese <= b:
                lista.append(tranzactie)

        return lista

    def cautareFullText(self, cuv):
        """
        Cauta stringul 'cuv' in caracteristicile masinilor
        si ale cardurilor client.
        :param cuv: stringul de cautat
        :return: obiectele care contin stringul dat.
        """
        lista = []
        for masina in self.__masinaRepository.read():
            if cuv in masina.model \
                    or cuv in str(masina.an_achizitie) \
                    or cuv in str(masina.nr_km)\
                    or cuv in masina.in_garantie:
                lista.append(masina)

        for cardClient in self.__cardClientRepository.read():
            if cuv in cardClient.nume \
                    or cuv in cardClient.prenume \
                    or cuv in str(cardClient.cnp) \
                    or cuv in str(cardClient.data_nasterii) \
                    or cuv in str(cardClient.data_inregistrarii):
                lista.append(cardClient)
        return lista

    def orodonareMasiniDupaManopera(self):
        """
        Ordoneaza masinile dupa suma manoperei.
        :return: lista sortata cu dictionare care au chei masina
        si valoarea suma platita pentru manopera.
        """
        rezultat = []
        sumaPerMasini = {}

        for masina in self.__masinaRepository.read():
            sumaPerMasini[masina.id_entity] = 0
        for tranzactie in self.__tranzactieRepository.read():
            sumaPerMasini[tranzactie.id_masina] += \
                tranzactie.suma_manopera

        for id_masina in sumaPerMasini:
            rezultat.append({
                "masina": self.__masinaRepository.read(id_masina),
                "suma manopera": sumaPerMasini[id_masina]
            })

        return sorted(rezultat, key=lambda suma: suma["suma manopera"],
                      reverse=True)

    def afisareCarduriDupaReduceri(self):
        """
        Afișarea cardurilor client ordonate descrescător "
        "după valoarea reducerilor obținute
        :return: lista ordonata cu dictionare care au chei cardul client
        si reducerile respective.
        """
        reduceri = {}
        rezultat = []

        for cardClient in self.__cardClientRepository.read():
            reduceri[cardClient.id_entity] = 0
        print(reduceri)
        for tranzactie in self.__tranzactieRepository.read():
            if tranzactie.id_card in reduceri:
                reduceri[tranzactie.id_card] += \
                    10/9*tranzactie.suma_manopera - tranzactie.suma_manopera

        for id_card in reduceri:
            rezultat.append({
                "Card Client": self.__cardClientRepository.read(id_card),
                "Reduceri": reduceri[id_card]
            })
        return sorted(rezultat, key=lambda reducere: reducere["Reduceri"],
                      reverse=True)

    def stergeDinIntervalZile(self, a, b):
        """
        Șterge toate tranzacțiile dintr-un anumit interval de zile.
        :param a: ziua de la care sa inceapa stergerea
        :param b: ziua pana la care sa se stearga
        :return: tranzactiile fara cele care au ziua
        in interiorul [a,b]
        """
        listaTranzactii = []

        for tranzactie in self.__tranzactieRepository.read():
            data_completa = tranzactie.data
            data_formatata = datetime.datetime\
                .strptime(str(data_completa), "%d.%m.%Y,%H:%M")
            ziua = data_formatata.day
            if a <= ziua <= b:
                listaTranzactii.append(tranzactie)
                self.__tranzactieRepository.\
                    sterge(tranzactie.id_entity)

        self.__undoRedoService.clearRedo()
        stergereMultipleOperatie = \
            StergereMultipleOperatie(self.__tranzactieRepository,
                                     listaTranzactii)
        self.__undoRedoService.addToUndo(stergereMultipleOperatie)

    def stergeInCascada(self, masina_sters):
        """
        Cand sterg o entitate sa stearga toate
        tranzactiile care implica acea entitate.
        :param masina_sters: entitatea de sters
        :return: tranzactiile fara cele care contin masina respectiva.
        """
        for tranzactie in self.__tranzactieRepository.read():
            if tranzactie.id_masina == masina_sters:
                tranzactieStearsa = \
                    self.__tranzactieRepository.read(tranzactie.id_entity)
                self.__tranzactieRepository.sterge(tranzactie.id_entity)
            self.__undoRedoService.clearRedo()
            stergereOperatie = StergereOperatie(self.__tranzactieRepository,
                                                tranzactieStearsa)
            self.__undoRedoService.addToUndo(stergereOperatie)
        self.__masinaRepository.sterge(masina_sters)
