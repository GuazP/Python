# /usr/bin/python3
from klasy import Szczegolowa

def main():
    dane = 10, 11, 15, 20, 10, 16, 23, 14, 23, 12
    a1 = 0.005
    a2 = 0.995
    n = 10

    s2 = Szczegolowa(*dane).odchylenie()
    print(s2)

    kwantyl_1 = 23.589
    kwantyl_2 = 1.735

    result_1 = n*s2/kwantyl_1
    result_2 = n*s2/kwantyl_2

    print(result_1**0.5)
    print(result_2**0.5)
    #~ Func


if __name__ == "__main__":
    main()
