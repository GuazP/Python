@staticmethod
def func():
    var = "abc"
    print("func")

other = "abc"

if __name__ == "__main__":
    print("main")
    print(dir())
    print(type(func))
    print(func)
    try:
        func()
    except TypeError as ex:
        print(ex)
    try:
        print(var)
    except NameError as ex:
        print(ex)
    print(other)
