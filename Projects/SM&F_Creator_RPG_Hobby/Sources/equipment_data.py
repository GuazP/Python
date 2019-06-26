default_armors = {
        'Metal Skin': (8, 10, -3, 6, 'Armor', 'Overstretched ', 8, ['Unmobile', 'Airtight'], 5000),
        'Heavy Rider Plate Armor': (6, 8, -3, 6, 'Armor', 'Overstretched ', 6, ['Unmobile', 'Airtight', 'Hardened'], 2600),
        'Full Plate Armor': (5, 7, 0, 10, 'Armor', 'Heavy', 3, ['Unmobile'], 1600),
        'Half Plate Armor': (3, 6, 1, 12, 'Armor', 'Heavy', 2, ['Unmobile'], 800),
        'Light Rider Plate Armor': (3, 7, 0, 10, 'Armor', 'Heavy', 4, ['Unmobile'], 1000),
        'Densly ring Mail': (2, 4, 3, 18, 'Armor', 'Medium', 0, [''], 600),
        'Chain Mail': (2, 3, 4, 18, 'Armor', 'Medium', -1, [''], 300),
        'Soldiers Mail': (1, 2, 4, 18, 'Armor', 'Medium', -2, ['Hardened'], 100),
        'Studded Leather': (1, 2, 6, None, 'Clothes', 'Light', -3, [''], 60),
        'Heavy Leather': (1, 1, 8, None, 'Clothes', 'Light', -4, [''], 30),
        'Light Leather': (0, 1, 8, None, 'Clothes', 'Light', -4, [''], 20),
        'Formal Attire': (0, 0, 8, 18, 'Clothes', 'Material', None, ['Elegant', 'stiff'], 200),
        'Adventure Attire': (0, 0, None, None, 'Clothes', 'Material', None, [''], 5)
        }

