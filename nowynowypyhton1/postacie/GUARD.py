from basic import BASIC_SKILS
import random

class Guard(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 100
        self.hp = 100
        self.regeneration_health = 30
        self.visibility = 10
        self.speed = 5
        self.zadawany_damage = random.randint(100,200)

    def info_o_guard(self):
        print("==="*10)
        print(f"Aktualnie posiadasz {self.hp} hp!!")
        print(f'Widzisz na odeglosc {self.visibility} metrow!!')
        print(f'Poruszasz sie z zawrotno predkoscio {self.speed} METORW NA SEKUNDE!!')
        print('Zadajesz zaleznie od formy od 10 do nawet 100 obrazen :)')
        print("==="*10)


    def walka(self):
        while True:
            self.info_o_guard()
            print(" a - Stajesz do walki!!")
            print(" b - ucieczka")
            print(" c - leczenie")
            inp = input("Co chcesz zrobic: ").lower()
            if inp == "a":
                print(f'Zadaes {self.zadawany_damage}!')
                return self.zadawany_damage

            elif inp == "b":
                print("Ucieczka ...")
                szansa_ucieczki = random.randint(1,10)
                if szansa_ucieczki > 6:
                    print("Udalo sie uciec!!")
                    break
                else:
                    print("Nie udalo sie uciec wlaczysz dalej")
                    return self.zadawany_damage
            elif inp == "c":
                return self.regeneration

            else:
                print("Nie ma takiej komendy")


        



                    