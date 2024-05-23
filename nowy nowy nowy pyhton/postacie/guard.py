from postacie.basic_skills import BASIC_SKILS
import random

class Guard(BASIC_SKILS):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 100
        self.hp = 100
        self.regeneration_health = 30
        self.visibility = 10
        self.speed = 5
        self.zadawany_damage = random.randint(100, 200)

    def info_o_guard(self):
        print("=" * 30)
        print(f"Aktualnie posiadasz {self.hp} HP!")
        print(f'Widzisz na odległość {self.visibility} metrów!')
        print(f'Poruszasz się z zawrotną prędkością {self.speed} METRÓW NA SEKUNDĘ!')
        print('Zadajesz zależnie od formy od 10 do nawet 100 obrażeń :)')
        print("=" * 30)
