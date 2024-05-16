class BASIC_SKILS:
    def __init__(self) -> None:
        self.alive = True
        self.max_health = 0
        self.hp = 0
        self.regeneration_health = 0
        self.visibility = 0
        self.speed = 0
        self.zadawany_damage = 0


    def czy_zyje(self):
        return self.hp > 0

    
    def regeneration(self):
        if self.hp + self.regeneration_health > self.max_health:
            self.hp = self.max_health
        else:
            self.hp += self.regeneration_health

    def utrata_hp(self):
        self.hp -= self.zadawany_damage

    
    def maksymalny_regeneracja(self):
        if self.hp == self.max_health:
            print("Przeciwnik uleczyl sie do MAX !!!")


    def podstawowe_skille(self):
        print("=="*20)
        print(f'Przeciwinik posiada jeszcze {self.hp} zycia')
        print(f'Przeciwnik widzi na {self.visibility} metrow')
        print(f'Przeciwnik porusza sie z zawrota prendkoscio rowno {self.speed}')
        print(f'Aktualnie przeciwnik zadaj obrazenia w wyskokosci {self.zadawany_damage}')
        print("=="*20)

    def zadawany_damage1(self):
        if self.hp - self.zadawany_damage > 0:
            self.hp == self.hp - self.zadawany_damage
            print(f"Straciles znaczno ilosc zycia rowno{self.zadawany_damage} hp")
        else:
            print(f'Zadawane obrazenia pozbawily cie zycia GAME OVER!!! zadano ci {self.zadawany_damage} hp')

    
            





        