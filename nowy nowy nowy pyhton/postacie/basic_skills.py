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
        return self.alive
    
    def smierc(self):
        self.alive = False
        print("Zostałeś pokonany! Gra skończona.")

    def regeneration(self):
        if self.hp < self.max_health:
            self.hp = min(self.max_health, self.hp + self.regeneration_health)
        else:
            print(f"Zdrowie jest na maksymalnym poziomie {self.max_health}")
    
    def utrata_hp(self, damage:int):
        self.hp -= damage



    def podstawowe_skille(self):
        print("=="*20)
        print(f'Animatronik posiada jeszcze {self.hp} zycia')
        print(f'Animatronik widzi na {self.visibility} metrow')
        print(f'Animatronik porusza sie z zawrotna predkoscia rowna {self.speed}')
        print(f'Aktualnie Animatronik zadaje obrazenia w wysokosci {self.zadawany_damage}')
        print("=="*20)

    def zadawany_damage_1(self):
        if self.hp - self.zadawany_damage > 0:
            self.hp -= self.zadawany_damage
            print(f"Stracona ilosc zycia wynosi {self.zadawany_damage} hp i pozostalo jeszcze {self.hp} hp")
        else:
            self.hp = 0
            print(f'Zadawane obrazenia pozbawily zycia (OSOBE) zadano {self.zadawany_damage} hp')
