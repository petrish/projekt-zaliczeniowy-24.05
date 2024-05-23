import random

class Kamery:
    def __init__(self, nazwa, dzialanie):
        self.nazwa = nazwa
        self.dzialanie = dzialanie
        self.energia_kamer = 100
        self.koszt_uzycia = 0
        self.ilosc_animatronikow =  random.randint(0, 4)
        self.imiona_animatronikow = ["Freddy", "Bonnie", "Chica", "Foxy"]

    def sprawdz(self):
                if self.energia_kamer > self.koszt_uzycia:
                    self.energia_kamer -= self.koszt_uzycia
                    print("==="* 10)
                    print("Kamery sa nieskonczonego uzytku nie wymagaja energii")
#------------------------------------------
                    if self.dzialanie:
                        print("==="* 10)
                        print(f'Na kamerze {self.nazwa} widzisz {self.ilosc_animatronikow} animatronika/i i jest/są to:')
                        print
                        print("==="* 10)
                        if self.ilosc_animatronikow == 0:
                            print("Brak animatroników.")
                        elif self.ilosc_animatronikow == 1:
                            print(self.imiona_animatronikow[0])
                        else:
                            losowe_animatroniki = random.sample(self.imiona_animatronikow, self.ilosc_animatronikow)
                            for animatronik in losowe_animatroniki:
                                print(animatronik)
                    else:
                        print("KAMERA NIE DZIALA")
                        print("BRAK OBRAZU [ERROR]")  
                    print("==="* 10)
#------------------------------------------               



