import tkinter as tk


class Welcome():

    def __init__(self, master):

        self.master = master
        self.master.geometry('1000x600+150+50')
        self.master.title('WELCOME')

        self.label1=tk.Label(self.master, text='Welcome to ...', fg='red')
        self.label1.grid(row=0,column=2)
        self.button1=tk.Button(self.master, text='OK',fg='blue', command=self.gotoWages)
        self.button1.grid(row=6,column=2)
        self.button3=tk.Button(self.master, text='QUIT', fg='blue', command=self.master.destroy)
        self.button3.grid(row=7,column=2)

    def gotoWages(self):
        self.label1.destroy(); del(self.label1);
        self.button1.destroy(); del(self.button1);
        self.button3.destroy(); del(self.button3);
        self.wages = Wages(self.master)


class Wages():

    def __init__(self, master):
       
        self.master = master
        self.master.title('Wages')

        self.label1=tk.Label(self.master, text='Secound Window ...', fg='red')
        self.label1.grid(row=0,column=2)
        self.button2=tk.Button(self.master, text='BACK', fg='blue',command=self.gotoBack, )
        self.button2.grid(row=7,column=2)

    def gotoBack(self):
        self.label1.destroy(); del(self.label1);
        self.button2.destroy(); del(self.button2);
        self.back = Welcome(self.master)


def main():

    master=tk.Tk()
    myGUIWelcome=Welcome(master)
    master.mainloop()

if __name__ == '__main__':
    main()
