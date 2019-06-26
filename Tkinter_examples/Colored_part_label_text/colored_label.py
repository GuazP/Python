import tkinter as tk
from random import randint
from time import time as tm

begi=tm()
list_2 = [2, 5, 8, 9, 14, 26, 28, 34, 43, 51, 55, 60, 77]
list_1 = [randint(1, 100) for i in range(100)]

root = tk.Tk()

common_nums = set(list_1).intersection(list_2)

for i in list_1:
    label = tk.Label(root, text=i)
    if i in common_nums:
        # print(i)
        label.config(fg='red')
    label.pack(side=tk.LEFT)
end=tm()
print (end-begi)

root.mainloop()
