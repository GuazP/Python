from threading import Thread
from time import time

class counter(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Wystartowałem!")
        self.wartosc = 0
        self.start()

    def run(self):
        while True:
            self.wartosc += 1

def main():
    start = time()+1
    licznik = counter()
    licznik2 = counter()
    while time() < start:
        pass
    print("Ilość wywołań:", licznik.wartosc+licznik2.wartosc)
    print("Ilość wywołań:", licznik.wartosc, "|", licznik2.wartosc)
    exit()

if __name__ == "__main__":
     main()
