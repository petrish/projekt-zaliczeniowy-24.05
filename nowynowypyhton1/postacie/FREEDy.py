from basic import BASIC_SKILS
import random

class Freddy(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 500
        self.hp = 400
        self.visibility = 10
        self.speed = 10
        self.zadawany_damage = random.randint(1, 60)
        self.regeneration_health = self.regeneration

    def spotkanie(self):
        print("==="*10)
        print("Spotkałeś Freddy'ego")
        print("Podstawowe umiejętności:")
        print(super().podstawowe_skille())
        return self.zadawany_damage


