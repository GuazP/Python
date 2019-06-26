from tkinter import *

sys.path.insert(0, 'Sources')
import equipment_data
import stats_data


class Model():
    def __init__(self):
        pass

    #########################################################
    # Child classes to hold data                            #
    #########################################################

    class MainMenu():
        def buttons(self):
            main_buttons = ["Stwórz postać", "Wczytaj postać", "Sprawdź build", "Wyjdź"]
            return main_buttons

    class CreationMenu():

        def __init__(self):
            from Character import Character
            # Core
            self.name = False
            self.archetype = False
            self.alignment = False
            self.race = False
            self.apperance = False
            self.stats = False
            self.classes = False
            self.equipment = False

            # Skills
            self.interactive = False
            self.knowledge = False
            self.crafting = False
            self.general = False
            self.proficiency = False
            self.magic_schools = False

            # Character
            self.Character = Character()

        def creation_panel_data(self):
            core = ["Name", "Archetype", "Alignment", "Race", "Apperance", "Stats", "Classes", "Equipment"]
            skills = ["Interactive", "Knowledge", "Crafting", "General", "Proficiency", "Magic Schools"]
            return core, skills

        def creation_get_preview(self):
            return self.Character.get_data_preview1, self.Character.get_data_preview2

        def preview(self):
            try:
                self.Character.finallize()
            except Exception as ex:
                self.Character_ERROR(ex)
            finally:
                self.Character.char_data_previev()

        def set_name(self, name):
            try:
                self.Character.set_name(name)
                self.name = True
            except Exception as ex:
                self.Character_ERROR(ex)

        def set_archetype(self, archetype):
            try:
                self.Character.set_archetype(archetype)
                self.archetype = True
            except Exception as ex:
                self.Character_ERROR(ex)

        def set_alignment(self, general, detailed):
            try:
                self.Character.set_general_alignment(general)
                self.Character.set_detailed_alignment(detailed)
                self.alignment = True
            except Exception as ex:
                self.Character_ERROR(ex)

        def set_race(self, race):
            try:
                self.Character.set_race(race)
                self.race = True
            except Exception as ex:
                self.Character_ERROR(ex)

        def set_stats(self, stats):
            try:
                self.Character.set_stats(stats)
                self.stats = True
            except Exception as ex:
                self.Character_ERROR(ex)

        def set_classes(self, classes):
            try:
                self.Character.set_base_class(classes)
                self.classes = True
            except Exception as ex:
                self.Character_ERROR(ex)

        def del_classes(self):
            try:
                self.Character.del_base_class()
                self.classes = False
            except Exception as ex:
                self.Character_ERROR(ex)

        def Character_ERROR(self, param):
            print("Do nothing: ", param)

    #########################################################
    # Sending data to view                                  #
    #########################################################

    class Races():
        def __init__(self):
            from stats_data import races
            self.races = races

        def get_races(self):
            return self.races

        def check_race(self, data):
            if data in self.races:
                return True
            return False

    class Archetype():
        def __init__(self):
            from stats_data import archetypes
            self.archetypes = archetypes

        def get_archetypes(self):
            return self.archetypes

        def check_archetype(self, data):
            if data in self.archetypes:
                return True
            return False

    class Apperance():
        def __init__(self):
            from stats_data import pointers_group, features_names
            self.pointers = pointers_group
            self.features = features_names

        def get_features(self):
            return self.features

        def get_pointers(self):
            return self.pointers

    class Alignment():
        def __init__(self):
            from stats_data import general_alignment, detailed_grid
            self.general_alignment = general_alignment
            self.detailed_grid = detailed_grid

        def get_alignment(self):
            return (self.general_alignment, self.detailed_grid)

        def get_general(self):
            return self.general_alignment

        def get_detailed(self):
            return self.detailed_grid

        def check_alignment(self, data):
            # data holds [general_alignment, detailed_from_grid]
            if data[0] in self.general_alignment and data[1] in self.detailed_grid:
                return True
            return False

    class Stats():
        def __init__(self):
            from stats_data import stats_points_cost, stats_points_cap
            self.points_cost = stats_points_cost
            self.points_cap = stats_points_cap

        def check_cost(self, dict_stats):
            return sum(self.points_cost.get(y) for _, y in dict_stats.items()) <= self.points_cap

        def get_default(self, Char):
            return Char.stats

    class Classes():
        def __init__(self):
            from stats_data import base_classes
            self.base_classes = base_classes

        def get_classes(self):
            return self.base_classes

        def check_classes(self, arg):
            if arg in self.base_classes:
                return True
            return False


#########################################################
# Sending data to controller                            #
#########################################################


#########################################################
# Get data from controller to Character                 #
#########################################################
