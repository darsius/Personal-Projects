from Domain.clientCard import CardClient

from Repository.repositoryJson import RepositoryJson
from emptyFile import golesteFisier


def testCardClientRepository():
    filename = 'testClientCardRepository.json'
    golesteFisier(filename)
    cardClientRepository = RepositoryJson(filename)

    cardClient = \
        CardClient("1",
                   "Dan",
                   "Geo",
                   "5020803264321",
                   "12.12.2000",
                   "12.12.2001")
    cardClientRepository.adauga(cardClient)

    assert cardClientRepository.read(cardClient.id_entity) == cardClient
    assert cardClientRepository.read("2") is None

    cardClient2 = \
        CardClient("2",
                   "Dani",
                   "Gal",
                   "5020803264320",
                   "12.12.2000",
                   "12.12.2001")
    cardClientRepository.adauga(cardClient2)
    cardClientRepository.sterge(cardClient.id_entity)

    assert cardClientRepository.read(cardClient.id_entity) is None
    assert cardClientRepository.read("2") is not None

    cardClientRepository.sterge(cardClient2.id_entity)

    assert cardClientRepository.read("2") is None

    cardClient2 = \
        CardClient("2",
                   "Dani",
                   "Gal",
                   "5020803264320",
                   "12.12.2000",
                   "12.12.2001")
    cardClientRepository.adauga(cardClient2)

    cardClientRepository.modifica(
        CardClient("2",
                   "DD",
                   "Gal",
                   "5020803264320",
                   "12.12.2000",
                   "12.12.2001"))

    cardClient3 = \
        CardClient("2",
                   "DD",
                   "Gal",
                   "5020803264320",
                   "12.12.2000",
                   "12.12.2001")

    assert cardClientRepository.read(cardClient2.id_entity) == cardClient3
