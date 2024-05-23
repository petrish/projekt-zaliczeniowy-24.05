from postacie.basic_skills import BASIC_SKILS
from akcje.kamery import Kamery
import random

class Foxy(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 250
        self.hp = 150
        self.regeneration_health = random.randint(50,100)
        self.visibility = 10
        self.speed = 20
        self.zadawany_damage = random.randint(50,60)

    def spotkanie_F(self):
        print("==="*10)
        print("Umiejetnosci Foxi'ego!!")
        print(super().podstawowe_skille())
    
