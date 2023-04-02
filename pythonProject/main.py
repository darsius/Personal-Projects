from Domain.clientCardValidator import CardClientValidator
from Domain.transactionValidator import TranzactieValidator
from Domain.carValidator import MasinaValidator

from Repository.repositoryJson import RepositoryJson
from Service.clientCardService import CardClientService
from Service.carService import MasinaService
from Service.transactionService import TranzactieService
from Service.undoRedoService import UndoRedoService
from UserInterface.console import Consola
from emptyFile import golesteFisier


def main():
    undoRedoService = UndoRedoService()

    masinaRepositoryJson = RepositoryJson("cars.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson,
                                  masinaValidator,
                                  undoRedoService)

    cardClientRepositoryJson = RepositoryJson("cards.json")
    cardClientValidator = CardClientValidator()
    cardClientService = CardClientService(cardClientRepositoryJson,
                                          cardClientValidator,
                                          undoRedoService)

    tranzactieRepositoryJson = RepositoryJson("transactions.json")
    tranzactieValidator = TranzactieValidator()
    tranzactieService = TranzactieService(
        masinaRepositoryJson,
        cardClientRepositoryJson,
        tranzactieRepositoryJson,
        tranzactieValidator,
        undoRedoService)

    golesteFisier("cards.json")
    golesteFisier("cars.json")
    golesteFisier("transactions.json")

    cardClientService.adauga("10", "a", "b", "99", "12.12.2010", "12.12.2010")
    cardClientService.adauga("11", "c", "d", "89", "12.12.2010", "12.12.2010")
    masinaService.adauga("10", "audi", 2000, 10000, "nu")
    tranzactieService.adauga("1", "10", "11", 30, 50, "12.12.1212,14:20")
    tranzactieService.adauga("2", "10", "11", 30, 50, "15.12.1212,14:20")

    console = Consola(masinaService,
                      cardClientService,
                      tranzactieService,
                      undoRedoService)

    console.runMenu()


main()
