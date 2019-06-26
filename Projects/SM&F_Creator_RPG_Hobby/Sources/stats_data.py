stats_points_cost = {-3: 0, -2: 2, -1: 4, 0: 7,
                    1: 10, 2: 14, 3: 18, 4: 22, 5: 27}

stats_points_cap = 90

archetypes = ["Soldier", "Guardian", "Berserker", "Bandit",
              "Archeologist", "Librarian", "Scholar", "Specialist",
              "Traveler", "Seducter", "Hermit", "Artist",
              "Priest", "Jester", "Craftsman", "Healer"]

archetypes_detail = [
    ""]

variable_modifier = {"good": 3, "med": 0, "low": -2}

stats_name = ["STR", "END", "DEX", "AGY", "WIS", "ITU", "INT", "FLR"]

stats_full_name = ["Strenght", "Endurance",
                   "Dexterity", "Agility",
                   "Wisdom", "Intuition",
                   "Inteligence", "Flair"]

stats_group_name = ["Toughness", "Mobility", "Soul", "Mind"]

pointers = ["Niedbały", "Niezawodny", #
            "Niecierpliwy", "Cierpliwy", #
            "Brzydki", "Piękny", #Ugly, Beautifull
            "Groźny", "Przyjacielski"] #

pointers_group = ["Effectiveness", "Composure",  #"Skuteczność", "Opanowanie"
                  "Attraction", "Self-possesion"]     #"Atrakcyjność", "Prezentacja"

general_alignment = ["Pure Good", "Conditionaly Good",
                 "True Neutral",
                 "Conditionaly Evil", "Pure Evil"]

detailed_alignment = [("Honorable", "Betrayer"),
                 ("Submissive", "Dominant")]

detailed_grid = ["Honorable Submissive", "Honorable", "Honorable Dominant",
                 "Mysterious Submissive", "Mysterious", "Mysterious Dominant",
                 "Betrayer Submissive", "Betrayer", "Betrayer Dominant"]

features_description = ["a"]*16

base_classes = ["Warrior", "Scout", "Archer", "Thief",
                "Hexxer", "Warden", "Trapper", "Bard",
                "Witch", "Seazier", "Enlightened", "Ancestor Speaker"]

base_classesPL = ["Żerca", "Woj", "Wiedźma", "Łucznik", "Złodziej", "Mówca Przodków",
                "Plugawiec", "Strażnik", "Klątwiarz", "Traper", "Zwiadowca", "Bard"]


races = ["Human", "Dwarven", "Clouder", #Człowiek, Krasnoludek, Chmurnik
        "Buckthorn", "Nymph", "Devil"] #Rokitnik, Rusałka, Czart

specialist_classes = []

heroic_classes = []

    #~ Base, Armor, Shield, Agility, Intuition, Magic, Natural, Battle, Size, feature, Another
                                              #Ba|Ar|Sh|Ag|It|Ma|Na|Ba|Si|Fe|An
