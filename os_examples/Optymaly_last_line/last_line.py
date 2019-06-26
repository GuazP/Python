import os
with open(__file__, "rb") as f:
    first = f.readline()        # Read the first line.
    f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
    while f.read(1) != b"\n":   # Until EOL is found...
        f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
    last = f.readline()         # Read last line.
    print(last)
