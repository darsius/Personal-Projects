from Domain.carValidator import MasinaValidator
from Repository.repositoryJson import RepositoryJson
from Service.carService import MasinaService
from emptyFile import golesteFisier


def testMasinaService():
    # Teste CRUD
    golesteFisier("testCarService.json")

    masinaValidator = MasinaValidator()
    masinaRepository = RepositoryJson("testCarService.json")
    masinaService = MasinaService(masinaRepository, masinaValidator)

    masinaService.adauga("1",
                         "Audi",
                         20000,
                         2016,
                         "nu")
    assert len(masinaService.get_all()) == 1

    masinaService.modifica("1",
                           "Mercedes",
                           20000,
                           2016,
                           "nu")

    masina = masinaRepository.read("1")
    assert masina.model == "Mercedes"

    masinaService.sterge("1")
    assert len(masinaService.get_all()) == 0

    # Test Actualizare Garantie
    masinaService.adauga("1",
                         "Audi",
                         2019,
                         20000,
                         "nu")

    masinaService.adauga("2",
                         "Bmw",
                         2013,
                         20000,
                         "da")

    masinaService.adauga("3",
                         "Bmw",
                         2013,
                         2000,
                         "nu")

    masinaService.actualizareGarantie()
    masina1 = masinaRepository.read("1")
    masina2 = masinaRepository.read("2")
    masina3 = masinaRepository.read("3")

    assert masina1.in_garantie == "da"
    assert masina2.in_garantie == "nu"
    assert masina3.in_garantie == "nu"
