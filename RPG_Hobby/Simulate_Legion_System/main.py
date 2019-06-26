from Player import Player
from math import floor

def walka(Players, first_start):
    if first_start:
        first = 0
        secound = 1
    else:
        first = 1
        secound = 0
    while Players[first].HP > 0:
        Players[first].hit(Players[secound])
        if not Players[secound].HP > 0:
            return secound
        Players[secound].hit(Players[first])
    return first

def main(Players):
    how_many_tests = 10000
    counter = 0
    results = []
    for i in range(how_many_tests//100):
        for j in range(50):
            counter += walka(Players, True)
            Players[0].reset()
            Players[1].reset()
            counter += walka(Players, False)
            Players[0].reset()
            Players[1].reset()
        results.append(counter)
        counter = 0
    print("Skuteczność", Players[0], "to:", round(sum(results)/(how_many_tests//100), 2), "%")
    print("Skuteczność", Players[1], "to:", round(100-(sum(results)/(how_many_tests//100)), 2), "%")


if __name__ == "__main__":
    for i in range(0,20):
        print("Przewaga", abs(20-(i+1)), "SW Woja")
        Players = [ Player("Woj", 1+i, 1+floor(i/2)),#Nick, SW, PWW
                    Player("Mag", 20, 15)]#Nick, SW, PWW
        main(Players)
