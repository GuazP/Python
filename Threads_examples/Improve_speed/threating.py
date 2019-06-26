import threading
from time import time

def twoja_funkcja(*args, **kwargs):
    pass

def main(func):
    start = time()+1
    licznik = 0
    w1 = threading.Thread(target=func)
    w2 = threading.Thread(target=func)
    while time() < start:
        licznik += 2
    print("Ilość wywołań:", licznik)

if __name__ == "__main__":
     main(twoja_funkcja)
