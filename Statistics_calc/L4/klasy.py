import functools
from copy import deepcopy
from math import floor
from itertools import takewhile
from fractions import Fraction

class Szczegolowa():
    def __init__(self, *args):
        if len(args) > 1:
            self._data = tuple([v for v in args])
            self._dsize = len(self._data)
        else:
            raise TypeError("Na podstawie jednej zmiennej nie można wyliczyć żadnej średniej.")


    def __str__(self):
        return "Szereg punktowy szczegółowy"


    def set_new_data(self, *args):
        self.__init__(self, *args)

    @property
    def data(self):
        return self._data

    @property
    def dsize(self):
        return self._dsize

    def srednia_arytmetyczna(self):
        return float(sum(self.data)/self.dsize)

    def srednia_geometryczna(self):
        return float(functools.reduce(lambda x,y: x*y, self.data)**(1/self.dsize))

    def srednia_harmoniczna(self):
        return float(len(self._data)/sum([1/i for i in self.data]))

    def srednia_potegowa(self, r=2):
        return float((sum([i**r for i in self.data]) / len(self.data))**(1/r))

    def mediana(self):
        sorted_ = list(deepcopy(self.data))
        sorted_.sort()
        mid = floor(self.dsize/2)
        if self.dsize%2:
            return float((sorted_[mid]+sorted_[mid+1])/2)
        else:
            return float(sorted_[mid])

    def dominanta(self): #To fix, can return multiple dominants...
        D = {self.data.count(k) : k for k in self.data}
        return float(D[max(D)])

    def odchylenie(self):
        return float(((sum([i**2 for i in self.data])/self.dsize-self.srednia_arytmetyczna()**2))**0.5)

    def wspolczynnik(self):
        return str(float(self.odchylenie() / self.srednia_arytmetyczna() * 100))+"%"

def SCREEN_CLEAR(clear=True):
    if clear:
        print("\033[H\033[J", end="")


if __debug__ and __name__ == "__main__":
    dane = [[2,3,4,2,4,4,3,2,5,5,6,1,2,1,3,4],
        [1,5,4,6,2,3,4,5,1,4,4,3,5,2,4]]
    #~ dane = [(1400, 6), (1800, 9), (2200, 2), (2700, 13)]
    #~ dane = {(100,200): 15, (200,300): 26, (300,400): 8, (400,500): 20,\
            #~ (500,600): 21, (600,700): 10}
    #~ dane = {(1200,1400): 20, (1400,1600): 10, (1600,1800): 20, (1800,2000): 30,\
            #~ (2000,2200): 20}
    if dane:
        for i in dane:
            S = Szczegolowa(*i)
            print("Arytmetyczna:", S.srednia_arytmetyczna()) #Wszystkie
            print("Geometryczna:", S.srednia_geometryczna()) #Szczegółowa
            print("Harmoniczna:", S.srednia_harmoniczna()) #Szczegółowa
            print("Potęgowa:", S.srednia_potegowa()) #Szczegółowa
            print("Mediana:", S.mediana()) #Wszystkie
            print("Dominanta:", S.dominanta()) #Szczegółowa i Przedziałowa
            print("Odchylenie:", S.odchylenie()) #Szczegółowa i Przedziałowa
            print("Wspolczynnik odchylenia:", S.wspolczynnik()) #Szczegółowa
            print()
            pass
        print(len(dane))
