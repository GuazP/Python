def TECH_name(device):
    while True:
        choice = input("\nWprowadź nazwę wynalazku: ")
        if device.insert_name(choice):
            break
        else:
            print("Chociaż jeden znak musi być nazwą wynalazku.")
            print("[Suchar mechaniczny: Może to być spacja ^^]")

def GM_modifier(device):
    print("\nMnożnik czasu domyślny 1.5, możliwy do modyfikacji przez GM'a na 1 lub 2.")
    while True:
        choice = input("Wprowadź mnożnik: ")
        if device.insert_multiplier(choice):
            break
        else:
            print("Pozostaw puste, wprowadź 1 lub 2 i kliknij enter.")

def SW(device):
    print("\nWprowadź sumę poziomów głównego wynalazcy w klasach tinkera i pochodnych.")
    while True:
        choice = input("Wprowadź SW: ")
        if device.insert_SW(choice):
            break
        else:
            print("Wprowadź liczbę jedno lub dwucyfrową bez przecinka.")

def FD(device):
    print("\nWprowadź FD (function difficulty) wynalazku z tabeli.")
    while True:
        choice = input("Wprowadź FD: ")
        if device.insert_FD(choice):
            break
        else:
            print("Wprowadź liczbę z zakresu 1 do 7 włącznie.")

def TS(device):
    print("\nWprowadzaj kolejno funkcjonalności nieprzekraczające wartości", device.TL-1)
    while True:
        choice = input("Wprowadź TS: ")
        if not choice:
            if device.TS:
                break
            else:
                print("Musisz wprowadzić chociaż jedną wartość.")
        elif device.insert_TS(choice):
            print("Wartość dodana pomyślnie.")
        else:
            print("Wprowadź wartość nieujemną i nie większą od SW+1.")
            print("Lub pozostaw pole puste i kliknij enter aby zakończyć wprowadzanie.")

def TS_recap(device):
    device.TS = []
    TS(device)

def MR(device):
    print("\nWprowadź MR (malfunction rating), szansa na usterkę razy pięć.")
    while True:
        choice = input("Wprowadź MR: ")
        if device.insert_MR(choice):
            break
        else:
            print("Wprowadź liczbę z zakresu 1 do 5 włacznie.")
