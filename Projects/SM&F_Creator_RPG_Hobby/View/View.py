from tkinter import *
from copy import deepcopy

class View():
###########################################################
# Initialize nessesary fields                             #
###########################################################
    def __init__(self, master):
        #Status bar
        self.status_frame = Frame(master, bg="white")
        self.status = None
        self.status_bar()
        self.status_frame.pack(side=BOTTOM, fill=X)

        #Main frame
        self.frame = Frame(master, bg="black")
        self.frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(self.frame, "Dark", "Button", "Text", "Label")

        #Object containers
        self.selector = []
        self.creation_panel = {}
        self.labels = []
        self.entries = []
        self.spinboxes = []
        self.navigate = ""
        self.decision = 0

        #Additional window controllers
        self.confirm = ""
        self.selected = ""


    def status_bar(self, value = "Witamy w aplikacji SM&F"):
        if self.status:
            self.status.destroy()
        self.status = Label(self.status_frame, text=value, bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

###########################################################
# Clean fields which contains data                        #
###########################################################

    def cleaner(self):
        for item in self.selector:
            item.destroy()
        for item in self.labels:
            item.destroy()
        for item in self.entries:
            item.destroy()
        for item in self.spinboxes:
            item.destroy()
        self.creation_panel.clear()
        self.navigate = ""

###########################################################
# Generate fields with data from model                    #
###########################################################


###########################################################
# Methods from controller to create fields in main window #
###########################################################
    def main_view(self, buttons):
    #### Navigate functions for main menu          ####
        def Creation(self):
            self.navigate = "Create"
        def Load(self):
            self.navigate = "Load"
        def BuildTest(self):
            self.navigate = "Test build"
        function = [lambda _: Creation(self),
                     lambda _: Load(self),
                     lambda _: BuildTest(self),
                     lambda _: exit()]

    #### Configurations for create interference    ####
        self.configure_grid_y()
        row = 0

    #### Create body of view                       ####
        for txt, func in zip(buttons, function):
            self.selector.append(Button(self.frame, text=txt))
            self.selector[-1].bind("<ButtonRelease-1>", func)
            self.selector[-1].grid(row=row, sticky=NSEW)
            row += 1
        self.frame.pack(side=LEFT, fill=BOTH, expand=1)

    def creation_view(self, core_line, skills_line):
    #### Navigate functions for main menu          ####
        def set_navigate(self, arg):
            self.navigate = arg

    #### Configurations for create interference    ####
        self.configure_grid_x(20)
        self.configure_grid_y(5)
        row = 0
        col = 0

    #### Create body of view                       ####
        for txt in core_line:
            if col == 12:
                col = 0
                row += 1
            self.creation_panel[txt] = Button(self.frame, text=txt, command=lambda cls=self, arg=txt: set_navigate(cls, arg))
            self.creation_panel[txt].grid(row=row, column=col, columnspan=3, sticky=NSEW)
            col += 3

        for txt in skills_line:
            if col == 12:
                col = 0
                row += 1
            self.creation_panel[txt] = Button(self.frame, text=txt, state=DISABLED, command=lambda cls=self, arg=txt: set_navigate(cls, arg))
            self.creation_panel[txt].grid(row=row, column=col, columnspan=4, sticky=NSEW)
            col += 4

        self.creation_panel["Preview"] = Button(self.frame, text="Preview", command=lambda cls=self: set_navigate(cls, "Preview"))
        self.creation_panel["Preview"].grid(row=row+1, column=0, columnspan=12, sticky=NSEW)

        self.preview_window1 = Label(self.frame, text="", justify=LEFT)
        self.preview_window1.grid(row=0, rowspan=5, column=12, columnspan=4, sticky=NSEW)
        self.preview_window1.config(state='disabled', relief=SUNKEN)

        self.preview_window2 = Label(self.frame, text="", justify=LEFT)
        self.preview_window2.grid(row=0, rowspan=5, column=16, columnspan=4, sticky=NSEW)
        self.preview_window2.config(state='disabled', relief=SUNKEN)

        self.frame.pack(side=LEFT, fill=BOTH, expand=1)

    def name_view(self, master):
        frame = Frame(master)
        frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(frame, "Dark", "Button", "Label", "Frame")
        labels = {}
        entries = {}
        self.confirm = ""
        self.selected = {}

        self.configure_grid_y(3, window=frame)
        self.configure_grid_x(3, window=frame)

        def confirm_manager(self, entries):
            name = entries["Name"].get()
            surname =  entries["Surname"].get()
            if len(name) > 2:
                if surname != "":
                    name += " " + surname
                self.confirm = name
            else:
                confirm_button.config(state="disabled")

        name = StringVar()
        labels["Name"] = Label(frame, text="Insert Name: ")
        labels["Name"].grid(row=0, column=0, sticky=EW)
        entries["Name"] = Entry(frame, textvariable=name)
        entries["Name"].grid(row=0, column=1, columnspan=2, sticky=EW)

        surname = StringVar()
        labels["Surname"] = Label(frame, text="Optionally Surname: ")
        labels["Surname"].grid(row=1, column=0, sticky=EW)
        entries["Surname"] = Entry(frame, textvariable=surname)
        entries["Surname"].grid(row=1, column=1, columnspan=2, sticky=EW)

        confirm_button = Button(frame, text="Confirm", command=lambda cls=self: confirm_manager(cls, entries))
        confirm_button.grid(row=2, column=0, columnspan=3, sticky=EW)

    def archetypes_view(self, master, archetypes, details):
        frame = Frame(master)
        frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(master, "Dark", "Button", "Frame")
        buttons = {}
        self.confirm = ""
        self.selected = ""

        self.configure_grid_y(8, window=frame)
        self.configure_grid_x(8, window=frame)

        def confirm_manager(self):
            if self.selected:
                self.confirm = self.selected
                self.selected = ""

        def display_details(detail, text_field, race):
            if self.selected:
                buttons[self.selected].config(background="black")
            else:
                buttons["Confirm"].config(state='normal')
            buttons[race].config(background="green")
            text_field = detail
            label.config(text=text_field)
            self.selected = race

        text_field = ""
        label = Label(frame, bd=6, bg="white", height=12, width=20)
        label.grid(row=0, rowspan=5, column=5, columnspan=3, sticky=NSEW)

        row = 0
        col = 0

        for txt in archetypes:
            if col == 4:
                col = 0
                row += 1
            buttons[txt] = Button(frame, text=txt,
                        command=lambda det=details.get(txt), var=text_field, rac=txt: display_details(det, var, rac))
            buttons[txt].grid(row=row, column=col, sticky=NSEW)
            col += 1
        row += 1

        buttons["Confirm"] = Button(frame, text="Confirm", command=lambda cls=self: confirm_manager(cls))
        buttons["Confirm"].grid(row=row, column=0, columnspan=4, sticky='NSEW')
        buttons["Confirm"].config(state='disabled')

    def alignment_view(self, master, general, details):
        frame = Frame(master)
        frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(frame, "Dark", "Button", "Frame")
        buttons_general = {}
        buttons_details = {}
        self.confirm = []
        self.selected = ["", ""]

        self.configure_grid_y(3, window=frame)
        self.configure_grid_x(9, window=frame)

        def confirm_manager(self):
            if self.selected:
                self.confirm = self.selected
                self.selected = ["", ""]

        def confirm_filler(position, txt):
            if not position and self.selected[0]:
                buttons_general[self.selected[0]].config(background="black")
            elif position and self.selected[1]:
                buttons_details[self.selected[1]].config(background="black")
            self.selected[position] = txt
            if "" not in self.selected:
                confirm_button.config(state="normal")

        row = 0
        col = 0

        for txt in general:
            buttons_general[txt] = Button(frame, text=txt, command=lambda x=txt: confirm_filler(0, x))
            buttons_general[txt].grid(row=row, column=col, columnspan=3, sticky=EW)
            buttons_general[txt].bind("<ButtonRelease-1>", lambda _, arg=buttons_general[txt]: arg.config(background="green"))
            row+=1

        for txt in details:
            if col == 3:
                col = 0
                row += 1
            buttons_details[txt] = Button(frame, text=txt, command=lambda x=txt: confirm_filler(1, x))
            buttons_details[txt].grid(row=row, column=col, sticky=EW)
            buttons_details[txt].bind("<ButtonRelease-1>", lambda _, arg=buttons_details[txt]: arg.config(background="green"))
            col +=1

        confirm_button = Button(frame, text="Confirm", command=lambda cls=self: confirm_manager(cls))
        confirm_button.grid(row=row+1, column=0, columnspan=3, sticky=EW)
        confirm_button.config(state='disabled')

    def races_view(self, master, races, details):
        frame = Frame(master)
        frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(master, "Dark", "Button", "Frame")
        buttons = {}
        self.confirm = ""
        self.selected = ""

        self.configure_grid_y(12, window=frame)
        self.configure_grid_x(4, window=frame)

        def confirm_manager(self, cancel=False):
            if cancel:
                self.confirm = "Cancel"
            elif self.selected:
                self.confirm = self.selected #ToDo submit gender
                self.selected = ""

        def display_details(detail, text_field, race):
            if self.selected:
                buttons[self.selected].config(background="black")
            else:
                buttons["Confirm"].config(state='normal')
            buttons[race].config(background="green")
            text_field = detail
            label.config(text=text_field)
            self.selected = race

        def change_sex(self, bool): #ToDo change race names
            if bool:
                buttons["Male"].config(state='normal', background="black")
                buttons["Female"].config(state='disabled', background="green")
            else:
                buttons["Female"].config(state='normal', background="black")
                buttons["Male"].config(state='disabled', background="green")

        text_field = ""
        label = Label(frame, textvariable=text_field, bd=6, bg="white", height=12, width=20)
        label.grid(row=0, rowspan=4, column=6, columnspan=6, sticky=NSEW)

        row = 1
        col = 0

        buttons["Male"] = Button(frame, text="Male", command=lambda cls=self: change_sex(cls, False))
        buttons["Male"].grid(row=0, column=0, columnspan=3, sticky=NSEW)
        buttons["Male"].config(state='disabled', background="green")
        buttons["Female"] = Button(frame, text="Female", command=lambda cls=self: change_sex(cls, True))
        buttons["Female"].grid(row=0, column=3, columnspan=3, sticky=NSEW)

        for txt in races:
            if col == 6:
                col = 0
                row += 1
            buttons[txt] = Button(frame, text=txt,
                        command=lambda det=details.get(txt), var=text_field, rac=txt: display_details(det, var, rac))
            buttons[txt].grid(row=row, column=col, columnspan=2, sticky=NSEW)
            col += 2
        row += 1

        buttons["Cancel"] = Button(frame, text="Cancel", command=lambda cls=self: confirm_manager(cls, True))
        buttons["Cancel"].grid(row=row, column=0, columnspan=3, sticky=NSEW)
        buttons["Confirm"] = Button(frame, text="Confirm", command=lambda cls=self: confirm_manager(cls))
        buttons["Confirm"].grid(row=row, column=3, columnspan=3, sticky=NSEW)
        buttons["Confirm"].config(state='disabled')

    def stats_view(self, master, default, point_cost):
        frame = Frame(master)
        frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(master, "Dark", "Button", "Frame")
        buttons = {}
        label_names = {}
        label_values = {}
        self.confirm = ""
        self.configure_grid_y(10, window=frame)
        self.configure_grid_x(4, window=frame)

        def confirm_manager(self, default):
            if calc_points(default) > -1:
                self.confirm = default

        def calc_points(dict_items):
            return 90-sum([point_cost.get(y) for _, y in dict_items.items()])

        def change_value(stat, value, default):
            new_value = default.get(stat)
            if (new_value > -3 and value < 0) or (new_value < 5 and value > 0):
                temp = deepcopy
                default[stat] = default.get(stat, 0)+value
            label.config(text="Points left : " + str(calc_points(default)))
            label_values[stat].config(text=default.get(stat))


        label = Label(frame, text="Points left : " + str(calc_points(default)))
        label.grid(row=0, column=0, columnspan=4, sticky=NSEW)

        row = 1
        col = 1

        for element in default:
            label_names[element] = Label(frame, text=element)
            buttons[element+"-"] = Button(frame, text="-",
                        command=lambda st=element, dft=default: change_value(st, -1, dft))
            label_values[element] = Label(frame, text=default.get(element))
            buttons[element+"+"] = Button(frame, text="+",
                        command=lambda st=element, dft=default: change_value(st, 1, dft))
            label_names[element].grid(row=row, column=0, sticky=NSEW)
            buttons[element+"-"].grid(row=row, column=1, sticky=NSEW)
            label_values[element].grid(row=row, column=2, sticky=NSEW)
            buttons[element+"+"].grid(row=row, column=3, sticky=NSEW)
            row += 1

        buttons["Confirm"] = Button(frame, text="Confirm", command=lambda dft=default, cls=self: confirm_manager(cls, dft))
        buttons["Confirm"].grid(row=row, column=0, columnspan=4, sticky=NSEW)

    def classes_view(self, master, classes):
        frame = Frame(master)
        frame.pack(side=TOP, fill=Y, anchor=CENTER)
        self.configure_visual(master, "Dark", "Button")
        buttons = {}
        self.confirm = ""
        self.selected = ""

        self.configure_grid_y(4, window=frame)
        self.configure_grid_x(4, window=frame)

        def confirm_manager(self, arg=""):
            if self.selected and not arg:
                self.confirm = self.selected
                self.selected = ""
            elif arg:
                self.confirm = "DELETE"
                self.selected = ""

        def display_details(selected):
            if self.selected:
                buttons[self.selected].config(background="black")
            else:
                buttons["Confirm"].config(state='normal')
            buttons[selected].config(background="green")
            self.selected = selected

        row = 0
        col = 0

        for txt in classes:
            if col == 4:
                col = 0
                row += 1
            buttons[txt] = Button(frame, text=txt,
                                  command=lambda select=txt: display_details(select))
            buttons[txt].grid(row=row, column=col, sticky=NSEW)
            col += 1
        row += 1

        buttons["Delete"] = Button(frame, text="Delete", command=lambda cls=self, arg="DELETE": confirm_manager(cls, arg))
        buttons["Delete"].grid(row=row, column=0, columnspan=2, sticky=NSEW)
        buttons["Confirm"] = Button(frame, text="Confirm", command=lambda cls=self: confirm_manager(cls))
        buttons["Confirm"].grid(row=row, column=2, columnspan=2, sticky=NSEW)
        buttons["Confirm"].config(state='disabled')

###########################################################
# Fields updated by Controllers                           #
###########################################################

    def set_char_label(self, txt):
        self.preview_window1.config(text=txt[0])
        self.preview_window2.config(text=txt[1])

###########################################################
# Configurations functions                                #
###########################################################

    def creation_send_on(self, *param):
        for option in param:
            self.creation_panel[option].config(state='active')


    def configure_visual(self, master, visual, *names):
        if visual == "Dark":
            for name in names:
                master.option_add("*"+name+".background", "black")
                master.option_add("*"+name+".foreground", "white")
        elif visual == "Bright":
            for name in names:
                master.option_add("*"+name+".background", "white")
                master.option_add("*"+name+".foreground", "black")

    def configure_grid_x(self, col=1, col_interval=1, weigh=1, window=""):
        if not window:
            window = self.frame
        for x in range(col*col_interval):
            Grid.columnconfigure(window, x, weight=weigh)

    def configure_grid_y(self, row=1, row_interval=1, weigh=1, window=""):
        if not window:
            window = self.frame
        for y in range(row*row_interval):
            Grid.columnconfigure(window, y, weight=weigh)

###########################################################
# Controller access data reader                           #
###########################################################

    def get_navigate(self):
        temp = self.navigate
        self.navigate = ""
        return temp

    def get_confirm(self):
        temp = self.confirm
        self.confirm = ""
        return temp