#! /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Maciej 'Guaz' Pawłowski"

if __name__ == "__main__":
    import sys
    sys.path.insert(0, 'Controller')
    from Controller import Controller
    c = Controller()
    c.mainmenu_controller()
