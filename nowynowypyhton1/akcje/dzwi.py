class Drzwi:
    def __init__(self,nazwa) -> None:
        self.nazwa = nazwa
        self.energia_drzwi = 100
        self.koszt_drzwi = 5
        self.otwarte = True

    def zamknij(self):
        print("==="* 10)
        if self.energia_drzwi > self.koszt_drzwi:
            self.energia_drzwi -= self.koszt_drzwi
            print(f'Koszt zamkniencia drzwi wynosi 5 i zostalo ci jeszcze {self.energia_drzwi} energii drzwi!!')
            print("==="* 10)
#-------------------------------
            if self.otwarte == True:
                print(f'{self.nazwa} zostaly zamkniente')
                self.otwarte = False

            else:
                print(f'{self.nazwa} sa juz zamkniente')
            print("==="* 10)
#-------------------------------
        else:
            print("==="* 10)
            print("Drzwi nie mozna juz zamknac (BRAK ENERGII)")
            print("==="* 10)

    def otworz(self):
        print("==="* 10)
        if self.otwarte == False:
            print(f'{self.nazwa} zostaly otwarte')
            self.otwarte = True
        else:
            print(f'{self.nazwa} sa juz otwarte')
        print("==="* 10)




        