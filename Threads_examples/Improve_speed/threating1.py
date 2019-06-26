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
    while time() < start:
        pass
    print("Ilość wywołań:", licznik.wartosc)
    exit()

if __name__ == "__main__":
     main()
