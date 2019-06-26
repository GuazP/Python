#!/usr/bin/env python3



def foo1():
    print(1)

def foo2():
    print(2)

def main():
    switch = {  1: foo1,
                2: foo2}

    select = int(input("Select: "))

    switch.get(select)()

main()

#Another way with args:

def foo1(a, b, c):
    print(1, a, b, c)

def foo2(b, c):
    print(2, b, c)
    c+=1

def main():
    a=2
    b=3
    c=4

    switch = {  1: lambda a1=a, b1=b, c1=c: foo1(a1,b1,c1),
                2: lambda b1=b: foo2(b1, c)}


    switch.get(1)() #Here call whole "switch"
    c+=1
    switch.get(1)() #Here call whole "switch"
    switch.get(2)() #Here call with another 'c' "switch"

main()
