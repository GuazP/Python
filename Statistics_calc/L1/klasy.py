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
        return sum(self.data)/self.dsize

    def srednia_geometryczna(self):
        return functools.reduce(lambda x,y: x*y, self.data)**(1/self.dsize)

    def srednia_harmoniczna(self):
        return len(self._data)/sum([1/i for i in self.data])

    def srednia_potegowa(self, r=2):
        return (sum([i**r for i in self.data]) / len(self.data))**(1/r)

    def mediana(self):
        sorted_ = list(deepcopy(self.data))
        sorted_.sort()
        mid = floor(self.dsize/2)
        if self.dsize%2:
            return (sorted_[mid]+sorted_[mid+1])/2
        else:
            return sorted_[mid]

    def dominanta(self): #To fix, can return multiple dominants...
        D = {self.data.count(k) : k for k in self.data}
        return D[max(D)]

    def odchylenie(self):
        return ((sum([i**2 for i in self.data])/self.dsize-self.srednia_arytmetyczna()**2))**0.5

    def wspolczynnik(self):
        return str(self.odchylenie() / self.srednia_arytmetyczna() * 100)+"%"

class Wazona():
    def __init__(self, *args):
        try:
            if len(args) > 1:

                self._data = tuple((k, v) for k, v in args)
                self._dsize = sum(int(v) for k, v in self._data)
            else:
                raise TypeError("Na podstawie jednej zmiennej nie można wyliczyć żadnej średniej.")
                del(self)
        except ValueError as e:
            print("Wprowadź dane poprawnie od nowa, oddzielone spacją, obiekt nie zostaje zainicjalizowany")
            del(self)

    def __str__(self):
        return "Szereg rozdzielczy punktowy"

    def set_new_data(self, *args):
        self.__init__(self, *args)

    @property
    def data(self):
        return self._data

    @property
    def dsize(self):
        return self._dsize

    def srednia_arytmetyczna_ulamek(self):
        return sum(k*v for k, v in self.data)/self.dsize

    def srednia_arytmetyczna(self):
        return sum(k*v for k, v in self.data)/self.dsize

    def mediana(self):
        sorted_ = list(deepcopy(self.data))
        sorted_.sort(key=lambda x: x[0])
        mid = floor(self.dsize/2)
        prev = False
        for key, value in self.data:
            if value < mid:
                mid -= value
            elif value == mid and mid%2:
                key = prev
            elif prev:
                return (prev+key)/2
            else:
                return key

