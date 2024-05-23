from postacie.freddy import Freddy
from postacie.bonie import Bonie
from postacie.chica import Chicka
from postacie.foxy import Foxy
from postacie.guard import Guard
from akcje.swiatla import Swiatla
from akcje.kamery import Kamery
from akcje.drzwi import Drzwi
import random
import time


#-------------------------------------


# def czy_drzwi_otwarte(l_drzwi, p_drzwi):
#     if l_drzwi and p_drzwi:
#         print("Obydwa drzwi są otwarte.")
#         return True
#     elif l_drzwi:
#         print("Lewe drzwi są otwarte.")
#         return True
#     elif p_drzwi:
#         print("Prawe drzwi są otwarte.")
#         return True
#     else:
#         print("Oba drzwi są zamknięte.")
#         return False



#-------------------------------------

def display_time(hour):
    print(f"========================================================== {hour} ==========================================================")

def main_game():
    #------------------------------
    l_drzwi = Drzwi("Lewe drzwi")
    l_swiatlo = Swiatla()
    p_drzwi = Drzwi("Prawe drzwi")
    p_swiatlo = Swiatla()
    #------------------------------
    bohater = Guard()
    print("============== FIVE NIGHTS AT FREDDY'S ==============")
    print("ZASADY + TIPY --> a")
    print("SKIP --> dowony klawisz")
    inp = input().lower()
    if inp == "a":
        print("==="*10)
        print("Zasady są proste!!! ")
        print("*"*5)
        print("Musisz przetrwać do 6 AM nie dając się pokonać animatronikom, które będą próbowały cię zabić")
        print("*"*5)
        print("Do pomocy możesz używać przedmiotów, które będą podane niżej")
        print("*"*5)
        print("Gdy zginiesz chociaż raz, przegrywasz cały challenge, lecz jeśli uda ci się przetrwać do 6 AM, wygrywasz!")
        print("*"*5)
        print("Gdy zamykasz drzwi gdy ktos cie akatuje (po zapaleniu swiatla) to automatycznie sie otwieraja")
        print("*"*5)
        print("POWODZENIA!!!")
        print("==="*10)
        print("=============== WITAJ W ROZGRYWCE =============== ")

    
    
    hours = ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
    for hour in hours:
        display_time(hour)
        start_time = time.time()
        while time.time() - start_time < 10:   
            if not bohater.czy_zyje():
                print("Zostałeś pokonany! Gra skończona.")
                return
            
            print("==="*10)
            print("A - zamknij lewe drzwi")
            print("B - otwórz lewe drzwi")
            print("C - zapal lewe światło")
            print("D - zgaś lewe światło")
            print("**"*10)
            print("E - zamknij prawe drzwi")
            print("F - otwórz prawe drzwi")
            print("G - zapal prawe światło")
            print("H - zgaś prawe światło")
            print("**"*10)
            print("I - otwórz monitor")
            print("K - informacje o bohaterach")           
            ina = input("Co chcesz zrobić: ").lower()
            
            if ina == "a":
                l_drzwi.zamknij()
            elif ina == "b":
                l_drzwi.otworz()
            elif ina == "c":
                animatroniki = ["Freddy", "Bonie", "Chicka", "Foxy", "NIC"]
                l_swiatlo.wlacz()
                los = random.choice(animatroniki)
                print("==="*10)
                print(f"Widzisz {los}")
                print("==="*10)
                if los in (animatroniki[0], animatroniki[1], animatroniki[2], animatroniki[3]):
                    ss = input("Masz chwilę, żeby zamknąć drzwi... (Wciśnij 'a' aby zamknąć): ").lower()
                    if ss == "a":
                        print("Gratulacje, zamknąłeś drzwi.")
                    else:
                        print(f"Nie zamknąłeś drzwi. PRZEGRAŁEŚ!!! Zabił/a cię {los}.")
                        bohater.smierc()
                        break
            elif ina == "d":
                l_swiatlo.wylacz()
            elif ina == "e":
                p_drzwi.zamknij()
            elif ina == "f":
                p_drzwi.otworz()
            elif ina == "g":
                p_swiatlo.wlacz()
                losk = random.choice(animatroniki)
                print("==="*10)
                print(f"Widzisz {los}")
                print("==="*10)
                if losk in (animatroniki[0], animatroniki[1], animatroniki[2], animatroniki[3]):
                    sss = input("Masz chwilę, żeby zamknąć drzwi... (Wciśnij 'e' aby zamknąć): ").lower()
                    if sss == "e":
                        print("Gratulacje, zamknąłeś drzwi.")
                    else:
                        print(f"Nie zamknąłeś drzwi. PRZEGRAŁEŚ!!! Zabił/a cię {los}.")
                        bohater.smierc()
                        break
            elif ina == "h":
                p_swiatlo.wylacz()
            elif ina == "k":
                print("==="*10)
                print("a - Freddy")
                print("b - Bonnie")
                print("c - Chicka")
                print("d - Foxy")
                print("g - guard")
                igs = input("O kim chcesz informacje: ")
                print("==="*10)
                
                if igs == "a":
                    f = Freddy()
                    f.spotkanie()
                elif igs == "b":
                    b = Bonie()
                    b.spotkanie_B()
                elif igs == "c":
                    c = Chicka()
                    c.spotkanie_C()
                elif igs == "d":
                    f = Foxy()
                    f.spotkanie_F()
                elif igs == "g":
                    bohater.info_o_guard()
                else:
                    print("Brak komendy")
                print("==="*10)

            elif ina == "i":
                print("=================== OTWORZYŁEŚ MONITOR ===================")
                while True:
                    print("a - kamera scena")
                    print("b - kamera jadalnia")
                    print("c - kamera pokoju serwisowego")
                    print("d - kamera toalety")
                    print("e - kamera kuchnia")
                    print("f - kamera piracka zatoka")
                    print("g - kamera l.korytarz")
                    print("h - kamera p.korytarz")
                    print("**"*10)
                    print("j - zamknij monitor")
                    ins = input("Wybierz opcję: ").lower()
                
                    if ins == "a":
                        k_stage = Kamery("Scena", True)
                        k_stage.sprawdz()
                    elif ins == "b":
                        k_daning = Kamery("Jadalnia", True)
                        k_daning.sprawdz()
                    elif ins == "c":
                        k_parts = Kamery("Pokój serwisowy", True)
                        k_parts.sprawdz()
                    elif ins == "d":
                        k_toilets = Kamery("Toalety", True)
                        k_toilets.sprawdz()
                    elif ins == "e":
                        k_kitchen = Kamery("Kuchnia", False)
                        k_kitchen.sprawdz()
                    elif ins == "f":
                        k_pirates_cove = Kamery("Piracka zatoka", True)
                        k_pirates_cove.sprawdz()
                    elif ins == "g":
                        k_l_hall = Kamery("Lewy korytarz", True)
                        k_l_hall.sprawdz()
                    elif ins == "h":
                        k_r_hall = Kamery("Prawy korytarz", True)
                        k_r_hall.sprawdz()
                    elif ins == "j":
                        print("=================== Wyłączyłeś monitor ===================")
                        break 
                    else:
                        print("==="*10)
                        print("Nie ma takiej komendy")
                        print("==="*10)
            else:
                print("==="*10)
                print("Nie ma takiej komendy")
                print("==="*10)
        if hour == "5 AM":
            print("==="*10)
            print("Przetrwałeś do 6 AM i wygrałeś grę! GRATUACJE!!!")
            print("==="*10)
            break





if __name__ == '__main__':
    main_game()

print("DZIEKI ZA GRE (bardzo dobrze sie bawilem tworzac to :)")