
def main():
    test = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    test2 = ['6', '8', '10', 'Q', 'A', '3', '5', '7', '9', 'J', 'K', '2', '4']
    test3 = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q']
    print (sortuj(test))
    print (sortuj(test2))
    print (sortuj(test3))

    talia = {"A" : 1, "K" : 13, "Q" : 12, "10" : 10, "J" : 11, "8" : 8, "9" : 9, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}
    print (sortuj2(talia)) #Result ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def sortuj2(slownik):
    talia = {"A" : 1, "K" : 13, "Q" : 12, "10" : 10, "J" : 11, "8" : 8, "9" : 9, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}
    return [i for i in sorted(slownik, key=talia.get)]

def sortuj(L):
    value_of_str = {"A": 1, "J": 11, "Q": 12, "K": 13}
    for i in L:
        try:
            value_of_str[i] = value_of_str.get(i, int(i))
        except ValueError:
            pass
    return [i for i in sorted(value_of_str, key=value_of_str.get)]

if __name__ == "__main__":
    main()