class Przedzialowa():
    def __init__(self, *args):
        if len(*args) > 1:
            self._data = dict(*args)
            self._total_count = sum([int(i) for i in self._data.values()])
            cprt_size = tuple(self.data.keys())[0]
            self._compartment_size = cprt_size[1]-cprt_size[0]
        else:
            raise TypeError("Na podstawie jednej zmiennej nie można wyliczyć żadnej średniej.")


    def __str__(self):
        return "Szereg rozdzielczy przedziałowy"


    def set_new_data(self, *args):
        self._data = dict(*args)
        self._total_count = sum(self._data.values())
        cprt_size = list(self.data.keys())[0]
        self._compartment_size = cprt_size[1]-cprt_size[0]

    @property
    def data(self):
        return self._data

    @property
    def total_count(self):
        return self._total_count

    @property
    def compartment_size(self):
        return self._compartment_size

    def srednia_arytmetyczna(self):
        return sum([(x[0]+x[1])/2*n for x, n in self.data.items()])/self.total_count

    def mediana(self):
        def correct_compartment(the_rst):
            for cmprt, num in sorted(self.data.items()):
                the_rst -= num
                if the_rst < 0:
                    the_rst += num
                    return cmprt, the_rst
        mid = self.total_count/2
        compartment, the_rest = correct_compartment(mid)
        cmprt_num = self.data.get(compartment)
        cmprt_size = self.compartment_size
        return compartment[0] + (cmprt_size / cmprt_num) * (mid - (mid-the_rest))

    def dominanta(self):
        if len(self.data) < 3:
            return None
        def max_compartment():
            temp = sorted(self.data.items())
            maxi = float("-inf")
            cmprt_max, num_max = None, None
            for cmprt, cm_num in temp[1:-1]:
                if cm_num > maxi:
                    cmprt_max, num_max = cmprt, cm_num
                    maxi = cm_num
                elif cmprt == maxi:
                    pass #ToDo many dominants
            else:
                if num_max < temp[-1][1] or num_max < temp[0][1]:
                    raise ValueError
                return cmprt_max, num_max
        try:
            compartment, num = max_compartment()
            cmprt_low, num_low = min(self.data.items(), key=lambda k: abs(k[0][1] - compartment[0]))
            cmprt_hig, num_hig = min(self.data.items(), key=lambda k: abs(k[0][0] - compartment[1]))
            if __debug__:
                print("compartment, num:", compartment, num)
                print("compartment, num:", cmprt_low, num_low)
                print("compartment, num:", cmprt_hig, num_hig)
            return compartment[0] + (num - num_low)* self.compartment_size / (num * 2 - num_hig - num_low)
        except ZeroDivisionError:
            return "Dominanta nie istnieje"
        except ValueError:
            return "Dominanta nie znajduje się "

    def odchylenie(self):
        #~ s = ,/ suma(środek przedziału**2 * liczebność [next]) / liczebność - srednia arytm
        mid_modifier = self.compartment_size/2
        sum_powed_compartments_and_amounts = sum(amnt*(cmprt[0]+mid_modifier)**2 for cmprt, amnt in self.data.items())
        #~ if __debug__:
            #~ for x, y in self.data.items():
                #~ print(y, "*(", x[0], "+", mid_modifier,")**2")
        return (sum_powed_compartments_and_amounts / self.total_count - self.srednia_arytmetyczna()**2)**0.5

def SCREEN_CLEAR(clear=True):
    if clear:
        print("\033[H\033[J", end="")


if __debug__ and __name__ == "__main__":
    #~ dane = [[2,3,4,2,4,4,3,2,5,5,6,1,2,1,3,4],
        #~ [1,5,4,6,2,3,4,5,1,4,4,3,5,2,4]]
    dane = [(1400, 6), (1800, 9), (2200, 2), (2700, 13)]
    #~ dane = {(100,200): 15, (200,300): 26, (300,400): 8, (400,500): 20,\
            #~ (500,600): 21, (600,700): 10}
    dane = {(1200,1400): 20, (1400,1600): 10, (1600,1800): 20, (1800,2000): 30,\
            (2000,2200): 20}
    if dane:
        for i in dane:
            #~ S = Szczegolowa(*i)
            #~ S = Wazona(*i)
            #~ print("Arytmetyczna:", S.srednia_arytmetyczna()) #Wszystkie
            #~ print("Geometryczna:", S.srednia_geometryczna()) #Szczegółowa
            #~ print("Harmoniczna:", S.srednia_harmoniczna()) #Szczegółowa
            #~ print("Potęgowa:", S.srednia_potegowa()) #Szczegółowa
            #~ print("Mediana:", S.mediana()) #Wszystkie
            #~ print("Dominanta:", S.dominanta()) #Szczegółowa i Przedziałowa
            #~ print("Odchylenie:", S.odchylenie()) #Szczegółowa i Przedziałowa
            #~ print("Wspolczynnik odchylenia:", S.wspolczynnik()) #Szczegółowa
            pass
        print(len(dane))
        S = Przedzialowa(dane)
        #~ S = Wazona(*dane)
        print("Arytmetyczna:", S.srednia_arytmetyczna()) #Wszystkie
        print("Mediana:", S.mediana()) #Wszystkie
        print("Dominanta:", S.dominanta()) #Szczegółowa i Przedziałowa
        print("Odchylenie:", S.odchylenie()) #Szczegółowa i Przedziałowa
