from Domain.car import Masina

from Repository.repositoryJson import RepositoryJson
from emptyFile import golesteFisier


def testMasinaRepository():
    filename = 'testCarRepository.json'
    golesteFisier(filename)
    masinaRepository = RepositoryJson(filename)

    masina = Masina("1", "logan", 2000, 230000, "nu")
    masinaRepository.adauga(masina)

    assert masinaRepository.read(masina.id_entity) == masina

    masina = Masina("2", "dacia", 2000, 230000, "da")
    masinaRepository.adauga(masina)
    masinaRepository.sterge("1")

    assert masinaRepository.read("1") is None
    assert masinaRepository.read("2") == masina

    masina2 = Masina("2", "bmw", 2000, 230000, "da")
    masinaRepository.modifica(masina2)

    assert masina2.model == "bmw"

    masina3 = Masina("3", "audi", 200, 20000, "nu")
    masinaRepository.adauga(masina3)

    assert masinaRepository.read("1") is None
    assert masinaRepository.read("2") is not None
    assert masinaRepository.read("3") is not None
    assert masinaRepository.read("4") is None