default_weapons = {
        'Maczuga': ('One-Hand', 'Bludgeoning', 'Hammers', 'Short', 'k10', ['0', ''], ['Pancerzołamacz', 'Zamaszysta']),
        'Buława': ('One-Hand', 'Bludgeoning', 'Hammers', 'Short', 'k12', ['1', 'Maczuga'], ['Pancerzołamacz', 'Zamaszysta', 'k+']),
        'Morgensztern': ('One-Hand', 'Bludgeoning', 'Hammers', 'Short', 'k10', ['2', 'Morgensztern'], ['Pancerzołamacz', 'Zamaszysta', 'Druzgocząca']),
        'Cep Bojowy': ('One-Hand', 'Bludgeoning', 'Hammers', 'Short', 'k12', ['3', 'Cep Bojowy'], ['Pancerzołamacz', 'Zamaszysta', 'Druzgocząca', 'k+']),
        'Ciężka Maczuga': ('Two-Hand', 'Bludgeoning', 'Hammers', 'Heavy', 'k12', ['0', ''], ['Dwuręczna', 'Pancerzołamacz', 'Zamaszysta', 'Ciężka']),
        'Ciężka Buława': ('Two-Hand', 'Bludgeoning', 'Hammers', 'Heavy', 'K12+2', ['1', 'Ciężka Maczuga'], ['Dwuręczna', 'Pancerzołamacz', 'Zamaszysta', 'Ciężka', 'k+']),
        'Wekiera': ('Two-Hand', 'Bludgeoning', 'Hammers', 'Heavy', 'k12', ['2', 'Ciężka Buława'], ['Dwuręczna', 'Pancerzołamacz', 'Zamaszysta', 'Ciężka', 'Druzgocząca']),
        'Cep Bojowy': ('Two-Hand', 'Bludgeoning', 'Hammers', 'Heavy', 'K12+2', ['3', 'Wekiera'], ['Dwuręczna', 'Pancerzołamacz', 'Zamaszysta', 'Ciężka', 'Druzgocząca', 'k+']),
        'Nadziak': ('One-Hand', 'Piercing', 'Picks', 'Short', 'k6', ['0', ''], ['Przebijająca', 'Druzgocząca']),
        'Kilof': ('Two-Hand', 'Piercing', 'Picks', 'Heavy', 'k8', ['0', ''], ['Dwuręczna', 'Przebijająca', 'Druzgocząca', 'Ciężka']),
        'Kosa': ('Two-Hand', 'Slashing', 'Picks', 'Polearms', 'k8', ['1', 'Kosa'], ['Dwuręczna', 'Penetrująca', 'Druzgocząca', 'k+']),
        'Kosa Bojowa': ('Two-Hand', 'Slashing', 'Picks', 'Polearms', 'k10', ['2', 'Kosa Bojowa'], ['Dwuręczna', 'Penetrująca', 'Druzgocząca', 'k++']),
        'Widły': ('Two-Hand', 'Piercing', 'Pikes', 'Polearms', 'k10', ['0', ''], ['Dwuręczna', 'Przebijająca', 'Przeszywająca', 'Szarżołamacz', 'Ciężka', 'Druzgocząca', 'k++']),
        'Włócznia': ('Two-Hand', 'Piercing', 'Pikes', 'Polearms', 'k6', ['1', 'Widły'], ['Dwuręczna', 'Przebijająca', 'Przeszywająca', 'Szarżołamacz', 'Szybka']),
        'Halabarda': ('Two-Hand', 'Slashing', 'Pikes', 'Polearms', 'k6', ['2', 'Włócznia'], ['Dwuręczna', 'Penetrująca', 'Przeszywająca']),
        'Oszczep': ('Two-Hand', 'Piercing', 'Pikes', 'Polearms', 'k6', ['2', 'Włócznia'], ['Dwuręczna', 'Przebijająca', 'Przeszywająca', 'Szarżołamacz', 'Szybka', 'Miotana']),
        'Partyzana': ('Two-Hand', 'Piercing', 'Pikes', 'Polearms', 'k8', ['2', 'Włócznia'], ['Dwuręczna', 'Przebijająca', 'Przeszywająca', 'Szarżołamacz', 'k+']),
        'Trójząb Hakowaty': ('Two-Hand', 'Piercing', 'Pikes', 'Polearms', 'k12', ['3', 'Widły'], ['Dwuręczna', 'Przebijająca', 'Przeszywająca', 'Szarżołamacz', 'Druzgocząca', 'k+++']),
        'Sierp': ('One-Hand', 'Slashing', 'Sickles', 'Short', 'k6', ['0', ''], ['Penetrująca', 'Zaczepna']),
        'Sierpak': ('One-Hand', 'Slashing', 'Sickles', 'Short', 'k8', ['1', 'Sierp'], ['Penetrująca', 'Zaczepna', 'k+']),
        'Sierp Bojowy': ('Two-Hand', 'Slashing', 'Sickles', 'Polearms', 'k8', ['2', 'Sierpak'], ['Dwuręczna', 'Penetrująca', 'Zaczepna', 'k+']),
        'Podwójny Sierp Bojowy': ('Two-Hand', 'Slashing', 'Sickles', 'Polearms', 'k10', ['3', 'Sierp Bojowy'], ['Dwuręczna', 'Penetrująca', 'Zaczepna', 'Szybka', 'k++']),
        'Toporek': ('One-Hand', 'Slashing', 'Axes', 'Short', 'k10', ['0', ''], ['Penetrująca']),
        'Topór Ręczny': ('One-Hand', 'Slashing', 'Axes', 'Short', 'k10', ['1', 'Toporek'], ['Penetrująca', 'Miotana']),
        'Topór Szarpany': ('One-Hand', 'Slashing', 'Axes', 'Short', 'k12', ['2', 'Topór ręczny'], ['Penetrująca', 'Druzgocząca', 'k+']),
        'Topór Podwójny': ('One-Hand', 'Slashing', 'Axes', 'Short', 'k12', ['3', 'Topór półtoraręczny'], ['Penetrująca', 'Szybka', 'k+']),
        'Siekiera': ('Two-Hand', 'Slashing', 'Axes', 'Heavy', 'k12', ['0', ''], ['Dwuręczna', 'Penetrująca', 'Ciężka', 'Zaczepna']),
        'Topór': ('Two-Hand', 'Slashing', 'Axes', 'Heavy', 'k12', ['1', 'Siekiera'], ['Dwuręczna', 'Penetrująca', 'Ciężka', 'Druzgocząca']),
        'Topór Bojowy': ('Two-Hand', 'Slashing', 'Axes', 'Heavy', 'k12', ['2', 'Topór'], ['Dwuręczna', 'Penetrująca', 'Ciężka', 'Druzgocząca', 'Zaczepna']),
        'Berdysz': ('Two-Hand', 'Slashing', 'Axes', 'Polearms', 'k12', ['3', 'Topór bojowy'], ['Dwuręczna', 'Penetrująca', 'Szarżołamacz', 'Przebijająca', 'Zaczepna', 'k+']),
        'Kostur': ('Two-Hand', 'Bludgeoning', 'Staffs', 'Polearms', 'k8', ['0', ''], ['Dwuręczna', 'Szybka', 'Wyszkolenie']),
        'Zakrzywiony Kostur': ('Two-Hand', 'Bludgeoning', 'Staffs', 'Polearms', 'k8', ['1', 'Kostur'], ['Dwuręczna', 'Ciężka', 'Przebijająca', 'Wyszkolenie']),
        'Bicz': ('One-Hand', 'Slashing', 'Whips', 'Range', 'k6', ['0', ''], ['Penetrująca', 'Szkolona', 'Zaczepna']),
        'Bicz Łańcuchowy': ('One-Hand', 'Slashing', 'Whips', 'Range', 'k6', ['1', 'Bicz'], ['Penetrująca', 'Szkolona', 'Zaczepna', 'Druzgocząca']),
        'Łańcuch': ('One-Hand', 'Slashing', 'Whips', 'Range', 'k10', ['2', 'Bicz łańcuchowy'], ['Penetrująca', 'Szkolona', 'Zaczepna', 'k++']),
        'Kolczasty Łańcuch': ('One-Hand', 'Slashing', 'Whips', 'Range', 'k10', ['3', 'Kolczasty łańcuch'], ['Penetrująca', 'Szkolona', 'Zaczepna', 'Druzgocząca', 'k++']),
        'Fist': ('Body', 'Bludgeoning', 'Knuckles', 'Melee', 'k4', ['0', ''], ['Zwarcie', 'Ręczna', 'Wrażliwa']),
        'Cestus': ('Hand', 'Bludgeoning', 'Knuckles', 'Melee', 'k8', ['0', ''], ['Zwarcie', 'Ręczna', 'Wrażliwa']),
        'Tekko': ('Hand', 'Bludgeoning', 'Knuckles', 'Melee', 'k8', ['1', 'Cestus'], ['Zwarcie', 'Ręczna']),
        'Kolczasta Rękawica': ('Hand', 'Bludgeoning', 'Knuckles', 'Melee', 'k8', ['2', 'Tekko'], ['Zwarcie', '-Ręczna']),
        'Khatar': ('Hand', 'Piercing', 'Knuckles', 'Melee', 'k8', ['1', ''], ['Zwarcie', 'Przebijająca']),
        'Potrójny Khatar': ('Hand', 'Piercing', 'Knuckles', 'Melee', 'k12', ['2', 'Khatar'], ['Zwarcie', 'Przebijająca', 'k++']),
        'Khatar Zygzakowy': ('Hand', 'Piercing', 'Knuckles', 'Melee', 'k10', ['3', 'Khatar'], ['Zwarcie', 'Przebijająca', 'Druzgocząca', 'k+']),
        'Pazury Tygrysa': ('Hand', 'Slashing', 'Knuckles', 'Melee', 'k8', ['1', ''], ['Zwarcie', 'Penetrująca']),
        'Tekko-Kagi': ('Hand', 'Slashing', 'Knuckles', 'Melee', 'k10', ['2', 'Pazury tygrysa'], ['Zwarcie', 'Penetrująca', 'Szkolona', 'Szybka', 'k+']),
        'Jelenie Rogi': ('Hand', 'Slashing', 'Knuckles', 'Melee', 'k12', ['3', 'Tekko-kagi'], ['Zwarcie', 'Penetrująca', 'Szkolona', 'Szybka', 'k++']),
        'Sztylet': ('One-Hand', 'Piercing', 'Daggers', 'Melee', 'k4', ['0', ''], ['Zwarcie', 'Przebijająca', 'Precyzyjna', 'Szybka']),
        'Lewak': ('One-Hand', 'Piercing', 'Daggers', 'Melee', 'k4', ['1', 'Sztylet'], ['Zwarcie', 'Przebijająca', 'Precyzyjna', 'Rozbrajająca']),
        'Rapier': ('One-Hand', 'Piercing', 'Daggers', 'Short', 'k6', ['1', 'Sztylet'], ['Przebijająca', 'Precyzyjna', 'k+']),
        'Triblade Dagger': ('One-Hand', 'Piercing', 'Daggers', 'Melee', 'K4 x2', ['3', 'Sztylet'], ['Zwarcie', 'Przebijająca', 'Precyzyjna', 'Szybka', 'k2']),
        'Krótki Miecz': ('One-Hand', 'Slashing', 'Swords', 'Short', 'k8', ['0', ''], ['Penetrująca', 'Precyzyjna']),
        'Miecz-Hak': ('One-Hand', 'Slashing', 'Swords', 'Short', 'k8', ['1', 'Krótki Miecz'], ['Penetrująca', 'Zaczepna']),
        'Sejmitar': ('One-Hand', 'Slashing', 'Swords', 'Short', 'k10', ['1', 'Krótki Miecz'], ['Penetrująca', 'Nieprecyzyjna', 'k+']),
        'Miecz Półtoraręczny*': ('One-Hand', 'Slashing', 'Swords', 'Heavy', 'k10', ['1', 'Krótki Miecz'], ['Penetrująca', 'Ciężka', 'Zamaszysta']),
        'Chopesz': ('One-Hand', 'Slashing', 'Swords', 'Short', 'k8', ['2', 'Sejmitar'], ['Penetrująca', 'Druzgocząca']),
        'Łamacz Mieczy': ('One-Hand', 'Slashing', 'Swords', 'Short', 'k8', ['3', 'Miecz-Hak'], ['Penetrująca', 'Precyzyjna', 'Rozbrajająca+', 'k-']),
        'Ostrze Zygzakowe': ('One-Hand', 'Slashing', 'Swords', 'Short', 'k10', ['3', 'Krótki Miecz'], ['Penetrująca', 'Druzgocząca', 'k+']),
        'Długi Miecz': ('Two-Hand', 'Slashing', 'Swords', 'Heavy', 'k10', ['0', ''], ['Dwuręczna', 'Penetrująca', 'Ciężka']),
        'Miecz Półtoraręczny': ('Two-Hand', 'Slashing', 'Swords', 'Short', 'k8', ['1', 'Długi Miecz'], ['Dwuręczna', 'Penetrująca']),
        'Bułat': ('Two-Hand', 'Slashing', 'Swords', 'Heavy', 'k12', ['1', 'Długi Miecz'], ['Dwuręczna', 'Penetrująca', 'Ciężka', 'Druzgocząca', 'k+']),
        'Miecz Dwuręczny': ('Two-Hand', 'Slashing', 'Swords', 'Heavy', 'K12+2', ['2', 'Miecz półtoraręczny'], ['Dwuręczna', 'Penetrująca', 'Ciężka', 'k++']),
        'Miecz Podwójny': ('Two-Hand', 'Slashing', 'Swords', 'Heavy', 'k8', ['2', 'Długi Miecz'], ['Dwuręczna', 'Penetrująca', 'Ciężka', 'Obosieczna', 'k-']),
        }

