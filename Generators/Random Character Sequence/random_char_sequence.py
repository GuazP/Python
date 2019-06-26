import random, string

def randWord(minimum, maximum, times_ascii=1):
    randseq = list(string.printable+string.ascii_letters*times_ascii)
    randseq = [ch for ch in randseq if not ch.isspace()]
    random.shuffle(randseq)
    return "".join(ch for ch in (randseq[:random.randint(minimum,maximum)]))

if __name__ == "__main__":
    for i in range(30):
        print('\"'+randWord(3, 10)+'\",', end=" ") 


