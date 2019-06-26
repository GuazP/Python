#! /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Maciej 'Guaz' Pawłowski"

from parametr_cpu import parameters_cpu as pc_cpu
from pdf_gen import gen_pdf as g_pdf
from bar128_B import code_128_B
from datetime import datetime as dt
from os import system as cmd
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

class main_window():
    def __init__(self):
        self.serwis_tag = pc_cpu()
        root = Tk()

        #Screen size
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        #print('Screen resolution: ', self.screen_width, 'x', self.screen_height)

        self.menubar = Menu(root)
        self.os_header = Frame(root)
        self.os_frame = Frame(root)
        self.os_tail = Frame(root)
        self.now_is = dt.now()
        self.window(root)

        def main_close_window():
            if messagebox.askokcancel("Zamknij", "Jestes pewien ze chcesz zamknac program?"):
                exit('Program zostal pomyslnie zamkniety.')
        root.protocol("WM_DELETE_WINDOW", main_close_window)

        def update():
            self.tkimg = PhotoImage(file="draw-img.gif")
            self.tkimg_label.config(image=self.tkimg)
            self.inputValue=self.comment_entry.get("1.0","end-1c")
            self.now_is = dt.now()
            check_time = Label(self.os_header, text="Aktualny czas: {}".format(self.now_is.strftime("%H:%M %d.%m.%Y")))
            check_time.grid(row=1)
            #print(self.inputValue)
            root.after(400, update)

        root.after(5000, update)
        root.bind("<Escape>", lambda i: self.printing_raport() or root.destroy())
        root.mainloop()


    def window(self, root):
        root.wm_title('CPU reader v1.03')
        root.overrideredirect(0)
        wind = str(int((self.screen_width-600)/2))
        root.geometry("600x630+"+wind+"+50")
        self.menubar_create()
        self.header_frame_create()
        self.body_frame_create()
        self.tail_frame_create()
        root.config(menu=self.menubar)
        #self.menubar.pack(side=TOP, fill=X)
        self.os_header.pack(side=TOP, fill=Y)
        self.os_tail.pack(side=BOTTOM, fill=BOTH)
        self.os_frame.pack(side=TOP, fill=Y)

    def menubar_create(self):
        optionmenu = Menu(self.menubar, tearoff=0)
        optionmenu.add_command(label="Generuj Codabar", command=lambda: self.new_code("<Button-1>"))
        optionmenu.add_command(label="Biały ekran", command=lambda: self.blank_screen("<Button-1>"))
        optionmenu.add_separator()
        optionmenu.add_command(label="Wyświetl konsolę", command=lambda: cmd('xterm'))
        self.menubar.add_cascade(label="Opcje", menu=optionmenu)

        datamenu = Menu(self.menubar, tearoff=0)
        datamenu.add_command(label="Bateria", command=lambda: self.print_txt("battery_info.txt"))
        datamenu.add_command(label="Bios", command=lambda: self.print_txt("bios_info.txt"))
        datamenu.add_command(label="Dysk", command=lambda: self.print_txt("disc_info.txt"))
        datamenu.add_command(label="Ekran", command=lambda: self.print_txt("screen_info.txt"))
        datamenu.add_command(label="Grafika", command=lambda: self.print_txt("graphic_info.txt"))
        datamenu.add_command(label="Model", command=lambda: self.print_txt("cpu_model_info.txt"))
        datamenu.add_command(label="Napęd", command=lambda: self.print_txt("drive_info.txt"))
        datamenu.add_command(label="Procesor", command=lambda: self.print_txt("proc_info.txt"))
        datamenu.add_command(label="Ram", command=lambda: self.print_txt("ram_info.txt"))
        datamenu.add_command(label="Wifi", command=lambda: self.print_txt("wifi_check.txt"))
        self.menubar.add_cascade(label="Dane", menu=datamenu)

        aboutmenu = Menu(self.menubar, tearoff=0)
        aboutmenu.add_command(label="Opis programu", command=lambda: self.license("<Button-1>"))
        aboutmenu.add_command(label="Nawigacja", command=lambda: self.helper("<Button-1>"))
        self.menubar.add_cascade(label="O programie", menu=aboutmenu)

    def header_frame_create(self):
        version = Label(self.os_header, text="CPU reader v{}".format("1.03"))
        version.grid(row=0)

        check_time = Label(self.os_header, text="Aktualny czas: {}".format(self.now_is.strftime("%H:%M %d.%m.%Y")))
        check_time.grid(row=1)

    def body_frame_create(self):
        #Comment widget
        comment_label = Label(self.os_frame, text="Wstaw komentarz: ")
        comment_label.grid(row=1,column=1)

        self.comment_entry_var = StringVar()
        self.comment_entry = Text(self.os_frame)
        self.comment_entry.grid(row=2, column=1, columnspan=4, sticky=E)
        self.inputValue=self.comment_entry.get("1.0","end-1c")

        def main_close_window():
            if messagebox.askokcancel("Zamknij", "Jestes pewien ze chcesz zamknac program?"):
                exit('Program zostal pomyslnie zamkniety.')
        button_quit = Button(self.os_frame, text = "Zamknij", command=main_close_window)
        button_quit.grid(row=1, column=4)

        #Enter coda ID
        entry_label= Label(self.os_frame, text="Wprowadz recznie ID \n(codabar): ")
        entry_label.grid(row=5, column=1, sticky=NSEW)

        self.coda_entry = StringVar()
        entry_coda = Entry(self.os_frame, textvariable=self.coda_entry)
        entry_coda.grid(row=5, column=2, columnspan=3)
        self.coda_entry.set("*opcjonalnie")

    def tail_frame_create(self):
        #Button functions
        czytaj = Button(self.os_tail, text="Ukonczono sprawdzanie")
        czytaj.bind("<Button-1>", self.confirm)
        czytaj.pack(side=BOTTOM, fill=X)

        blank = Button(self.os_tail, text="Wyswietl bialy ekran")
        blank.bind("<Button-1>", func=self.blank_screen)
        blank.pack(side=BOTTOM, fill=X)

        coda = Button(self.os_tail, text="Generuj nowy codabar")
        coda.bind("<Button-1>", func=self.new_code)
        coda.pack(side=BOTTOM, fill=X)

        # ZCZYTAJ CODA PRZEZ SSH
        try:
            self.tkimg = PhotoImage(file="draw-img.gif")
        except:
            code_128_B(self.serwis_tag.return_tag())
            self.tkimg = PhotoImage(file="draw-img.gif")
        self.tkimg_label = Label(self.os_tail, image=self.tkimg)
        self.tkimg_label.image = self.tkimg
        self.tkimg_label.pack(side=BOTTOM, fill=BOTH)

        #Check variables
        self.class_check = StringVar()
        self.class_check.set("B")

        raportA = Radiobutton(self.os_tail, text="A", variable=self.class_check, value="A")
        raportA.pack(side=LEFT, fill=Y)

        raportB = Radiobutton(self.os_tail, text="B", variable=self.class_check, value="B")
        raportB.pack(side=LEFT, fill=Y)

        raportBp = Radiobutton(self.os_tail, text="B+", variable=self.class_check, value="B+")
        raportBp.pack(side=LEFT, fill=BOTH)

        raportC = Radiobutton(self.os_tail, text="C", variable=self.class_check, value="C")
        raportC.pack(side=LEFT, fill=BOTH)

    def confirm(self, event):
        if not self.class_check.get():
            messagebox.showwarning('Błąd!', 'Zaznacz prawidlowo klase sprzetu.')
            return 0
        sec_root = Tk()
        sec_root.wm_title('Check confirm')
        sec_root.geometry('+850+150')
        os_confirm = Frame(sec_root)

        warning_frame = Label(os_confirm, text="Jestes pewny wprowadzonych danych?")
        warning_frame.grid(row=0, columnspan=2)

        confirm_button = Button(os_confirm, text="Tak\nWydrukuj etykiete.")
        confirm_button.bind("<Button-1>", lambda i: self.printing_raport() or sec_root.destroy())
        confirm_button.grid(row=1, column=0)

        abort_button = Button(os_confirm, text="Nie\nPowroc do okna", command=sec_root.destroy)
        abort_button.grid(row=1, column=1)

        os_confirm.pack()
        sec_root.mainloop()


    def printing_raport(self):
        with open("comment_file.txt", "w") as comment_file:
            comment_file.write("Klasa wizualna: {}\nKomentarz:\n{}".format(self.class_check.get(), self.inputValue))
        g_pdf(self.class_check)
        try:
            errorlog = open("error_log.txt", "r")
            messagebox.showwarning('Error!', errorlog.read())
        except FileNotFoundError:
            messagebox.showwarning('Zakończono', 'Pomyślnie zakończono działanie programu!\nPo zamknięciu komunikatu, zamknij program lub sprawdź parametry.')
        cmd('sudo lp -d plik.pdf')
        return 0

    def new_code(self, event):
        Check_ID = str(self.coda_entry.get())
        print(Check_ID)
        if not Check_ID == "*opcjonalnie" and not Check_ID == "":
            try:
                code_128_B(Check_ID)
            except TypeError:
                messagebox.showwarning('Niedozwolone znaki',
                                       'Wprowadziles niedozwolone znaki, kod kreskowy nie zostal zmieniony.')

    def blank_screen(self, event):
        #cmd('metacity --replace')
        if messagebox.showwarning('Zamykanie', 'By zamknac bialy ekran, wcisnij Escape lub kliknij prawym przyciskiem myszy.'):
            sec_root = Toplevel()
            sec_root.wm_title('Blank Screen')
            sec_root.configure(background="white")
            sec_root.geometry(str(self.screen_width+400) + 'x' + str(self.screen_height+400)+'+0+0')
            sec_root.bind("<Escape>", lambda i: sec_root.destroy())
            sec_root.bind("<Button-3>", lambda i: sec_root.destroy())
            os_fill = Frame(sec_root)
            os_fill.pack(fill=BOTH)
            sec_root.mainloop()

    def helper(self, event):
        helper_frame = Tk()
        helper_frame.wm_title('Nawigacja')
        helper_frame.geometry("400x70+200+200")
        helper_frame.bind("<Escape>", lambda i: helper_frame.destroy())
        helper_frame.bind("<Button-3>", lambda i: helper_frame.destroy())
        text_pool = Label(helper_frame, text="Zamykanie każdego okna nie będącego komunikatem,\n odbywa się za pomocą prawego przycisku myszy,\n lub klawisza Escape.")
        text_pool.pack(fill=BOTH)
        close = Button(helper_frame, text="Zamknij", command=lambda: helper_frame.destroy())
        close.pack(side=BOTTOM, fill=Y)
        helper_frame.mainloop()

    def license(self, event):
        license_frame = Tk()
        license_frame.wm_title('Licencja')
        license_frame.geometry("500x400+150+300")
        license_frame.bind("<Escape>", lambda i: license_frame.destroy())
        license_frame.bind("<Button-3>", lambda i: license_frame.destroy())
        version = Label(license_frame, text="CPU reader v1.03")
        version.pack(side=TOP, fill=BOTH)
        autor = Label(license_frame, text="Autorem oprogramowania jest Maciej Pawłowski")
        autor.pack(side=TOP, fill=BOTH)
        email = Label(license_frame, text="E-mail kontaktowy: maciej.pawlowski@mixbox.pl")
        email.pack(side=TOP, fill=BOTH)
        license_text = ["\nOprogramowanie nie jest integralną częścią systemu operacyjnego linux",
                        "umożliwia się zainstalowanie i korzystanie z oprogramowania na dowolnie",
                        "wybranej dystrybucji bądź konfiguracji. Warunkiem korzystania z programu",
                        "jest licencja od właściciela praw autorskich do oprogramowania.",
                        "Wszelkie podmioty pragnące rozprzestrzeniać oprogramowanie powinny",
                        "zwrócić się o pisemną zgodę do właściciela praw autorskich.\n"]
        for i in license_text:
            license_L = Label(license_frame, text=i)
            license_L.pack(side=TOP, fill=Y)

        client_text = ["\nPrawa autorskie do oprogramowania przekazane firmie AT OUTLET S.C.",
                       "ul. Białostocka 47 | 42-200 Częstochowa","REGON: 243515820 | NIP: 5732848991",
                       "Ilość dozwolonych kopii do użytku dla firmy: 10",
                       "Ilość uwzględnia wszystkie wersje oprogramowania.",
                       "Autor zobowiązuje się powiadamiać o możliwych aktualizacjach programu.\n"]
        for i in client_text:
            client = Label(license_frame, text=i)
            client.pack(side=TOP, fill=Y)

        close = Button(license_frame, text="Zamknij", command=lambda: license_frame.destroy())
        close.pack(side=BOTTOM, fill=Y)
        license_frame.mainloop()

    def print_txt(self, info_file):
        data_frame = Tk()
        data_frame.wm_title(info_file)
        data_frame.geometry("+850+150")
        data_frame.bind("<Escape>", lambda i: data_frame.destroy())
        data_frame.bind("<Button-3>", lambda i: data_frame.destroy())
        with open(info_file, "r") as info:
            text = info.readlines()
            for i in text:
                txt = Label(data_frame, text=i)
                txt.pack(side=TOP,fill=Y)
        close = Button(data_frame, text="Zamknij", command=lambda: data_frame.destroy())
        close.pack(side=BOTTOM, fill=Y)
        data_frame.mainloop()

    def do_nothing(self, event):
        print("Tchorzliwie odmawiam wykonania niedokonczonej operacji!")


if __name__ == "__main__":
    main_window()