weapon_special_list = {
        'Zwarcie': 'Aby zaatakować tą bronią należy przejść do zwarcia.',
        'Ciężka': 'W rundzie można wykonać maksymalnie jeden atak taką bronią.',
        'Dwuręczna': 'Podwojony bonus z siły do obrażeń przy ataku wielokrotnym lub szarży.',
        'Pancerzołamacz': 'Do ataków tej broni traktuj pancerz jak o 5 mniejszy, minimalnie 3 AR*.\n(* Broń nie może ominąć pancerza przy krytycznych obrażeniach)',
        'Zamaszysta': 'W rundzie nie można wykonać więcej ataków niż dwa taką bronią*.\n(* Nie można zwiększyć ilości tych ataków przez atuty)',
        'Przeszywająca': 'Ignoruje AR niższe od 10.',
        'Przebijająca': 'Każdy punkt obrażeń na kości, zmniejsza redukcję pancerza o 1 AR.',
        'Penetrująca': 'Jeśli AR jest mniejsze lub równe 2, zadajesz podwójne obrażenia z kości obrażeń.\n(* Podczas omijania większego pancerza w wyniku krytycznych obrażeń, nie zadajesz podwójnych obrażeń)',
        'Precyzyjna': 'Dwie najwyższe wartości na kości obrażeń omijają pancerz całkowicie.',
        'Druzgocząca': 'Rzucasz dwoma kośćmi na obrażenia i wybierasz korzystniejszy dla siebie wynik.\n(* Broń nie może ominąć pancerza przy krytycznych obrażeniach)',
        'Szybka': 'W ataku wielokrotnym wyprowadza dodatkowy cios.',
        'Miotana': 'Broń nadająca się do miotania bez kar.',
        'Zaczepna': 'Deklarując atak za plecy przed zadaniem obrażeń, możesz spróbować pociągnąć wroga aby go przewrócić.\n(* Broń z cechą zaczepna, zyskuje również cechę rozbrajająca.)',
        'Szarżołamacz': 'Zamiast swojej akcji, można zadeklarować przełamanie szarży.',
        'Szkolona': 'Wymaga przeszkolenia w tym typie broni.\n(* Bez wyszkolenia przy ataku zadawane są połowiczne obrażenia.)',
        'Prestiżowa': 'Jak szkolona wymaga przeszkolenia, jednak przeszkolenie dotyczy konkretnej broni.\n(* Bez wyszkolenia, przy ataku dwie najniższe wartości na kości obrażeń, powodują krzywdę tego który jej używa.)',
        'Ręczna': 'Dla tych obrażeń AR celu liczy się podwójnie, z wyjątkiem walki w zwarciu.',
        'Wrażliwa': 'Jeśli AR celu jest większe niż obrażenia, te różnice należy odjąć od życia atakującego.',
        'Rozbrajająca': 'Za pomocą tej broni, w akcji obrony, można zadeklarować próbę pozbawienia broni wroga.',
        'Nieprecyzyjna': 'Za pomocą tej broni krytyczne obrażenia nie omijają AR celu.',
        'Obosieczna': 'Atakując tą bronią można zaatakować jednocześnie dwóch wrogów kosztem 1 i 1/2 ataku.'
        }
