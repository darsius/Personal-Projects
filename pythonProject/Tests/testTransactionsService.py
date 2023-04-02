from Domain.clientCard import CardClient
from Domain.car import Masina
from Domain.transaction import Tranzactie
from Domain.transactionValidator import TranzactieValidator
from Repository.repositoryJson import RepositoryJson
from Service.transactionService import TranzactieService
from emptyFile import golesteFisier


def testTranzactiiService():
    # Teste CRUD
    golesteFisier("testTransactionsService.json")

    masinaRepository = RepositoryJson("testCarService.json")
    cardClientRepository = RepositoryJson("testClientCardService.json")

    tranzactieRepository = RepositoryJson("testTransactionsService.json")
    tranzactieValidator = TranzactieValidator()
    tranzactieService = TranzactieService(
        masinaRepository,
        cardClientRepository,
        tranzactieRepository,
        tranzactieValidator)

    tranzactieService.adauga("1", "1", "1", 500, 50, "12.10.2019,10:54")
    tranzactieService.adauga("2", "2", "2", 5000, 400, "12.10.2019,10:32")
    assert len(tranzactieService.get_all()) == 2

    tranzactieService.modifica("2", "2", "2", 5000, 400, "12.10.2020,10:32")
    tranzactie2 = tranzactieRepository.read("2")
    assert tranzactie2.data == "12.10.2020,10:32"

    tranzactieService.sterge("2")
    assert len(tranzactieService.get_all()) == 1

    # Test AfisareTranzactiiInInterval
    tranzactieService.adauga("2", "2", "2", 5000, 400, "15.10.2019,10:32")
    tranzactieService.adauga("3", "3", "1", 600, 80, "12.10.2019,10:32")

    a = 60
    b = 700
    assert tranzactieService.afisareTranzactiiInInterval(a, b) == \
           [Tranzactie(id_entity='3',
                       id_masina='3',
                       id_card='1',
                       suma_piese=600,
                       suma_manopera=72.0,
                       data='12.10.2019,10:32')]

    # Test CautareFullText
    cuv = "Au"
    assert tranzactieService.cautareFullText(cuv) == \
           [Masina(id_entity='1',
                   model='Audi',
                   an_achizitie=2019,
                   nr_km=20000,
                   in_garantie='da'),
            CardClient(id_entity='2',
                       nume='Aurica',
                       prenume='P',
                       cnp=459434394,
                       data_nasterii='10.12.1990',
                       data_inregistrarii='12.12.2019,12:12')]

    cuv = "Opel"
    assert tranzactieService.cautareFullText(cuv) == []

    # Test OrodonareMasiniDupaManopera
    lista = tranzactieService.orodonareMasiniDupaManopera()
    assert lista[0] == {'masina': Masina(id_entity='2',
                                         model='Bmw',
                                         an_achizitie=2013,
                                         nr_km=20000,
                                         in_garantie='nu'),
                        'suma manopera': 360.0}

    assert lista[1] == {'masina': Masina(id_entity='3',
                                         model='Bmw',
                                         an_achizitie=2013,
                                         nr_km=2000,
                                         in_garantie='nu'),
                        'suma manopera': 72.0}

    assert lista[2] == {'masina': Masina(id_entity='1',
                                         model='Audi',
                                         an_achizitie=2019,
                                         nr_km=20000,
                                         in_garantie='da'),
                        'suma manopera': 45.0}

    # Test AfisareCarduriDupaReduceri
    lista = tranzactieService.afisareCarduriDupaReduceri()
    assert lista[0] == \
           {'Card Client': CardClient(id_entity='2',
                                      nume='Aurica',
                                      prenume='P',
                                      cnp=459434394,
                                      data_nasterii='10.12.1990',
                                      data_inregistrarii='12.12.2019,12:12'),
            'Reduceri': 40.0}

    assert lista[1] == \
           {'Card Client': CardClient(id_entity='1',
                                      nume='Ada',
                                      prenume='M',
                                      cnp=459494394,
                                      data_nasterii='10.12.1990',
                                      data_inregistrarii='12.12.2019,12:12'),
            'Reduceri': 13.0}

    # Test StergeDinIntervalZile
    a = 7
    b = 13
    tranzactieService.stergeDinIntervalZile(a, b)

    assert len(tranzactieService.get_all()) == 1
