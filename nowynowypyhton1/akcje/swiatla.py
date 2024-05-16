class Swiatla:
    def __init__(self) -> None:
        self.wlaczone = False
        self.energia_swiatla = 100
        self.koszt_swiatla = 3

    def wlacz(self):
        print("==="*10)
        if self.energia_swiatla > self.koszt_swiatla:
            self.energia_swiatla -= self.koszt_swiatla
            print(f'Koszt wlaczenia swiatla wynosi 3 i pozostalo jeszcze {self.energia_swiatla} energii swiatla!!')
#------------------------------
            if self.wlaczone == False:
                print("==="*10)
                print("Swiatlo zostalo wlaczone")
                self.wlaczone = True
            else:
                print("Swiatlo jest juz wlaczone")
            print("==="*10)
#--------------------------------
        else:
            print("==="*10)
            print("Swiatla nie dzialaja (BRAK ENERGII)")
            print("==="*10)

    def wylacz(self):
        if self.wlaczone == True:
            print("==="*10)
            print("Swiatlo zostalo wylaczone")
            self.wlaczone = False
        else:
            print("Swiatlo jest juz wylaczone")
        print("==="*10)
