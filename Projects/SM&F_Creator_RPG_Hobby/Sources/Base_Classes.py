from random import randint
from math import floor as math_floor

class Class_Selector():
    'Selector for all rpg base classes'

    def select_class(self, string):
        temp = {"Warrior": Warrior, "Scout": Scout, "Archer": Archer, "Thief": Thief,
            "Hexxer": Hexxer, "Warden": Warden, "Bard": Bard, "Trapper": Trapper,
            "Witch": Witch, "Sleazier": Sleazier, "Enlightened": Enlightened, "Ancestor Speaker": Ancestor_Speaker}
        return temp.get(string, None)


class TemplateClass():
    poor_save = 0.25
    medium_save = 0.3334
    good_save = 0.5
    great_save = 0.75

    def __init__(self, lvl, first=False, HP=None):
        self.get_cls_var()
        self.lvl = lvl
        self.first = first
        if HP == None:
            first_HP = (first*(10+self.health_type[0]+self.randHP()))
            even_HP = math_floor(lvl/2)*self.health_type[0]
            odd_HP = sum([self.randHP() for _ in range(math_floor((lvl-1)/2))])
            self.HP = first_HP + even_HP + odd_HP #first + even + odd
        else:
            if lvl % 2:
                self.HP += self.randHP()
            else:
                self.HP += self.health_type[0]
        self.calculate_saves()
        self.endu_times = 1*first + math_floor((lvl-1)/2) #endurance modifier
        self.attack = math_floor(lvl*self.attack_type) #base attack
        self.defence = math_floor(self.defence_type*lvl) #defense vs effects
        self.skill = self.skills_type * lvl # + INT MOD
        self.get_table()
        self.caster_init_()

    def __str__(self):
        return "Template Class"

    def randHP(self):
        return randint(1, self.health_type[1])

    def caster(self):
        return bool(self.caster_kind)

    def lvl_advance(self):
        self.__init__(self.lvl+1, self.first, self.HP)

    def str_HP_builder(self):
        str_HP = " (" + "d".join(str(z) for z in (self.first+math_floor((self.lvl-1)/2), self.health_type[1])) + " + " + str(((10+self.health_type[0])*self.first) + math_floor(self.lvl/2)*self.health_type[1]) + ")"
        return str_HP

    def get_class_specials(self):
        temp = []
        for x,y in self.table:
            if x < self.lvl+1:
                temp += [y] if isinstance(y, str) else [y[z] for z in range( len(y) )]
            else:
                return temp
        return temp

class Warrior(TemplateClass):
    def __str__(self):
        return "Warrior"

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.great_save) #max tough + mod

    def get_cls_var(self):
        self.health_type = (4, 4)
        self.attack_type = 1
        self.defence_type = 0.5
        self.skills_type = 4
        self.caster_type = 0
        self.school_type = 0

    def get_table(self):
        self.table = [(1, "Warrior Path"), (2, "Path Feature"), (3, "Path Feature"),\
                        (5, "Weapon Family"), (6, "Path Feature"), (7, "Path Feature"), \
                        (10, ("Path Feature", "Weapon Speciality")), (11, "Path Feature"), \
                        (14, "Path Feature"), (15, ("Path Feature", "Weapon Mastery")) ]

    def caster_init_(self):
        self.caster_kind = ""

class Archer(TemplateClass):

    def __str__(self):
        return "Archer"

    def get_cls_var(self):
        self.health_type = (2, 4)
        self.attack_type = 1
        self.defence_type = 0.5
        self.skills_type = 6
        self.caster_type = 0
        self.school_type = 0

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.great_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = ""

class Thief(TemplateClass):

    def __str__(self):
        return "Thief"

    def get_cls_var(self):
        self.health_type = (1, 4)
        self.attack_type = 0.75
        self.defence_type = 0.67
        self.skills_type = 8
        self.caster_type = 0
        self.school_type = 0

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.great_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.great_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = ""

class Scout(TemplateClass):

    def __str__(self):
        return "Scout"

    def get_cls_var(self):
        self.health_type = (2, 4)
        self.attack_type = 1
        self.defence_type = 0.67
        self.skills_type = 6
        self.caster_type = 0
        self.school_type = 0

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.great_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.good_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = ""

