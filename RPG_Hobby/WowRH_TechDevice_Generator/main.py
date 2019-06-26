#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py

from Device import Device
from func import TECH_name, GM_modifier, SW, FD, TS, TS_recap, MR


def changing_options(device):
    menu_selection = {
        k: v
        for k, v in zip("1234567",
                        [TECH_name, GM_modifier, SW, FD, TS, TS_recap, MR])
    }
    print("""Wybierz opcję, co chcesz zmienić w wynalazku!
1 - Zmienić nazwę
2 - Zmienić GM modifier
3 - Zmienić SW
4 - Zmienić FD
5 - Dodać TS
6 - Zresetować i zastąpić TS
7 - Zmienić MR""")
    choice = input("Twój wybór: ")
    try:
        if int(choice) in range(1, 8):
            menu_selection.get(choice)(device)
            device.calculating()
            device.print_calculation()
    except ValueError:
        print("Niepoprawny wybór!\n")


def main(args):
    print("Witam w kreatorze wynalazków!")
    device = Device()

    TECH_name(device)
    GM_modifier(device)
    SW(device)
    FD(device)
    TS(device)
    MR(device)

    device.calculating()
    device.print_calculation()

    print("\nObliczenia do wynalazku gotowe!")

    while input(
            "\nWprowadź jakąkolwiek wartość jeśli chcesz coś zmienić w wynalazku, bądź pozostaw puste i kliknij enter aby zakończyć program: "
    ):
        changing_options(device)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
