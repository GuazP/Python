from random import randint
from itertools import product

def main():
    triangle_1 = [1, 2, randint(1,4)]
    triangle_2 = [1, 2, randint(1,4)]
    print(triangle_1, triangle_2)
    similarity = is_similar_triangle(triangle_1, triangle_2)
    if similarity:


def is_similar_triangle(triangle_1, triangle_2):
    triangle_1.sort()
    triangle_2.sort()

    if triangle_1 == triangle_2:
        return True

    proportion = 0
    proportion_achieved = []
    
    for enum, two_sides in enumerate(product(trojkat_1, trojkat_2)):
        mod = enum%3 
        if not mod:
            proportion = two_sides[0] / two_sides[1]
            proportion_achieved = [True]
            continue
        else:
            if proporcja == two_sides[0] / two_sides[1]:
                proportion_achieved.append(True)
            else:
                proportion_achieved = []
                continue
        if mod > 1 and len(proportion_achieved) == 3:
            return True
    return False

if __name__ == "__main__":
    main()
