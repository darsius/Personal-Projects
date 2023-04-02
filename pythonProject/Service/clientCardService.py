from Domain.addOperation import AdaugareOperatie
from Domain.clientCard import CardClient
from Domain.clientCardValidator import CardClientValidator
from Domain.modifyOperation import ModificareOperatie
from Domain.deleteOperation import StergereOperatie

from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class CardClientService:

    def __init__(self,
                 cardClientRepository: Repository,
                 cardClientValidator: CardClientValidator,
                 undoRedoService: UndoRedoService):
        self.__cardClientRepository = cardClientRepository
        self.__cardClientValidator = cardClientValidator
        self.__undoRedoService = undoRedoService

    def get_all(self):
        """
        Afiseaza obiectele card client.
        :return: cardurile client.
        """
        return self.__cardClientRepository.read()

    def adauga(self,
               id_card,
               nume,
               prenume,
               cnp,
               data_nasterii,
               data_inregistrarii):
        """
        Adauga obiectul card.
        :param id_card: id-ul cardului client
        :param nume: numele client
        :param prenume: prenumele client
        :param cnp: cnp client
        :param data_nasterii: data nasterii clientului
        :param data_inregistrarii: data inregistrarii cardului client
        :return: obiectul card in repository-ul specific.
        """
        card = CardClient(id_card,
                          nume,
                          prenume,
                          cnp,
                          data_nasterii,
                          data_inregistrarii)
        self.__cardClientValidator.valideaza(card)
        self.__cardClientRepository.adauga(card)

        self.__undoRedoService.clearRedo()
        adaugaOperatie = AdaugareOperatie(self.__cardClientRepository, card)
        self.__undoRedoService.addToUndo(adaugaOperatie)

    def sterge(self, id_card):
        """
        Sterge obiectul card.
        :param id_card: id-ul obiectului de sters
        :return: dictionarul fara cardul client respectiv.
        """
        cardSters = self.__cardClientRepository.read(id_card)

        self.__cardClientRepository.sterge(id_card)

        self.__undoRedoService.clearRedo()
        stergereOperatie = StergereOperatie(self.__cardClientRepository,
                                            cardSters)
        self.__undoRedoService.addToUndo(stergereOperatie)

    def modifica(self,
                 id_card,
                 nume,
                 prenume,
                 cnp,
                 data_nasterii,
                 data_inregistrarii):
        """
        Modifica obiectul card.
        :param id_card: id-ul cardului client de modificat
        :param nume: noul numele client
        :param prenume: noul prenume client
        :param cnp: noul cnp
        :param data_nasterii: noua data a nasterii
        :param data_inregistrarii: noua data a imregistrarii
        :return: obiectul card modificat in repository-ul specific.
        """
        cardVechi = self.__cardClientRepository.read(id_card)

        card = CardClient(id_card,
                          nume,
                          prenume,
                          cnp,
                          data_nasterii,
                          data_inregistrarii)
        self.__cardClientValidator.valideaza(card)
        self.__cardClientRepository.modifica(card)

        self.__undoRedoService.clearRedo()
        modificaOperatie = ModificareOperatie(self.__cardClientRepository,
                                              cardVechi,
                                              card)
        self.__undoRedoService.addToUndo(modificaOperatie)

    def cnpUnic(self, cnp=None):
        """
        Verificare pt cnp, sa fie unic.
        :param cnp: cnp-ul clientului
        :return: True, cnp unic, ridica eroare in caz contrar.
        """
        for cardClient in self.__cardClientRepository.read():
            if cardClient.cnp == cnp:
                raise ValueError("Cnp-ul exista deja!")
        return True