class Witch(TemplateClass):

    def __str__(self):
        return "Witch"

    def get_cls_var(self):
        self.health_type = (1, 4)
        self.attack_type = 0.5
        self.defence_type = 0.67
        self.skills_type = 4
        self.caster_type = 0.67
        self.school_type = 1

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.great_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.great_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Witch"
        self.caster_lvl = 1*self.first + math_floor(self.caster_type*self.lvl)
        self.school_lvl = 1*self.first + math_floor(self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 6*self.first + 3*self.caster_lvl

class Sleazier(TemplateClass):

    def __str__(self):
        return "Sleazier"

    def get_cls_var(self):
        self.health_type = (2, 4)
        self.attack_type = 0.5
        self.defence_type = 0.67
        self.skills_type = 6
        self.caster_type = 0.67
        self.school_type = 1

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.great_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Sleazier"
        self.caster_lvl = 1*self.first + math_floor(self.caster_type*self.lvl)
        self.school_lvl = 1*self.first + math_floor(self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 6*self.first + 3*self.caster_lvl

class Enlightened(TemplateClass):

    def __str__(self):
        return "Enlightened"

    def get_cls_var(self):
        self.health_type = (2, 4)
        self.attack_type = 0.5
        self.defence_type = 0.34
        self.skills_type = 6
        self.caster_type = 0.67
        self.school_type = 1

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.great_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Enlightened"
        self.caster_lvl = 1*self.first + math_floor(self.caster_type*self.lvl)
        self.school_lvl = 1*self.first + math_floor(self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 6*self.first + 3*self.caster_lvl

class Ancestor_Speaker(TemplateClass):

    def __str__(self):
        return "Ancestor Speaker"

    def get_cls_var(self):
        self.health_type = (3, 4)
        self.attack_type = 0.5
        self.defence_type = 0.5
        self.skills_type = 4
        self.caster_type = 0.67
        self.school_type = 1

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.great_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.poor_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Ancestor Speaker"
        self.caster_lvl = 1*self.first + math_floor(self.caster_type*self.lvl)
        self.school_lvl = 1*self.first + math_floor(self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 6*self.first + 3*self.caster_lvl

class Hexxer(TemplateClass):

    def __str__(self):
        return "Hexxer"

    def get_cls_var(self):
        self.health_type = (2, 4)
        self.attack_type = 1
        self.defence_type = 0.5
        self.skills_type = 2
        self.caster_type = 0.5
        self.school_type = 0.5

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.good_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.good_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Witch"
        self.caster_lvl = math_floor(1*self.first/2 + self.caster_type*self.lvl)
        self.school_lvl = math_floor(1*self.first/2 + self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 5*self.first + 2*self.caster_lvl

class Trapper(TemplateClass):
    #Genjutsu z naruto
    #Prześwietlanie strachu
    def __str__(self):
        return "Trapper"

    def get_cls_var(self):
        self.health_type = (0, 4)
        self.attack_type = 0.75
        self.defence_type = 0.67
        self.skills_type = 8
        self.caster_type = 0.5
        self.school_type = 0.5

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.good_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Witch"
        self.caster_lvl = math_floor(1*self.first/2 + self.caster_type*self.lvl)
        self.school_lvl = math_floor(1*self.first/2 + self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 5*self.first + 2*self.caster_lvl

class Warden(TemplateClass):

    def __str__(self):
        return "Warden"

    def get_cls_var(self):
        self.health_type = (3, 4)
        self.attack_type = 0.75
        self.defence_type = 0.67
        self.skills_type = 2
        self.caster_type = 0.5
        self.school_type = 0.5

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.great_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Warden"
        self.caster_lvl = math_floor(1*self.first/2 + self.caster_type*self.lvl)
        self.school_lvl = math_floor(1*self.first/2 + self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 5*self.first + 2*self.caster_lvl

class Bard(TemplateClass):

    def __str__(self):
        return "Bard"

    def get_cls_var(self):
        self.health_type = (1, 4)
        self.attack_type = 0.75
        self.defence_type = 0.67
        self.skills_type = 6
        self.caster_type = 0.5
        self.school_type = 0.5

    def calculate_saves(self):
        self.soul = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max soul + mod
        self.mind = 10 + math_floor(self.lvl*TemplateClass.good_save) #max mind + mod
        self.mobil = 10 + math_floor(self.lvl*TemplateClass.medium_save) #max mobil + mod
        self.tough = 10 + math_floor(self.lvl*TemplateClass.great_save) #max tough + mod

    def get_table(self):
        self.table = [(1, "ToDo")]

    def caster_init_(self):
        self.caster_kind = "Ancestor Speaker"
        self.caster_lvl = math_floor(1*self.first/2 + self.caster_type*self.lvl)
        self.school_lvl = math_floor(1*self.first/2 + self.school_type*self.lvl)
        self.school_skills = self.school_lvl * 2
        self.MP = 5*self.first + 2*self.caster_lvl
