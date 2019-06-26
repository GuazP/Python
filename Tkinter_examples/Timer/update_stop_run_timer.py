import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.iteration = 0
        self.run = False
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        if self.iteration % 2:
            self.stop() #Później wykona się to i zatrzyma nasz timer
        else:
            self.start() #Najpierw wykona się to, zwiększy iteration i wywoła jeszcze raz update
        self.iteration += 1
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        if self.run:
            self.root.after(1000, self.update_clock)
        else:
            self.root.after(1000, self.update_clock)
            print("Miejsce na funkcję w co 2-giej iteracji") #W tym przypadku nasza funkcja już więcej nie zostanie uruchomiona.

    def stop(self):
        print("stop")
        self.run = False

    def start(self):
        print("start")
        self.run = True

app=App()
