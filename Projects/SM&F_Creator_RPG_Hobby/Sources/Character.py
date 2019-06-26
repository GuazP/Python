import Base_Classes
from stats_data import *
from Equipment_manager import Equipment
#~ stat_points_cost;
#~ variable_modifier;
#~ stats_name;
#~ stats_full_name;
#~ stats_group_name;

from math import floor as math_floor

class Character():
    def __init__(self):
        ##Story details
        self.name = ""
        self.race = ""
        self.sex = ""
        self.detailed_alignment = ""
        self.general_alignment = ""
        self.archetype = ""

        ##General stats
        from stats_data import stats_name
        self.stats = {elem: -3 for elem in stats_name}

        from stats_data import pointers_group
        self.pointers = {elem: 0 for elem in pointers_group}

        self.classes = {}
        self.lvl = 0
        temp_modifier = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.HD = {x:[i*j for i, j in zip(temp_modifier, y)] #To rework
                   for x,y in hit_difficulty_set.items() }
        self.HP = 0
        self.HP_current = 0
        self.str_HP = "" #TODO
        self.MP = 0
        self.MP_current = 0
        self.magic_base = 0
        self.attack_base = 0
        self.defence_base = 0

        from stats_data import stats_group_name
        #Mind, Soul, Mobil, Tough
        self.saves = {}
        for elem in stats_group_name:
            self.saves[elem] = 10


        # General skills
        self.skills_interactive_data = {}
        self.skills_crafting_data = {}
        self.skills_knowledge_data = {}
        self.general_skill_cap = 0
        self.general_skill_points = 0

        # Base skills
        self.skills_base_data = {}
        self.base_skill_cap = 0
        self.base_skill_points = 0

        # Attack and Defence skills
        self.skills_proficiency_data = {}
        self.proficiency_skill_cap = 0
        self.proficiency_skill_points = 0

        # Magic skills
        self.skills_magic_data = {}
        self.magic_skill_cap = 0
        self.magic_skill_points = 0

        self.max_speed = 18
        self.eq = Equipment()

    def refresh(self):
        self.HP = 0
        self.MP = 0
        self.attack_base = 0
        self.defence_base = 0
        self.str_HP = ""

    @property
    def get_data_preview1(self):
        stats =  (f"Strenght     (STR) : {self.stats.get('STR')}\n"
                       f"Endurance    (END) : {self.stats.get('END')}\n"
                       f"Dexterity    (DEX) : {self.stats.get('DEX')}\n"
                       f"Agility      (AGY) : {self.stats.get('AGY')}\n"
                       f"Wisdom       (WIS) : {self.stats.get('WIS')}\n"
                       f"Intuition    (ITU) : {self.stats.get('ITU')}\n"
                       f"Intelligence (INT) : {self.stats.get('INT')}\n"
                       f"Flair        (FLR) : {self.stats.get('FLR')}\n")
        pointers = f"\n".join(str(x) + ": " + str(y) for x, y in self.pointers.items()) + "\n"
        classes = f"\n".join(str(x) + ": " + str(y) for x, y in self.classes.items()) + "\n" if self.classes else "None\n"
        string = ( f"Character name: {self.name}\n"
                   f"Character race: {self.race}\n"
                   f"Character sex: {self.sex}\n"
                   f"Character archetype: {self.archetype}\n"
                   f"\n"
                   f"General alignment: {self.general_alignment}\n"
                   f"Detailed alignment: {self.detailed_alignment}\n"
                   f"\n"
                   f"Health points: {self.HP}\n"
                   f"Power points: {self.MP}\n"
                   f"Attack points: {self.attack_base}\n"
                   f"Magic points: {self.magic_base}\n"
                   f"Defense points: {self.defence_base}\n"
                   f"\n"
                   f"Toughness save: {self.saves['Toughness']}\n"
                   f"Mobility save: {self.saves['Mobility']}\n"
                   f"Soul save: {self.saves['Soul']}\n"
                   f"Mind save: {self.saves['Mind']}\n"
                   f"\n"
                   f"Stats:\n"+
                   stats+
                   f"\n"
                   f"Pointers:\n"+
                   pointers+
                   f"\n"
                   f"Classes:\n"+
                   classes
                   )
        return string

    @property
    def get_data_preview2(self):
        hd = f"\n".join(str(x) + ": " + str(sum(y)) for x, y in self.HD.items()) + "\n"
        string = (f"Hit Difficulty:\n"+
                  hd)
        return string


    def char_data_previev(self):
        print("Imię postaci:", self.name)
        print("Rasa postaci:", self.race)

        # TODO
        print("General alignment:", self.general_alignment)
        print("Detailed alignment:", self.detailed_alignment)

        print("HP:", self.HP, self.str_HP)
        print("MP:", self.MP)
        print("Attack:", self.attack_base)
        print("Defence:", self.defence_base)

        #End TODO

        print("Saves:")
        for elem in stats_group_name:
            print("\t", elem + ":", self.saves.get(elem, 0))

        print("Statystyki główne:")
        for elem in stats_name:
            print("\t", elem + ":", self.stats.get(elem, 0))

        print("Wskaźniki:")
        for elem in pointers_group:
            print("\t", elem + ":", self.pointers.get(elem, 0))

        print("Klasy:")
        for elem in self.classes:
            print("\t", str(elem) + ":", self.classes.get(elem))
        print("Poziom:", self.lvl)

        print("HD:")
        for elem in hit_difficulty_names:
            print("\t", elem, ":", sum(self.HD.get(elem)))

        print("Equipment:")
        print("\tHelmet:", str(self.eq.helmet))
        print("\tAmulet:", str(self.eq.amulet))
        print("\tArmor:", str(self.eq.armor))
        print("\tBelt:", str(self.eq.belt))
        print("\tTalisman:", str(self.eq.talisman))
        print("\tHands:", str(self.eq.hands[0]) + ",", str(self.eq.hands[1]))
        print("\tContainer:", str(self.eq.container))

    def advance_class(self, string):
        classes = {str(x): x for x in self.classes}
        classes.get(string).lvl_advance()
        for elem in self.classes:
            if str(elem) == string:
                self.classes[elem] = self.classes.get(elem, 0) +1
        self.lvl += 1

    def set_name(self, name):
        self.name = name

    def set_race(self, race):
        self.race = race

    def set_archetype(self, archetype):
        self.archetype = archetype

    def set_general_alignment(self, general):
        self.general_alignment = general

    def set_detailed_alignment(self, details):
        self.detailed_alignment = details

    def set_stats(self, stats):
        if len(stats) == 8:
            self.stats = stats
            return True
        return False

    def set_pointers(self, stats):
        if len(stats) == 4:
            self.pointer = {x:y for x,y in zip(pointers_group, stats)}
            return True
        return False

    def set_base_class(self, base_class, class_lvl=1):
        Selector = Base_Classes.Class_Selector()
        temporary = Selector.select_class(base_class)
        if temporary == None:
            return False
        if self.classes:
            base_class = temporary(class_lvl)
        else:
            base_class = temporary(class_lvl, first=True)
        if str(base_class) in [str(x) for x,y in self.classes.items()]:
            self.advance_class(str(base_class))
            return True
        elif str(base_class) in base_classes:
            self.classes[base_class] = self.classes.get(base_class, base_class.lvl)
            self.lvl += base_class.lvl
            return True
        return False

    def del_base_class(self):
        for item in self.classes:
            del item
        del self.classes
        self.classes = {}

    def set_core_stat(self, name, value):
        if name in stats_name:
            self.stats[name] = int(value)
            return True
        return False

    def set_character_armor(self, armor_name, unique=False, description=None, *armor_data):
        self.eq.set_armor(armor_name.title(), unique, description, *armor_data)

    def set_character_weapon(self, weapon_name, unique=False, *weapon_data):
        self.eq.set_weapon(weapon_name.title(), unique, *weapon_data)

    def set_character_helmet(self, helmet_name, unique=False, *helmet_data):
        self.eq.set_helmet(helmet_name.title(), unique, *helmet_data)

    def set_character_amulet(self, amulet_name, unique=False, *amulet_data):
        self.eq.set_amulet(amulet_name.title(), unique, *amulet_data)

    def set_character_talisman(self, talisman_name, unique=False, *talisman_data):
        self.eq.set_talisman(talisman_name.title(), unique, *talisman_data)

    def set_character_belt(self, belt_name, unique=False, *belt_data):
        self.eq.set_belt(belt_name.title(), unique, *belt_data)

    def set_character_offhand(self, offhand_name, unique=False, *offhand_data):
        self.eq.set_offhand(offhand_name.title(), unique, *offhand_data)

    def set_character_container(self, container_name, unique=False, *container_data):
        self.eq.set_container(container_name.title(), unique, *container_data)

    def set_pointer_effectiveness(self, value):
        self.pointer["Effectiveness"] = self.pointer.get("Effectiveness", value)

    def set_pointer_composure(self, value):
        self.pointer["Composure"] = self.pointer.get("Composure", value)

    def set_pointer_attraction(self, value):
        self.pointer["Attraction"] = self.pointer.get("Attraction", value)

    def set_pointer_possesion(self, value):
        self.pointer["Self-possesion"] = self.pointer.get("Self-possesion", value)

    def get_core_modifier(self, name):
        if name in stats_name:
            return math_floor((self.stats[name]/2))

    def update_by_class_variables(self, cls):
        self.HP += cls.HP + (cls.endu_times * self.get_core_modifier("END"))
        self.saves[0] = cls.mind + self.get_core_modifier("INT") + self.get_core_modifier("FLR") \
            if cls.mind > self.saves[0] else self.saves[0]
        self.saves[1] = cls.soul + self.get_core_modifier("WIS") + self.get_core_modifier("ITU") \
            if cls.soul > self.saves[0] else self.saves[0]
        self.saves[2] = cls.mobil + self.get_core_modifier("DEX") + self.get_core_modifier("AGY") \
            if cls.mobil > self.saves[0] else self.saves[0]
        self.saves[3] = cls.tough + self.get_core_modifier("STR") + self.get_core_modifier("END") \
            if cls.tough > self.saves[0] else self.saves[0]
        self.attack_base += cls.attack
        self.defence_base = cls.defence
        self.general_cap_skills += cls.skill
        self.str_HP += cls.str_HP_builder()
        if cls.caster():
            self.MP = cls.MP
        pass

    def get_race_variables(self, race):
        pass

    def calculate_HD(self):
        if self.eq.armor.slot_name == "Armor":
            ar = self.eq.armor.HD
        else:
            ar = 0
        if self.eq.hands[1].slot_name == "Shield":
            sh = self.eq.hands[1].HD or 0
        else:
            sh = 0
        ag = self.get_core_modifier("AGY")
        it = self.get_core_modifier("ITU")
        ba = math_floor(self.defence_base/2)

        #Ba|Ar |Sh|Ag |It |Ma|Na|Ba |Si|Fe|An
        temp_modifier = [ 1, ar, 0, ag, it, 0, 0, ba, 0, 0, 0]
        self.HD = {x:[i*j for i, j in zip(temp_modifier, y)]
                   for x,y in hit_difficulty_set.items() }

    def finallize(self):
        self.refresh()
        for elem in self.classes:
            self.update_by_class_variables(elem)
        self.attack_base += self.get_core_modifier("DEX")
        self.calculate_HD()
        pass

"""
"""
