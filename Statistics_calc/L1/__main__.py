from klasy import *
from time import sleep

###################################################
# Menu główne programu liczącego                  #
###################################################


def main(what_implement=True):
    print("Program implementuje Fractions w celu uniknięcia błędów występujących na liczbach zmiennoprzecinkowych w pythonie.")
    print("Wyniki konwertowane są na wartości float dopiero po zakończeniu obliczeń dla ich dokładności.")
    init = {"1": szczegolowa, "2": wazona, "3": przedzialowa, "4": exit}
    while True:
        SCREEN_CLEAR(what_implement)
        what_implement = False

        print("1 - Szereg szczegółowy punktowy")
        print("2 - Szereg rozdzielczy punktowy")
        print("3 - Szereg rozdzielczy przedziałowy")
        print("4 - Wyjście")
        choice = input("Wybierz dla jakich danych chcesz wykonać obliczenia: ")
        if choice in init:
            if choice == '4':
                SCREEN_CLEAR()
                print("~"*37+"\n"+"# Zapraszam ponownie do obliczeń ;) #\n" + "~"*37)
            init.get(choice)()
            first_clean = True
        else:
            print("Wprowadż poprawną opcję")


###################################################
# Funkcje pomocnicze do walidacji danych          #
###################################################


def walidacja_ilosci_danych(wybrany_szereg, wprowadzanie):
    print(wybrany_szereg)
    while True:
        try:
            ile = int(input(wprowadzanie))
            if ile > 1:
                break
        except ValueError:
            SCREEN_CLEAR()
            print(wybrany_szereg)
            print("Wprowadź liczbę całkowitą, większą od 1!")
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


def szczegolowa():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################
    SCREEN_CLEAR()

    ile = walidacja_ilosci_danych("Wybrałeś obliczanie dla Szeregu szczegółowego punktowego.", "Wprowadź ilość elementów: ")

    dane = walidacja_calkowita_lub_ulamek(ile, liczebnosc=False)
    if dane == None:
        return None

    ###################################################
    # Inicjalizowanie klasy zdeklarowanymi elementami #
    ###################################################
    S = Szczegolowa(*dane)

    ###################################################
    # Wywoływanie metod klasy obliczającej            #
    ###################################################
    print("Arytmetyczna:", S.srednia_arytmetyczna())
    print("Geometryczna:", S.srednia_geometryczna())
    print("Harmoniczna:", S.srednia_harmoniczna())
    print("Potęgowa:", S.srednia_potegowa())
    print("Mediana:", S.mediana())
    print("Dominanta:", S.dominanta())
    print("Odchylenie:", S.odchylenie())
    print("Wspolczynnik odchylenia:", S.wspolczynnik())

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")


def wazona():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################
    SCREEN_CLEAR()

    ile = walidacja_ilosci_danych("Wybrałeś obliczanie dla Szeregu rozdzielczego punktowego.", "Wprowadź ilość elementów: ")

    dane = walidacja_calkowita_lub_ulamek(ile, liczebnosc=True)
    if dane == None:
        return None

    ###################################################
    # Inicjalizowanie klasy zdeklarowanymi elementami #
    ###################################################
    W = Wazona(*dane)

    ###################################################
    # Wywoływanie metod klasy obliczającej            #
    ###################################################
    print("Arytmetyczna:", W.srednia_arytmetyczna())
    print("Mediana:", W.mediana())

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")


def przedzialowa():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################
    SCREEN_CLEAR()

    #Ilość przedziałów
    ile = walidacja_ilosci_danych("Wybrałeś obliczanie dla Szeregu rozdzielczego przedziałowego.", "Wprowadź ilość przedziałów: ")

    #Początek przedziałów
    poczatek_przedzialu = walidacja_calkowita_przedzialowa("Wprowadź dolną wartość najniższego przedziału: ")
    if poczatek_przedzialu == None:
        return None

    #Rozmiar przedziałów
    rozmiar_przedzialu = walidacja_calkowita_przedzialowa("Wprowadź rozmiar przedziału: ")
    if rozmiar_przedzialu == None:
        return None

    #Liczebność przedziałów:
    print("Metoda wprowadzania: liczba całkowita")
    dane = {}
    dolny = poczatek_przedzialu
    gorny = poczatek_przedzialu+rozmiar_przedzialu
    while ile > len(dane):
        try:
            print("Przedział <{}, {}):".format(dolny, gorny))
            wejscie = int(input("Wprowadź liczebność przedziału: "))
            dane[(dolny, gorny)] = wejscie
            print(dane)
            dolny, gorny = gorny, gorny+rozmiar_przedzialu
        except ValueError:
            while True:
                print("Niepoprawne dane, chcesz kontynuować wprowadzanie?\n[t/n]:", end=" ")
                temp = input().lower()
                if temp=="t":
                    print("Metoda wprowadzania: liczba całkowita")
                    break
                elif temp =="n":
                    return None

    ###################################################
    # Inicjalizowanie klasy zdeklarowanymi elementami #
    ###################################################
    P = Przedzialowa(dane)

    ###################################################
    # Wywoływanie metod klasy obliczającej            #
    ###################################################
    print("Arytmetyczna:", P.srednia_arytmetyczna())
    print("Mediana:", P.mediana())
    print("Dominanta:", P.dominanta())
    print("Odchylenie:", P.odchylenie())

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")


if __name__ == "__main__":
    main()
