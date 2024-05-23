from postacie.basic_skills import BASIC_SKILS
import random

class Freddy(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 500
        self.hp = 400
        self.visibility = 10
        self.speed = 10
        self.zadawany_damage = random.randint(1, 60)
        self.regeneration_health = random.randint(20,60)

    def spotkanie(self):
        print("==="*10)
        print("Umiejetnosci Freddy'ego")
        print(super().podstawowe_skille())


