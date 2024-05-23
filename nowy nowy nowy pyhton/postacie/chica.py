from postacie.basic_skills import BASIC_SKILS
import random

class Chicka(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 350
        self.hp = 250
        self.regeneration_health = random.randint(50,100)
        self.visibility = 9
        self.speed = random.randint(8,12)
        self.zadawany_damage = random.randint(20,60)

    def spotkanie_C(self):
        print("==="*10)
        print("Umiejetnosci Chicke!!")
        print(super().podstawowe_skille())