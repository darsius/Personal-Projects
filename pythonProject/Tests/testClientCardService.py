from Domain.clientCardValidator import CardClientValidator
from Repository.repositoryJson import RepositoryJson
from Service.clientCardService import CardClientService
from emptyFile import golesteFisier


def testCardClientService():
    # Teste CRUD
    golesteFisier("testClientCardService.json")

    cardValidator = CardClientValidator()
    cardRepository = RepositoryJson("testClientCardService.json")
    cardClientService = CardClientService(cardRepository, cardValidator)

    cardClientService.adauga("1",
                             "Ada",
                             "M",
                             459494394,
                             "10.12.1990",
                             "12.12.2019,12:12")
    assert len(cardClientService.get_all()) == 1

    cardClientService.modifica("1",
                               "Ada",
                               "Maria",
                               459494394,
                               "10.12.1990",
                               "12.12.2019,12:12")

    card = cardRepository.read("1")
    assert card.prenume == "Maria"

    cardClientService.sterge("1")
    assert len(cardClientService.get_all()) == 0

    cardClientService.adauga("1",
                             "Ada",
                             "M",
                             459494394,
                             "10.12.1990",
                             "12.12.2019,12:12")

    cardClientService.adauga("2",
                             "Aurica",
                             "P",
                             459434394,
                             "10.12.1990",
                             "12.12.2019,12:12")