hit_difficulty_set = {"Melee Hit Difficulty": [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      "Touch Hit Difficulty": [5, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
                    "Suprise Hit Difficulty": [5, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
                    "Flanked Hit Difficulty": [5, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                     "Ranged Hit Difficulty": [5, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1],
               "Ranged Touch Hit Difficulty": [5, 0, 2, 1, 0, 1, 0, 1, 2, 1, 1],
             "Ranged Suprise Hit Difficulty": [5, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]}

hit_difficulty_names = ["Melee Hit Difficulty", "Touch Hit Difficulty",
                        "Suprise Hit Difficulty", "Flanked Hit Difficulty",
                        "Ranged Hit Difficulty", "Ranged Touch Hit Difficulty",
                        "Ranged Suprise Hit Difficulty"]

stats_full_name = ["Strenght", "Endurance",
                   "Dexterity", "Agility",
                   "Wisdom", "Intuition",
                   "Inteligence", "Flair"]

skills_magic_schools = [
            "Ancestors",            #~ Przodkowie
            "Blessings ",           #~ Błogosławieństwo
            "Conflagration",        #~ Pożoga
            "Creation",             #~ Stworzenie
            "Curse",                #~ Klątwy
            "Destruction",          #~ Zniszczenie
            "Dispersion",           #~ Rozproszenie
            "Enviroment",           #~ Środowisko
            "Illusion",             #~ Iluzja
            "Mutations",            #~ Mutacje
            "Regeneration",         #~ Regeneracja
            "Spirits",              #~ Duchy
            "The Dead"              #~ Umarli
                        ]

skills_weapon_expertise = [
                "Hammers",              #~ Młoty
                "Polearms",             #~ Drzewcowe
                "Axes",                 #~ Topory
                "Swords",               #~ Miecze
                "Daggers",              #~ Sztylety
                "Picks",                #~ Kilofy
                "Pikes",                #~ Piki
                "Sickles",              #~ Sierpy
                "Staffs",               #~ Kostury
                "Whips",                #~ Bicze
                "Knuckles & Hand",      #~ Kastety
                "Short Bows",           #~ Krótkie Łuki
                "Reflective Bows",      #~ Łuki refleksyjne
                "Long Bows",            #~ Długie Łuki
                "Light Crossbows",      #~ Lekkie kusze
                "Heavy Crossbows",      #~ Ciężkie kusze
                "Throwing weapons"      #~ Bronie miotane
                            ]

skills_general = [
            "Animal care",              #~ Opieka nad zwierzętami
            "Appraise",                 #~ Wycena
            "Calculating",              #~ Liczenie
            "Climbing",                 #~ Wspinaczka
            "Concentration",            #~ Koncentracja
            "Cooking",                  #~ Gotowanie
            "Jumping",                  #~ Skok
            "Knotting",                 #~ Wiązanie
            "Medicating",               #~ Opatrywanie
            "Perception",               #~ Spostrzegawczość
            "Reading",                  #~ Czytanie
            "Ressistance [Alcohol]",    #~ Odporność na alkochol
            "Ressistance [Intoxicate]", #~ Odporność na odurzenie
            "Running",                  #~ Bieganie
            "Sense of Direction",       #~ Orientacja w terenie
            "Swimming"                  #~ Pływanie

                 ]

skills_knowledges = [
            "Anatomy",              #~ Anatomia
            "Ancestors",            #~ Przodkowie
            "Appraise",             #~ Wycena
            "Geography",            #~ Geografia
            "Gods and Guardians",   #~ Bogowie i Strażnicy
            "Herbal Medicine",      #~ Ziołolecznictwo
            "Military",             #~ Militaria
            "Moon Energy",          #~ Księżycowa Moc
            "Poisons",              #~ Trucizny
            "Rituals",              #~ Rytuały
            "Spirits",              #~ Duchy
            "Survival",             #~ Przetrwanie
            "Undead",               #~ Nieumarli
            "Witches"               #~ Wiedźmy
                    ]

skills_active = [
            "Aquire trophies",      #~ Pozyskiwanie trofeów
            "Balamce",              #~ Równowaga
            "Camouflage",           #~ Maskowanie
            "Detect bluff",         #~ Wyczuwanie kłamstw
            "Estimate distance",    #~ Ocena odległości
            "Hide",                 #~ Ukrywanie się
            "Horse riding ",        #~ Jeździectwo
            "Move Silently",        #~ Skradanie
            "Open locks",           #~ Otwieranie zamków
            "Pickpocket",           #~ Kradzież kieszonkowa
            "Sailing",              #~ Żeglarstwo
            "Search through",       #~ Przeszukiwanie
            "Trace",                #~ Tropienie
            "Train animals",        #~ Tresura
            "Traps",                #~ Zastawianie pułapek
                ]

skills_crafting = [
            "Alchemy",              #~ Alchemia
            "Blacksmithing",        #~ Kowalstwo
            "Brewing Poisons",      #~ Tworzenie trucizn
            "Carpentry",            #~ Stolarstwo
            "Draftsmanship",        #~ Kreślarstwo
            "Husbandry",            #~ Rolnictwo
            "Weaponsmith",          #~ Zbrojnictwo
                  ]
