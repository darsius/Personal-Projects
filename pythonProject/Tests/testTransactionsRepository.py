from Domain.transaction import Tranzactie
from Repository.repositoryJson import RepositoryJson
from emptyFile import golesteFisier


def testTranzactieRepository():
    filename = 'testTransactionsRepository.json'
    golesteFisier(filename)
    tranzactieRepository = RepositoryJson(filename)

    tranzactie1 = Tranzactie("1", "1", "1", 30, 50, "12.12.2004,12:10")
    tranzactieRepository.adauga(tranzactie1)

    assert tranzactieRepository.read(tranzactie1.id_entity) == tranzactie1

    tranzactie1 = Tranzactie("1", "1", "1", 30, 50, "11.11.1111,11:11")
    tranzactieRepository.modifica(tranzactie1)

    assert tranzactie1.data == "11.11.1111,11:11"

    tranzactieRepository.sterge("1")

    assert tranzactieRepository.read("1") is None
