from Tests.testClientCardRepository import testCardClientRepository
from Tests.testClientCardService import testCardClientService
from Tests.testCarRepository import testMasinaRepository
from Tests.testCarService import testMasinaService
from Tests.testTransactionsRepository import testTranzactieRepository
from Tests.testTransactionsService import testTranzactiiService


def runAllTests():
    testMasinaRepository()
    testCardClientRepository()
    testTranzactieRepository()
    testCardClientService()
    testMasinaService()
    testTranzactiiService()
