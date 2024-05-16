from postacie.FREEDy import Freddy
from postacie.BONNIE import Bonie
from postacie.CHICKA import Chicka
from postacie.FOXY import Foxy
from postacie.GUARD import Guard
import random

#-------------------------------------
def walka_1(postac:Guard):
    przeciwnik = random.randint(1,4)
    if przeciwnik == 1:
        print("==="*10)
        print("Walczysz z Freddy'm")
        przeciwnik = Freddy()
        przeciwnik.regeneration()
        postac.regeneration()
        while postac.alive() and przeciwnik.alive():
            postac.utrata_hp(przeciwnik.spotkanie_Fr())
            przeciwnik.utrata_hp(postac.walka())
        if not (postac.alive()):
            print("Zostales pokonanay GAME OVER!!! PRZEGRALES :( ")
            return None
    elif przeciwnik == 2:
        print("==="*10)
        print("Walczysz z Bonnie'm")
        przeciwnik = Bonie()
        przeciwnik.regeneration()
        postac.regeneration()
        while postac.alive() and przeciwnik.alive():
            postac.utrata_hp(przeciwnik.spotkanie_B())
            przeciwnik.utrata_hp(postac.walka())
        if not (postac.alive()):
            print("Zostales pokonanay GAME OVER!!! PRZEGRALES :( ")
            return None
    elif przeciwnik == 3:
        print("==="*10)
        print("Walczysz z Chick'om")
        przeciwnik = Chicka()
        przeciwnik.regeneration()
        postac.regeneration()
        while postac.alive() and przeciwnik.alive():
            postac.utrata_hp(przeciwnik.spotkanie_C())
            przeciwnik.utrata_hp(postac.walka())
        if not (postac.alive()):
            print("Zostales pokonanay GAME OVER!!! PRZEGRALES :( ")
            return None
    elif przeciwnik == 4:
        print("==="*10)
        print("Walczysz z Foxy'm")
        przeciwnik = Foxy()
        przeciwnik.regeneration()
        postac.regeneration()
        while postac.alive() and przeciwnik.alive():
            postac.utrata_hp(przeciwnik.spotkanie_F())
            przeciwnik.utrata_hp(postac.walka())
        if not (postac.alive()):
            print("Zostales pokonanay GAME OVER!!! PRZEGRALES :( ")
            return None
        
        
walka_1()
