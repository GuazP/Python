#!/usr/bin/python3

#~ Warning, some undesirable behavior in rouletewheel with negative fitness function result. ToDo


from random import randint, choice, uniform
POP_SIZE = 30
GEN_SIZE = 16

def main():
    global POP_SIZE
    best = None
    pop = population()
    print("Wynik - populacja początkowa:")
    print("\n".join(str(pop[i])+" | "+str(fitness(pop[i])) for i in range(0, POP_SIZE)))

    __mutation_prob = 0.1
    __crossover_prob = 0.5

    for generation in range(0, 1000):
        for iteration in range(0, POP_SIZE):
            if flip(__mutation_prob): pop[iteration] = mutation(pop[iteration])
            if flip(__crossover_prob):
                partner_idx = randint(0, POP_SIZE-1)
                pop[iteration] = crossover(pop[iteration], pop[partner_idx])
        adapt = [fitness(person) for person in pop]
        pretendent = max(adapt)
        if best == None or pretendent >= best:
            idx = adapt.index(pretendent)
            print("Index potencjalnie idealnego osobnika:", idx, "o wartości:", pretendent)
            print("W pokoleniu:", generation, "| o genotypie:", pop[idx])
            best = pretendent
            x = int(pop[idx], 2)
        selected = roulettewheel(adapt)
        for i in range(0, POP_SIZE): pop[i] = pop[selected[i]]
    #~ print("Wynik - populacja końcowa:")
    #~ print("Łańcuch | Wartość przystosowania")
    #~ print("\n".join(str(pop[i])+" | "+str(fitness(pop[i])) for i in range(0, POP_SIZE)))
    print("X dla którego funkcja jest maksymalna, wynosi:", x)

def population():
    global GEN_SIZE, POP_SIZE
    P = []
    while len(P)!=POP_SIZE:
        rand_init = "".join(choice(["0", "1"]) for i in range(GEN_SIZE)) #Generuje osobnika
        if rand_init not in P: #Sprawdza unikalność.
            P.append(rand_init) #Dodaje jeśli jest unikalny w liście.
    return P

def mutation(t): #Argumentami jest osobnik
    idx = randint(0, len(t)-1)
    change = "1" if t[idx] == "0" else "0"
    t = t[:idx] + change + t[idx+1:]
    return t

def crossover(P, R): #Argumentami jest dwóch osobników
    chang = randint(0, len(P))
    return P[:chang]+R[chang:]

def fitness(t): #Argumentem jest osobnik
    return -(int(t, 2)-1)**2/256 
    #~ return (sum([int(i) for i in t])/len(t))**2

def flip(prawd):
    return prawd < uniform(0, 1)

def roulettewheel(F): #Argumentami są przystosowania osobników
    global POP_SIZE
    result = list(0 for i in range(POP_SIZE))
    sumy = list(0 for i in range(POP_SIZE))
    sumy[0] = F[0] if F[0]>0 else 0
    for i in range(1, POP_SIZE): sumy[i] = sumy[i-1]+F[i] if F[i]>0 else sumy[i-1]
    if sumy[-1] > 0:
        for iteration in range(POP_SIZE): sumy[iteration] = sumy[iteration] / sumy[-1];
        for iteration in range(POP_SIZE):
            r = uniform(0,1)
            for j in range(0, POP_SIZE):
                if sumy[j] < r: result[iteration] = j;
    else:
        for i in range(0, POP_SIZE): result[i] = 0;
    return result

if __name__ == "__main__":
    main()
