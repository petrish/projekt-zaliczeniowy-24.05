from postacie.basic_skills import BASIC_SKILS
import random

class Bonie(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 400
        self.hp = 300
        self.regeneration_health = random.randint(50,100)
        self.visibility = 8
        self.speed = random.randint(5,15)
        self.zadawany_damage = random.randint(1,39)

    def spotkanie_B(self):
        print("==="*10)
        print("Umiejetnpsci Bonni'ego!!")
        print(super().podstawowe_skille())
        
