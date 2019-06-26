from itertools import product

def main():
    #### Settings Section ####
    sign = ">=" #~ "==" - equal chance, ">=" - more or equal chance, ">" - more chance etc.
    throws = 2
    dice = 6
    out_dmg_dice = None #~ throw away "the best", "the worst", "worse", "better" or None
    modifier = 0
    dice_times = 2
    
    #### Printing Section ####
    print("TABLE {}d{} with {}".format(throws, dice, sign))
    print("Próg | Normal | Advant | DisAdv |", end="")
    print(" Nor +{0} | Nor -{0} |".format(modifier), end="")
    print(" Adv -{0} | DsA +{0} |".format(modifier), end="")
    print()
    for i in range(throws-abs(modifier), throws*dice+1+abs(modifier)):
        ###Regular
        print("{:^5}".format(i), end="|")
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice)), end="|")
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice, rolltype="Adv")), end="|")
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice, rolltype="DsA")), end="|")
        ###Normal with modifier
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice, add=modifier)), end="|")
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice, add=-modifier)), end="|")
        ####Adv/DisAdv with modifier
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice, add=-modifier, rolltype="Adv")), end="|")
        print("{:>8}".format(rpg_prob_result(throws, dice, i, sign, dmgdice=out_dmg_dice, add=modifier, rolltype="DsA")), end="|")
        print()
        
    #### Chances for dice ####
    print()
    print("Dice | Normal | Advant | DisAdv |", end="")
    print()
    for i in range(1, 6+1):
        print("{:^5}".format(i), end="|")
        print("{:>8}".format(how_many_chances(throws, dice, result=i, times=dice_times)), end="|")
        print("{:>8}".format(how_many_chances(throws, dice, result=i, times=dice_times, rolltype="Adv")), end="|")
        print("{:>8}".format(how_many_chances(throws, dice, result=i, times=dice_times, rolltype="DsA")), end="|")
        print()

class DiceGlobal:
    holder = {  "3d6": [sorted(i) for i in product(range(1, 6+1), repeat=3)],
                "4d6": [sorted(i) for i in product(range(1, 6+1), repeat=4)],
                "5d6": [sorted(i) for i in product(range(1, 6+1), repeat=5)]}

def rpg_prob_result(n, dices, result, operant="==", add=0, dmgdice=None, rolltype=None):
    if rolltype: n+=1
    if dmgdice: n+=1
    
    test_table = str(n)+"d"+str(dices)
    if test_table in DiceGlobal.holder:
        L = DiceGlobal.holder.get(test_table)
    else:
        L = [sorted(i) for i in product(range(1, dices+1), repeat=n)]
        DiceGlobal.holder.update({test_table: L})
    
    if rolltype == "Adv": L = [ignore(i, "the worst") for i in L]
    if rolltype == "DsA": L = [ignore(i, "the best") for i in L]
    if dmgdice: L = [ignore(i, dmgdice) for i in L]
    
    P = [i for i in L if eval("sum(i)+"+str(add)+operant+str(result))]
    return "{:.3f}%".format(len(P)/len(L)*100).replace(".", ",")
    
def how_many_chances(n, dices, result, times, rolltype=None):
    if rolltype: n+= 1
    test_table = str(n)+"d"+str(dices)
    if test_table in DiceGlobal.holder:
        L = DiceGlobal.holder.get(test_table)
    else:
        L = [sorted(i) for i in product(range(1, dices+1), repeat=n)]
        DiceGlobal.holder.update({test_table: L})
    
    if rolltype == "Adv": L = [ignore(i, "the worst") for i in L]
    if rolltype == "DsA": L = [ignore(i, "the best") for i in L]
    
    P = [i for i in L if i.count(result)>=times]
    return "{:.3f}%".format(len(P)/len(L)*100).replace(".", ",")

def ignore(arg, val):
    if val == "the worst":
        return arg[1:]
    elif val == "the best":
        return arg[:len(arg)-1]
    elif not len(arg) in (4, 5):
        raise AttributeError("Zły argument dla funkcji odrzuć.")
    elif val == "worse":
        return arg[:1]+arg[2:]
    elif val == "better":
        return arg[:2]+arg[3:]
    else:
        raise AttributeError("Zły argument dla funkcji odrzuć.")

if __name__ == "__main__":
    main()


