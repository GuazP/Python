#Correct way to not partially override:
class List(list):
    def __getitem__(self, index):
        if isinstance(index, tuple):
            return [self[i] for i in index]
        return super().__getitem__(index)

seq = List("foo bar baaz quux mumble".split())
print(seq[0])
print(seq[2,4,4])
print(seq[1::2])


#Wrong way, but overrides normal list which destroy readability
class list(list):
    def __getitem__(self, index):
        if isinstance(index, tuple):
            return [self[i] for i in index]
        return super().__getitem__(index)

#That override will work
seq = list("foo bar baaz quux mumble".split())
print(seq[0])
print(seq[2,4,4])
print(seq[1::2])

#For that, override won't work
seq = ["foo", "bar", "baaz", "quux","mumble"]
print(seq[0])
try: print(seq[2,4,4])
except TypeError as ex: print(ex)
print(seq[1::2])

