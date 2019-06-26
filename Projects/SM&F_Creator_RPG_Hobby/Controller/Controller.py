from tkinter import *

import sys
sys.path.insert(0, 'View')
from View import View
sys.path.insert(0, 'Model')
from Model import Model

class Controller():
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = View(self.root)
        self.root.title("SN&F Character Creation Panel")
        self.root.overrideredirect(0)
        self.root.geometry("1200x650+"+str((self.root.winfo_screenwidth()-1200)//2)+"+20")

    def mainmenu_controller(self):
        MainMenu = self.model.MainMenu()
        buttons = MainMenu.buttons()
        self.view.main_view(buttons)
        def update():
            navigate = self.view.get_navigate()
            if navigate:
                if navigate == "Create":
                    return self.creation_controller()
                elif navigate == "Load":
                    #~ self.loading_controller()
                    print("Function isn't writed")
            self.root.after(100, update)
        self.root.after(100, update)
        self.root.mainloop()

    def creation_controller(self):
        self.CreationPanel = self.model.CreationMenu()
        core, skills = self.CreationPanel.creation_panel_data()
        self.preview_window = 0
        self.creation_check = False
        self.view.cleaner()
        self.view.creation_view(core, skills)
        navigate_select = {"Name"           : self.name_window,
                           "Archetype"      : self.archetype_window,
                           "Alignment"      : self.alignment_window,
                           "Race"           : self.race_window,
                           "Apperance"      : self.apperance_window,
                           "Stats"          : self.stats_window,
                           "Classes"        : self.classes_window,
                           "Equipment"      : self.equipment_window,
                           "Interactive"    : self.equipment_window,
                           "Knowledge"      : self.equipment_window,
                           "Crafting"       : self.equipment_window,
                           "General"        : self.equipment_window,
                           "Proficiency"    : self.equipment_window,
                           "Magic Schools"  : self.equipment_window
                           }
        #TODO
        self.view.set_char_label(self.CreationPanel.creation_get_preview())
        def update():
            navigation = self.view.get_navigate()
            if navigation in navigate_select:
                self.root.withdraw()
                navigate_select.get(navigation)()
            if self.creation_check:
                self.view.set_char_label(self.CreationPanel.creation_get_preview())
                self.creation_check = False
                #Undisable buttons startly locked
                if not self.CreationPanel.general and self.CreationPanel.archetype and self.CreationPanel.race:
                    self.view.creation_send_on('General')
                if not self.CreationPanel.knowledge and self.CreationPanel.stats and self.CreationPanel.classes:
                    self.view.creation_send_on('Interactive', 'Knowledge', 'Proficiency', 'Crafting', 'Magic Schools')
            self.root.after(100, update)

        def close_window():
            self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", close_window)
        self.root.after(100, update)
        self.root.mainloop()

    def name_window(self):
        root = Tk()
        root.title("SM&F Name Editor")
        def check_name(string):
            if len(string) > 2:
                return True
            return False

        self.view.name_view(root)
        def update():
            confirm = self.view.get_confirm()
            if confirm and check_name(confirm):
                self.view.creation_panel['Name'].config(background="green")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.set_name(confirm)
                self.creation_check = True
                return None
            root.after(100, update)

        def close_window():
            self.root.deiconify()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", close_window)
        root.after(100, update)

    def archetype_window(self):
        root = Tk()
        root.title("SM&F Archetype Selector")
        data = self.model.Archetype()
        archetypes = data.get_archetypes()
        #ToDo
        details = {x:y for x,y in zip(archetypes, range(16))}

        self.view.archetypes_view(root, archetypes, details)
        def update():
            confirm = self.view.get_confirm()
            if confirm and data.check_archetype(confirm):
                self.view.creation_panel["Archetype"].config(background="green")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.set_archetype(confirm)
                self.creation_check = True
                return None
            root.after(100, update)

        def close_window():
            self.root.deiconify()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", close_window)
        root.after(100, update)

    def alignment_window(self):
        root = Tk()
        root.title("SM&F Alignment Selector")
        data = self.model.Alignment()
        general = data.get_general()
        details = data.get_detailed()

        self.view.alignment_view(root, general, details)
        def update():
            confirm = self.view.get_confirm()
            if confirm and data.check_alignment(confirm):
                self.view.creation_panel['Alignment'].config(background="green")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.set_alignment(confirm[0], confirm[1])
                self.creation_check = True
                return None
            root.after(100, update)

        def close_window():
            self.root.deiconify()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", close_window)
        root.after(100, update)

    def race_window(self):
        root = Tk()
        root.title("SM&F Race Selector")
        data = self.model.Races()
        races = data.get_races()
        #ToDo
        details = {x:y for x,y in zip(races, range(6))}

        self.view.races_view(root, races, details)
        def update():
            confirm = self.view.get_confirm()
            if confirm and data.check_race(confirm):
                self.view.creation_panel['Race'].config(background="green")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.set_race(confirm)
                self.creation_check = True
                return None
            elif confirm == "Cancel":
                self.root.deiconify()
                root.destroy()
                return None
            root.after(100, update)

        def close_window():
            self.root.deiconify()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", close_window)
        root.after(100, update)

    def apperance_window(self):
        self.root.deiconify()

    def stats_window(self):
        root = Tk()
        root.title("SM&F Stats Calculator")
        data = self.model.Stats()
        default = data.get_default(self.CreationPanel.Character)
        def check_stats(dict_items):
            if len(dict_items) == 8 and data.check_cost(dict_items):
                return True
            return False

        self.view.stats_view(root, default, data.points_cost)
        def update():
            confirm = self.view.get_confirm()
            if confirm and check_stats(confirm):
                self.view.creation_panel['Stats'].config(background="green")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.set_stats(confirm)
                self.creation_check = True
                return None
            root.after(100, update)

        def close_window():
            self.root.deiconify()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", close_window)
        root.after(100, update)

    def classes_window(self):
        root = Tk()
        root.title("SM&F Classes Selector")
        data = self.model.Classes()
        classes = data.get_classes()

        self.view.classes_view(root, classes)
        def update():
            confirm = self.view.get_confirm()
            if confirm and data.check_classes(confirm):
                self.view.creation_panel['Classes'].config(background="green")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.set_classes(confirm)
                self.creation_check = True
                return None
            elif confirm == "DELETE":
                self.view.creation_panel['Classes'].config(background="black")
                self.root.deiconify()
                root.destroy()
                self.CreationPanel.del_classes()
                self.creation_check = True
                return None
            root.after(100, update)

        def close_window():
            self.root.deiconify()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", close_window)
        root.after(100, update)

    def equipment_window(self):
        self.root.deiconify()











