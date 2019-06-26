from tkinter import Tk, Button

gui = Tk()
gui.geometry("300x200")

def hide():
    gui.withdraw() # Hide window

    #~ Create secound one:
    secound_window = Tk()
    secound_window.geometry("300x200")
    #~ Here should be code opening new window ended with line:
    secound_window.protocol("WM_DELETE_WINDOW", lambda: reveal(secound_window))
    #~ ... Or some button should control it.
    drugieokno.mainloop()


def reveal(root):
    root.destroy() #~ Close secound window
    gui.deiconify() #~ Reveal old one

b1 = Button(gui, text = "Click", command=reveal).place(x=150, y=150)

gui.mainloop()
