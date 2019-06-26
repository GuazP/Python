from klasy import *
from time import sleep


###################################################
# Funkcje pomocnicze do walidacji danych          #
###################################################


def walidacja_ilosci_danych(wybrany_szereg, wprowadzanie, mini=1, dozwolone=()):
    print(wybrany_szereg)
    while True:
        try:
            ile = int(input(wprowadzanie))
            if dozwolone and ile not in dozwolone:
                print("Wprowadź jedną z liczb `{}`:".format(", ".join(str(_) for _ in dozwolone)))
            elif ile > mini:
                break
            else:
                print("Wprowadź liczbę całkowitą, większą od 1!")
        except ValueError:
            SCREEN_CLEAR()
            print(wybrany_szereg)
            print("Wprowadź liczbę całkowitą, większą od 1!")
        except TypeError:
            SCREEN_CLEAR()
            print(wybrany_szereg)
    return ile

def walidacja_calkowita_lub_ulamek(ile, liczebnosc):
    dane = []
    if liczebnosc:
        metoda_wprowadzania = "Metoda wprowadzania: liczba całkowita<spacja>liczebność [lub licznik<spacja>mianownik<spacja>liczebność]"
    else:
        metoda_wprowadzania = "Metoda wprowadzania: liczba całkowita [lub licznik<spacja>mianownik]"

    print(metoda_wprowadzania)
    while ile > len(dane):
        try:
            wejscie = input("Wprowadź "+str(len(dane)+1)+" argument: ").split()
            if liczebnosc:
                if len(wejscie) == 2:
                    dane.append((Fraction(int(wejscie[0])), int(wejscie[1])))
                elif len(wejscie) == 3:
                    dane.append((Fraction(int(wejscie[0]), int(wejscie[1])), int(wejscie[2])))
                else:
                    raise ValueError
            else:
                if len(wejscie) == 1:
                    dane.append(Fraction(int(wejscie[0])))
                elif len(wejscie) == 2:
                    dane.append(Fraction(int(wejscie[0]), int(wejscie[1])))
                else:
                    raise ValueError

        except ValueError:
            while True:
                print("Niepoprawne dane, chcesz kontynuować wprowadzanie?\n[t/n]:", end=" ")
                temp = input().lower()
                if temp=="t":
                    print(metoda_wprowadzania)
                    break
                elif temp =="n":
                    return None
    return dane

def walidacja_calkowita_przedzialowa(komunikat):
    metoda_wprowadzania = "Metoda wprowadzania: liczba całkowita [lub licznik<spacja>mianownik]"
    print(metoda_wprowadzania)
    while True:
        try:
            wejscie = input(komunikat).split()
            if len(wejscie) == 1:
                dane = Fraction(int(wejscie[0]))
            elif len(wejscie) == 2:
                dane = Fraction(int(wejscie[0]), int(wejscie[1]))
            else:
                raise ValueError
            break
        except ValueError:
            while True:
                print("Niepoprawne dane, chcesz kontynuować wprowadzanie?\n[t/n]:", end=" ")
                temp = input().lower()
                if temp=="t":
                    print(metoda_wprowadzania)
                    break
                elif temp =="n":
                    return None
    return dane


###################################################
# Funkcje tworzące odpowiednie obiekty liczące    #
###################################################

def kwantyle_rozkladu_normalnego(p):
    kwantyle = {0.900: 1.28,
                0.950: 1.64,
                0.975: 1.96,
                0.990: 2.33,
                0.995: 2.58}
    return kwantyle.get(p)

def kwantyle_rozkladu_studenta(k, p):
    kwantyle = {6: {0.900: 1.440,
                    0.950: 1.943,
                    0.975: 2.447,
                    0.990: 3.143,
                    0.995: 3.707},
                8: {0.900: 1.397,
                    0.950: 1.859,
                    0.975: 2.306,
                    0.990: 2.897,
                    0.995: 3.355},
                9: {0.900: 1.383,
                     0.950: 1.833,
                     0.975: 2.262,
                     0.990: 2.821,
                     0.995: 3.250},
                10: {0.900: 1.372,
                     0.950: 1.812,
                     0.975: 2.228,
                     0.990: 2.764,
                     0.995: 3.169},
                20: {0.900: 1.325,
                     0.950: 1.725,
                     0.975: 2.086,
                     0.990: 2.528,
                     0.995: 2.845},
                25: {0.900: 1.316,
                     0.950: 1.708,
                     0.975: 2.060,
                     0.990: 2.485,
                     0.995: 2.787}}
    return kwantyle.get(k).get(p)

def kwantyle_chi_kwadrat(k, p):
    kwantyle = {10: {0.005: 2.603,
                     0.010: 3.053,
                     0.025: 3.816,
                     0.050: 4.575,
                     0.950: 19.675,
                     0.975: 21.920,
                     0.990: 24.725,
                     0.995: 26.757},
                20: {0.005: 8.034,
                     0.010: 8.897,
                     0.025: 10.283,
                     0.050: 11.591,
                     0.950: 32.671,
                     0.975: 35.479,
                     0.990: 38.932,
                     0.995: 41.401},
                24: {0.005: 9.886,
                     0.010: 10.856,
                     0.025: 12.401,
                     0.050: 13.848,
                     0.95: 36.415,
                     0.975: 39.364,
                     0.990: 42.980,
                     0.995: 45.559}}
    return kwantyle.get(k).get(p)

if __name__ == "__main__":
    exit("Error, this file contains only function for another main program.")
