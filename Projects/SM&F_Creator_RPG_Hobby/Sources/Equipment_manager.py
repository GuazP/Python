from equipment_data import *

class Equipment():
    def __init__(self):
        self.helmet = Empty()
        self.amulet = Empty()
        self.armor = Empty()
        self.belt = Empty()
        self.talisman = Empty()
        self.hands = [Empty(), Empty()]
        self.container = Empty()

    def __str__(self):
        return "Equipment"

    def set_weapon(self, weapon_name, unique=False, *weapon_data):
        if weapon_name.title() in default_weapons: #name.title()
            self.hands[0] = Weapon(weapon_name, default_weapons.get(weapon_name.title()))
        elif unique and len(weapon_data) > 6:
            self.hands[0] = Weapon(weapon_name, weapon_data)
        if self.hands[0].slot.startswith("Two"):
            self.hands[1] = Empty(True)

    def set_armor(self, armor_name, unique=False, description=None, *armor_data):
        if armor_name in default_armors:
            self.armor = Armor(armor_name, default_armors.get(armor_name.title()), description=description)
        elif unique and len(armor_data) > 8:
            self.armor = Armor(armor_name, armor_data[:9], armor_data[-1], description=description)

    def set_helmet(self, helmet_name, unique=False, *helmet_data, description=None):
        if helmet_name in default_helmets:
            temp = default_helmets.get(helmet_name)
            self.helmet = Helmet(helmet_name, temp[:-1], temp[-1])
        elif unique and len(talisman_data) > 2:
            self.helmet = Helmet(helmet_name, helmet_data, description)

    def set_amulet(self, amulet_name, unique=False, *amulet_data, description=None):
        if amulet_name in default_amulets:
            temp = default_amulets.get(amulet_name)
            self.amulet = Amulet(amulet_name, temp[:-1], temp[-1])
        elif unique and len(amulet_data) > 2:
            self.amulet = Amulet(amulet_name, amulet_data, description)

    def set_talisman(self, talisman_name, unique=False, *talisman_data, description=None):
        if talisman_name in default_talismans:
            temp = default_talismans.get(talisman_name)
            self.talisman = Talisman(talisman_name, temp[:-1], temp[-1])
        elif unique and len(talisman_data) > 2:
            self.talisman = Talisman(talisman_name, talisman_data, description)

    def set_belt(self, belt_name, unique=False, *belt_data, description=None):
        if belt_name in default_belts:
            temp = default_belts.get(belt_name)
            self.belt = Belt(belt_name, temp[:-1], temp[-1])
        elif unique and len(belt_data) > 2:
            self.belt = Belt(belt_name, belt_data, description)

    def set_container(self, container_name, unique=False, *container_data, description=None):
        if container_name in default_containers:
            temp = default_containers.get(container_name)
            self.container = Container(container_name, temp[:-1], temp[-1])
        elif unique and len(talisman_data) > 2:
            self.container = Container(container_name, container_data, description)

class Armor():
    #default_armor construction
    #~ Name:                -> Nazwa pancerza
    #~ (HD,                 -> HD Armor mod
    #~ AR,                  -> AR (Armor Reduction)
    #~ max_stat,            -> Max Agi/Itu bonus
    #~ max_speed,           -> Max speed possible
    #~ type,                -> Typ Armor/Clothes
    #~ weight,              -> Kategoria wagowa
    #~ str_req,             -> Siła wymagana do walki w pancerzu
    #~ specials             -> Specialne cechy pancerza
    #~ ),
    def __init__(self, name, data, enchantment=None, description=None):
        self.name = name
        self.HD = data[0]
        self.AR = data[1]
        self.max_agi_itu = data[2]
        self.max_speed = data[3]
        self.arm_type = data[4]
        self.weight = data[5]
        self.properties = data[6]
        self.str_req = data[7]
        self.price = data[8]
        self.description = description
        self.set_slot_name()

    def __str__(self):
        return self.name

    def set_slot_name(self):
        self.slot_name = "Armor"

    def get_description(self):
        if self.description == None:
            return "Zwyczajny"
        return self.description

class Empty():
    def __init__(self, busy=False):
        self.set_slot_name(busy)

    def set_slot_name(self, busy):
        if busy:
            self.slot_name = "Busy"
        else:
            self.slot_name = "None"

    def __str__(self):
        return self.slot_name

class Shield(Armor):
    def set_slot_name(self):
        self.slot_name = "Shield"

    def __str__(self):
        return self.name

class Base_magic_equipment():
    def __init__(self, name, data, description=None):
        self.name = name
        self.properties = data[0]
        self.price = data[1]
        self.other = data[2:]
        self.description = description
        self.set_slot_name()

    def __str__(self):
        return self.name

    def get_description(self):
        if self.description == None:
            return "Zwyczajny"
        return self.description

class Belt(Base_magic_equipment):
    def set_slot_name(self):
        self.slot_name = "Belt"

class Helmet(Base_magic_equipment):

    def set_slot_name(self):
        self.slot_name = "Helmet"

class Amulet(Base_magic_equipment):
    def set_slot_name(self):
        self.slot_name = "Amulet"

class Talisman(Base_magic_equipment):
    def set_slot_name(self):
        self.slot_name = "Talisman"

class Container(Base_magic_equipment):
    def set_slot_name(self):
        self.slot_name = "Container"

class Weapon():
    #default_weapons construction
    #~ Name:                -> Nazwa broni
    #~ (slot,               -> Jaki slot zajmuje
    #~ kind,                -> Jaki rodzaj obrażeń
    #~ family,              -> Jaka rodzina broni
    #~ ranged,              -> Jaki zasięg broni
#TODO    #~ (dex, str)           -> wymagany DEX/STR do korzystania
    #~ damage,              -> Jakie obrażenia broni
    #~ (lvl, parrent),      -> Jaki lvl kowalstwa i jaki jej poprzednik
    #~ specials             -> Specialne cechy bronii
    #~ ),
    def __init__(self, name, weapon_data, enchantment=None):
        self.name = name.title()
        self.slot = weapon_data[0]
        self.kind = weapon_data[1]
        self.family = weapon_data[2]
        self.ranged = weapon_data[3]
        self.damage = weapon_data[4]
        self.craft = weapon_data[5]
        self.specials = {}
        self.insert_specials(weapon_data[6])

    def __str__(self):
        return self.name

    def debug_info(self):
        print(default_weapons.get(self.name)[:6], self.specials)

    def insert_specials(self, items):
        for item in items:
            temp = Specials(item)
            self.specials[item] = self.specials.get(item, temp)

    def get_weapon_specials(self):
        return [(name,Object.get_description()) for name, Object in self.specials.items()]

class Specials():
    def __init__(self, special):
        self.name = special
        self.description = weapon_special_list.get(special)

    def __str__(self):
        return self.name

    def get_description(self):
        if self.description == None:
            return "Brak opisu"
        return self.description
