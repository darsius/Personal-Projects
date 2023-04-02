import datetime

from Service.clientCardService import CardClientService
from Service.carService import MasinaService
from Service.transactionService import TranzactieService
from datetime import datetime

from Service.undoRedoService import UndoRedoService
from Tests.testAll import runAllTests


class Consola:
    def __init__(self,
                 masinaService: MasinaService,
                 cardClientService: CardClientService,
                 tranzactieService: TranzactieService,
                 undoRedoService: UndoRedoService):
        self.masinaService = masinaService
        self.cardClientService = cardClientService
        self.tranzactieService = tranzactieService
        self.undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD masini")
            print("2. CRUD card client")
            print("3. CRUD tranzactie")
            print("4. Căutare mașini și clienți. Căutare full text")
            print("5. Afișarea tuturor tranzacțiilor cu suma "
                  "cuprinsă în intervalul [a,b]")
            print("6. Afișarea mașinilor  ordonate descrescător "
                  "după suma obținută pe manoperă")
            print("7. Afișarea cardurilor client ordonate descrescător "
                  "după valoarea reducerilor obținute")
            print("8. Ștergerea tuturor tranzacțiilor dintr-un anumit "
                  "interval de zile. ")
            print("9. Actualizarea garanției la fiecare mașină")
            print("g. Generare n masini")
            print("s. Stergere masini in cascada")
            print("t. Ruleaza teste")
            print("u. Undo")
            print("r. Redo")
            self.showAllMasini()
            self.showAllCardClient()
            self.showAllTranzactii()
            optiune = input("Alegeti o optiune ")
            if optiune == "1":
                self.runCrudMasiniMenu()
            elif optiune == "2":
                self.runCrudCardClientMenu()
            elif optiune == "3":
                self.runCrudTranzactieMenu()
            elif optiune == "4":
                self.uiCautareFullText()
            elif optiune == "5":
                self.uiAfisareTranzactiiInInterval()
            elif optiune == "6":
                self.uiAfisareMasiniDupaManopera()
            elif optiune == "7":
                self.uiAfisareCarduriDupaReduceri()
            elif optiune == "8":
                self.uiStergeDinIntervalZile()
                self.showAllTranzactii()
            elif optiune == "9":
                self.uiActualizareGarantie()
                self.showAllMasini()
            elif optiune == "g":
                self.runGenerareMasini()
            elif optiune == "s":
                self.StergeInCascada()
                self.showAllTranzactii()
            elif optiune == "t":
                runAllTests()
            elif optiune == "u":
                self.undoRedoService.doUndo()
            elif optiune == "r":
                self.undoRedoService.doRedo()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita")

    def runCrudMasiniMenu(self):
        while True:
            print("1. Adauga masina")
            print("2. Sterge masina")
            print("3. Modifca masina")
            print("a. Afiseaza toate masinile")
            print("x. Iesire")

            optiune = input("Alegeti o optiune ")

            if optiune == "1":
                self.uiAdaugaMasina()
            elif optiune == "2":
                self.uiStergeMasina()
            elif optiune == "3":
                self.uiModificaMasina()
            elif optiune == "a":
                self.showAllMasini()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita")

    def runCrudCardClientMenu(self):
        while True:
            print("1. Adauga card client")
            print("2. Sterge card client")
            print("3. Modifca card client")
            print("a. Afiseaza toate cardurile client")
            print("x. Iesire")

            optiune = input("Alegeti o optiune ")

            if optiune == "1":
                self.uiAdaugaCardClient()
            elif optiune == "2":
                self.uiStergeCardClient()
            elif optiune == "3":
                self.uiModificaCardClient()
            elif optiune == "a":
                self.showAllCardClient()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita")

    def runCrudTranzactieMenu(self):
        while True:
            print("1. Adauga tranzactie")
            print("2. Sterge tranzactie")
            print("3. Modifca tranzactie")
            print("a. Afiseaza toate tranzactiile")
            print("x. Iesire")

            optiune = input("Alegeti o optiune ")

            if optiune == "1":
                self.uiAdaugaTranzactie()
            elif optiune == "2":
                self.uiStergeTranzactie()
            elif optiune == "3":
                self.uiModificaTranzactie()
            elif optiune == "a":
                self.showAllTranzactii()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita")

    def uiAdaugaMasina(self):
        try:
            id_masina = input("Dati id-ul masinii: ")
            model = input("Dati modelul masinii: ")
            an_achizitie = int(input("Dati anul achizitiei: "))
            nr_km = float(input("Dati numarul de kilometri ai masinii: "))
            in_garantie = input("Dati statusul garantiei (da/nu) "
                                "al masinii: ")

            self.masinaService.adauga(
                id_masina, model, an_achizitie, nr_km, in_garantie)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeMasina(self):
        try:
            id_masina = input("Dati id-ul masinii de sters: ")

            self.masinaService.sterge(id_masina)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaMasina(self):
        try:
            id_masina = input("Dati id-ul masinii de modificat: ")
            model = input("Dati modelul noii masini: ")
            an_achizitie = int(input("Dati noul an al achizitiei: "))
            nr_km = float(input("Dati noul numarul de kilometri ai masinii: "))
            in_garantie = input("Dati noul status al garantiei (da/nu) "
                                "masinii: ")

            self.masinaService.modifica(
                id_masina, model, an_achizitie, nr_km, in_garantie)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllMasini(self):
        for masina in self.masinaService.get_all():
            print(masina)

    def uiAdaugaCardClient(self):
        try:
            id_card = input("Dati id-ul cardului client: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            cnp = input("Dati cnp-ul clientului: ")
            data_nasterii = input("Dati data nasterii clientului "
                                  "(in format dd.mm.yyyy): ")
            data_nasterii = datetime.strptime(data_nasterii, "%d.%m.%Y")
            data_inregistrarii = input("dati data inregistrarii clientului "
                                       "(in format dd.mm.yyyy): ")
            data_inregistrarii = \
                datetime.strptime(data_inregistrarii, "%d.%m.%Y")

            if self.cardClientService.cnpUnic(cnp):
                self.cardClientService.adauga(
                    id_card,
                    nume,
                    prenume,
                    cnp,
                    data_nasterii,
                    data_inregistrarii)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeCardClient(self):
        try:
            id_card = input("Dati id-ul cardului client de sters: ")

            self.cardClientService.sterge(id_card)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaCardClient(self):
        try:
            id_card = input("Dati id-ul cardului client de modificat: ")
            nume = input("Dati numele noului client: ")
            prenume = input("Dati prenumele noului client: ")
            cnp = input("Dati cnp-ul noului client: ")
            data_nasterii = input("Dati data nasterii clientului "
                                  "(in format dd.mm.yyyy): ")
            data_nasterii = datetime.strptime(data_nasterii, "%d.%m.%Y")
            data_inregistrarii = input("dati data inregistrarii clientului "
                                       "(in format dd.mm.yyyy): ")
            data_inregistrarii = \
                datetime.strptime(data_inregistrarii, "%d.%m.%Y")

            self.cardClientService.modifica(
                id_card,
                nume,
                prenume,
                cnp,
                data_nasterii,
                data_inregistrarii)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllCardClient(self):
        for card in self.cardClientService.get_all():
            print(card)

    def uiAdaugaTranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul tranzactiei: ")
            id_masina = input("Dati id-ul masinii:  ")
            id_card = input("Dati id-ul cardului client: ")
            suma_piese = float(input("Dati suma pieselor: "))
            suma_manopera = float(input("Dati suma manoperei: "))
            data = input("Dati data si ora tranzactiei "
                         "(in format dd.mm.yyyy,hh:mm): ")
            data = datetime.strptime(data, "%d.%m.%Y,%H:%M")

            self.tranzactieService.adauga(
                id_tranzactie,
                id_masina,
                id_card,
                suma_piese,
                suma_manopera,
                data.strftime("%d.%m.%Y,%H:%M"))

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeTranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul tranzactiei de sters ")

            self.tranzactieService.sterge(id_tranzactie)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaTranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul tranzactiei de modificat: ")
            id_masina = input("Dati id-ul noii masini:  ")
            id_card = input("Dati id-ul cardului noului client: ")
            suma_piese = float(input("Dati noua suma a pieselor: "))
            suma_manopera = float(input("Dati noua suma a manoperei: "))
            data = input("Dati data si ora tranzactiei "
                         "(in format dd.mm.yyyy,hh:mm): ")
            data = datetime.strptime(data, "%d.%m.%Y,%H:%M")

            self.tranzactieService.modifica(
                id_tranzactie,
                id_masina,
                id_card,
                suma_piese,
                suma_manopera,
                data.strftime("%d.%m.%Y,%H:%M"))

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllTranzactii(self):
        for tranzactie in self.tranzactieService.get_all():
            print(tranzactie)

    def runGenerareMasini(self):
        try:
            n = int(input("Alegeti un numar de masini: "))
            self.masinaService.generareMasini(n)
            self.showAllMasini()
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiAfisareTranzactiiInInterval(self):
        try:
            a = float(input("Alegeti marginea intervalului inferioara "))
            b = float(input("Alegeti marginea intervalului superioara "))
            lista = self.tranzactieService.afisareTranzactiiInInterval(a, b)
            if lista:
                print(f"Tranzactiile cu suma cuprinsa intre {a}, {b} sunt ")
            else:
                print("Nu exista tranzactii cu suma in interval. ")
            for x in lista:
                print(x)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiCautareFullText(self):
        try:
            cuv = input("Alegeti un cuvant pentru a-l cauta: ")
            lista = self.tranzactieService.cautareFullText(cuv)
            for elem in lista:
                print(elem)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiAfisareMasiniDupaManopera(self):
        lista = self.tranzactieService.orodonareMasiniDupaManopera()
        for elem in lista:
            print(elem)

    def uiAfisareCarduriDupaReduceri(self):
        lista = self.tranzactieService.afisareCarduriDupaReduceri()
        for elem in lista:
            print(elem)

    def uiStergeDinIntervalZile(self):
        try:
            a = int(input("Dati ziua de la care sa se stearga: "))
            b = int(input("Dati ziua pana la care sa se stearga: "))
            if b < a:
                print("Zilele trebuie sa fie in ordine calendaristica ")
            else:
                self.tranzactieService.stergeDinIntervalZile(a, b)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiActualizareGarantie(self):
        self.masinaService.actualizareGarantie()

    def StergeInCascada(self):
        try:
            masina_sters = input("Dati id- ul masinii de sters: ")
            self.tranzactieService.stergeInCascada(masina_sters)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
