# /usr/bin/python3
from klasy import *
from funkcje_wprowadzania import *

###################################################
# Menu główne programu liczącego                  #
###################################################


def main(what_implement=True):
    print("Program implementuje Fractions w celu uniknięcia błędów występujących na liczbach zmiennoprzecinkowych w pythonie.")
    print("Wyniki konwertowane są na wartości float dopiero po zakończeniu obliczeń dla ich dokładności.")
    init = {"1": szczegolowa, "2": exit}
    while True:
        SCREEN_CLEAR(what_implement)
        what_implement = False

        print("1 - Szereg szczegółowy punktowy")
        print("2 - Wyjście")
        choice = input("Wybierz dla jakich danych chcesz wykonać obliczenia: ")
        if choice in init:
            if choice == '2':
                SCREEN_CLEAR()
                print("~"*37+"\n"+"# Zapraszam ponownie do obliczeń ;) #\n" + "~"*37)
            init.get(choice)()
            first_clean = True
        else:
            print("Wprowadż poprawną opcję")

def szczegolowa():
    ###################################################
    # Walidacja i wprowadzanie danych                 #
    ###################################################
    SCREEN_CLEAR()

    n = walidacja_ilosci_danych("Wybrałeś obliczanie dla Szeregu szczegółowego punktowego.", "Wprowadź ilość elementów: ")
    print("Wprowadź dane tabeli x:")
    x = walidacja_calkowita_lub_ulamek(n, liczebnosc=False)
    if x == None:
        return None

    print("Wprowadź dane tabeli y:")
    y = walidacja_calkowita_lub_ulamek(n, liczebnosc=False)
    if y == None:
        return None

    ###################################################
    # Wprowadzanie danych w kod do programu           #
    ###################################################
    #~ n = 4
    #~ x = [Fraction(800), Fraction(700), Fraction(600), Fraction(500)]
    #~ y = [Fraction(200), Fraction(400), Fraction(500), Fraction(600)]

    ###################################################
    # Inicjalizowanie klasy zdeklarowanymi elementami #
    ###################################################

    Sx = Szczegolowa(*x).odchylenie()
    Sy = Szczegolowa(*y).odchylenie()

    ###################################################
    # Sumy pomocnicze do obliczeń                     #
    ###################################################

    sum_x, sum_y, sum_xy, sum_x2 = przedstaw_dane_i_oblicz_sumy(x, y)

    ###################################################
    # Wywoływanie metod klasy obliczającej            #
    ###################################################
    print("Dane:")
    print("Sx {:10} | Sy {:10}".format(Sx,Sy))
    print("Współczynnik korelacji:")
    print("r = (1/{} * {} - {}*{}) / ({}*{})".format(n, sum_xy, sum_x/n, sum_y/n, Sx, Sy))
    r = ((1 / n * sum_xy) - ((sum_x / n) * (sum_y / n))) / (Sx * Sy)
    print("r =", r)
    funkcja = Funkcja_Prostej(*wyznacz_prosta_regresji_liniowej(n, sum_xy, sum_x, sum_y, sum_x2))
    print(funkcja)

    ###################################################
    # Wywoływanie metod klasy obliczającej            #
    ###################################################
    while True:
        try:
            print("Wprowadź coś poza liczbą jeśli chcesz zakończyć testowanie.")
            print("Dla zadanego x:", funkcja.oblicz_dla(float(input("Podstaw za x z regresji liniowej:"))))
        except ValueError:
            break

    ###################################################
    # Wyjście do menu głównego                        #
    ###################################################
    sleep(0.5) #Zabezpieczenie przed nieumyślnym podwójnym kliknięciem entera
    input("Zatwierdź enterem aby wyczyścić ekran i powrócić do menu głównego.")

def przedstaw_dane_i_oblicz_sumy(x, y):
    print("{:10} | {:10} | {:10} | {:10}".format("Xi", "Yi", "XiYi", "Xi**2"))
    suma_kol1 = 0
    suma_kol2 = 0
    suma_kol3 = 0
    suma_kol4 = 0
    for xi, yi in zip(x,y):
        try:
            print("{:10} | {:10} | {:10} | {:10}".format(xi, yi, xi*yi, xi**2))
        except TypeError as e:
            print("{:10} | {:10} | {:10} | {:10}".format(float(xi), float(yi), float(xi*yi), float(xi)**2))
        suma_kol1 += xi
        suma_kol2 += yi
        suma_kol3 += xi*yi
        suma_kol4 += xi**2
    print("-"*49)
    try:
        print("{:10} | {:10} | {:10} | {:10}".format(suma_kol1, suma_kol2, suma_kol3, suma_kol4))
    except TypeError as e:
        print("{:10} | {:10} | {:10} | {:10}".format(float(suma_kol1), float(suma_kol2), float(suma_kol3), float(suma_kol4)))
    return suma_kol1, suma_kol2, suma_kol3, suma_kol4

def wyznacz_prosta_regresji_liniowej(n, sum_xiyi, sum_xi, sum_yi, sum_xi2):
    print("a = ({0} * {1} - {2} * {3} )/ ({0} * {4} - {2}**2)".format(n, sum_xiyi, sum_xi, sum_yi, sum_xi2))
    print("a = ({0} * {1} - {2} * {3} )/ ({0} * {4} - {5})".format(n, sum_xiyi, sum_xi, sum_yi, sum_xi2, sum_xi**2))
    print("a = ({0} - {1}) / {2}".format(n*sum_xiyi, sum_xi*sum_yi, n*sum_xi2 - sum_xi**2))
    a = (n * sum_xiyi - sum_xi * sum_yi) / (n*sum_xi2 - (sum_xi)**2)
    print("a =", a)
    print("b = ({0} - {1}) / {2}".format(sum_yi/n, a, sum_xi/n))
    b = (sum_yi/n) - a * (sum_xi/n)
    print("b =", b)
    return a, b


if __name__ == "__main__":
    main()


    #~ >>> ((sum([1500**2, 2000**2, 2400**2, 3000**2, 4000**2, 5000**2])/6) - 2983**2)**0.5
#~ 1198.6287999209765
#~ >>> ((sum([100**2, 300**2, 500**2, 800**2, 1200**2, 1500**2])/6) - (4400/6)**2)**0.5
#~ 492.1607686744466
