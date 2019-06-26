# /usr/bin/python3
from klasy import *
from funkcje_wprowadzania import *
from time import sleep

###################################################
# Menu główne programu liczącego                  #
###################################################


def main(what_implement=False):
    print("Program implementuje Fractions w celu uniknięcia błędów występujących na liczbach zmiennoprzecinkowych w pythonie.")
    print("Wyniki konwertowane są na wartości float dopiero po zakończeniu obliczeń dla ich dokładności.")
    init = {"1": zad1, "2": zad2, "3": zad3, "4": zad4, "5": exit}
    while True:
        SCREEN_CLEAR(what_implement)
        what_implement = True

        print("1 - Model pierwszy")
        print("2 - Model drugi")
        print("3 - Model pierwszy o nieznanym σ")
        print("4 - Model drugi o próbie >= 50")
        print("5 - Wyjście")
        choice = input("Wybierz dla jakich danych chcesz wykonać obliczenia: ")
        if choice in init:
            if choice == '5':
                SCREEN_CLEAR()
                print("~"*37+"\n"+"#{:^35}#\n".format("Zapraszam ponownie do obliczeń ^^") + "~"*37)
            init.get(choice)()
            first_clean = True
        else:
            print("Wprowadż poprawną opcję")

def zad1():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################

    #~ START Dane wprowadzane
    n = walidacja_ilosci_danych("Zadanie pierwsze.", "Podaj ilość danych: ")
    dane = walidacja_calkowita_lub_ulamek(n, False)
    #~ STOP Dane wprowadzane

    #~ START Dane testowe
    #~ n = 25
    #~ dane = [165 for _ in range(n)]
    #~ STOP Dane testowe

    S = Szczegolowa(*dane)
    srednia = S.srednia_arytmetyczna()
    odchylenie = walidacja_ilosci_danych("", "Podaj odchylenie: ", 0)
    ufnosc = Fraction(walidacja_ilosci_danych("", "Podaj poziom ufności wyrażony w ilości punktów procentowych: ", 0), 100)
    a = (1-ufnosc)
    jeden_minus_a_przez_dwa = float(1 - a/2)

    ###################################################
    # Obliczanie wyniku na podstawie danych           #
    ###################################################

    try:
        kwantyl = kwantyle_rozkladu_normalnego(jeden_minus_a_przez_dwa)
    except KeyError:
        print("Tabela, nie posiada kwantyla o poziomie ufności {}".format(ufnosc))
        sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
        input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")
        return
    wynik = (srednia-kwantyl*(odchylenie/n**0.5), srednia+kwantyl*(odchylenie/n**0.5))

    ###################################################
    # Wypisanie wyniku                                #
    ###################################################

    print(wynik)

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")

def zad2():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################

    #~ START Dane wprowadzane
    n = walidacja_ilosci_danych("Zadanie drugie.", "Podaj ilość danych 7, 8, 10, 11, 21 lub 26: ", dozwolone=(7, 8, 10, 11, 21, 26))
    dane = walidacja_calkowita_lub_ulamek(n, False)
    #~ STOP Dane wprowadzane

    #~ START Dane testowe
    #~ n = 10
    #~ dane = [60, 62, 65, 74, 70, 70, 80, 60, 60, 55]
    #~ STOP Dane testowe

    S = Szczegolowa(*dane)
    srednia = S.srednia_arytmetyczna()
    odchylenie = S.odchylenie()
    ufnosc = 1-Fraction(walidacja_ilosci_danych("", "Podaj poziom ufności wyrażony w ilości punktów procentowych: ", 0),100)

    ###################################################
    # Obliczanie wykniku na podstawie danych          #
    ###################################################

    try:
        kwantyl = kwantyle_rozkladu_studenta(n-1, float(1-ufnosc/2))
        if kwantyl == None:
            raise Exception
    except Exception:
        print("Tabela, nie posiada kwantyla o poziomie ufności {}".format(ufnosc))
        sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
        input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")
        return
    wynik = (srednia-kwantyl*(odchylenie/n**0.5), srednia+kwantyl*(odchylenie/n**0.5))

    ###################################################
    # Wypisanie wyniku                                #
    ###################################################

    print(wynik)

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")

def zad3():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################

    #~ START Dane wprowadzane
    n = walidacja_ilosci_danych("Zadanie trzecie.", "Podaj ilość danych 11 lub 21: ", dozwolone=(11, 21, 25))
    dane = walidacja_calkowita_lub_ulamek(n, False)
    S = Szczegolowa(*dane)
    odchylenie = S.odchylenie()
    odchylenie_kwadrat = odchylenie**2
    #~ STOP Dane wprowadzane

    #~ START Dane testowe
    #~ n = 25
    #~ odchylenie_kwadrat = 225
    #~ STOP Dane testowe

    ufnosc = Fraction(walidacja_ilosci_danych("", "Podaj poziom ufności wyrażony w ilości punktów procentowych: ", 0, dozwolone=range(100)),100)
    a = (1-ufnosc)
    a_przez_dwa = a/2
    jeden_minus_a_przez_dwa = 1 - a/2

    print(a_przez_dwa)
    print(jeden_minus_a_przez_dwa)

    ###################################################
    # Obliczanie wyniku na podstawie danych           #
    ###################################################

    try:
        kwantyl_1 = kwantyle_chi_kwadrat(n-1, float(a_przez_dwa))
        kwantyl_2 = kwantyle_chi_kwadrat(n-1, float(jeden_minus_a_przez_dwa))
        if not kwantyl_1 or not kwantyl_2:
            raise Exception 
    except Exception:
        print("Tabela, nie posiada kwantyla o poziomie ufności {} o stopniu {}".format(ufnosc, n-1))
        sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
        input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")
        return

    przedzial_kwadrat = ((n * odchylenie_kwadrat) / kwantyl_2, (n * odchylenie_kwadrat) / kwantyl_1)
    wynik = tuple((i**0.5 for i in przedzial_kwadrat))

    ###################################################
    # Wypisanie wyniku                                #
    ###################################################

    print(wynik)

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")

def zad4():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################

    #~ START Dane wprowadzane
    n = walidacja_ilosci_danych("Zadanie czwarte.", "Podaj ilość danych: ")
    dane = walidacja_calkowita_lub_ulamek(n, False)
    S = Szczegolowa(*dane)
    odchylenie = S.odchylenie()
    odchylenie_kwadrat = odchylenie**2
    #~ STOP Dane wprowadzane

    #~ START Dane testowe
    #~ n = 200
    #~ odchylenie = 10
    #~ STOP Dane testowe

    ufnosc = Fraction(walidacja_ilosci_danych("", "Podaj poziom ufności wyrażony w ilości punktów procentowych: ", 0, 100, dozwolone=(99, 95, 90)))
    a = (1-ufnosc)
    jeden_minus_a_przez_dwa = 1 - a/2

    ###################################################
    # Obliczanie wyniku na podstawie danych           #
    ###################################################

    try:
        kwantyl = kwantyle_rozkladu_normalnego(float(jeden_minus_a_przez_dwa))
        if not kwantyl:
            raise Exception 
    except Exception:
        print("Tabela, nie posiada kwantyla o poziomie ufności {} o stopniu {}".format(ufnosc, n-1))
        sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
        input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")
        return
        
    _2n = 2*n
    wynik = (odchylenie*(_2n**0.5))/(((_2n - 3)**0.5) + kwantyl), (odchylenie*(_2n**0.5))/((_2n - 3)**0.5 - kwantyl)

    ###################################################
    # Wypisanie wyniku                                #
    ###################################################

    print(wynik)

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
