#Maciej Pawłowski


def main(poprzedni=[]):
	#Sprawdzamy czy został podany do zapamiętania wynik poprzedniego działania w miejsce macierzu_a
	if type(poprzedni)==tuple:
		poprzedni=list(poprzedni)
		if list(poprzedni)!=[]:
			poprzedni=poprzedni[0]

	#Mój test kontrolny
	if poprzedni==[]:
		print("Program nie przechowuje w pamięci żadnego macierzu.")
	else:
		print("Program pomyślnie zachował poprzedni macierz.")

	print ("Pamiętaj, ilość kolumn macierzy A, musi być równa ilości wierszy macierzy B!")
	print ("Liczby w wierszu! Liczby podawaj oddzielone spacją lub tabulacją.")

	#Przewiduję pomyłkę przy wprowadzaniu macierzy pod względem wartości.
	try:
		#Jeśli wprowadziliśmy do zapamiętania wynik poprzedniego działania, nadpisze macierz_a zamiast wprowadzać.
		if sprawdz_zbior(poprzedni):
			macierz_a=[[float(g) for g in (j for j in input("Kolejno wartości kolumn w wierszu {0}: ".format(i+1)).split())] for i in range(int(input("Wiersze macierzu A: ")))]
		else:
			macierz_a=poprzedni
		macierz_b=[[float(g) for g in (j for j in input("Kolejno wartości kolumn w wierszu {0}: ".format(i+1)).split())] for i in range(int(input("Wiersze macierzu B: ")))]

	#Zadziałaj w przypadku źle wprowadzonych danych.
	except ValueError:
		print("Wprowadzaj jedynie liczby całkowite i zmiennoprzecinkowe!")
		if sprawdz_zbior(poprzedni):
			body(poprzedni)
		else:
			body()

	#Tu nie wiem czemu test nie działa przy abort'cie spowodowanym Ctrl+C
	except KeyboardInterrupt:
		exit("Dziękuję za skorzystanie z programu")

	#Test czy macierz jest poprawnie skonstruowany geometrycznie, równa ilość kolumn i wierszy wg. zasad macierzowych.
	if poprawnosc_macierzy(macierz_a, macierz_b)==False:
		print("Sprawdź poprawność macierzy!")
		body(poprzedni)

#Kontrolnie wyświetl macierze do weryfikacji wizualnej użytkownika:
	print ("Macierz A")
	for i in range(len(macierz_a)):
		 print(macierz_a[i])
	print ("Macierz B")
	for i in range(len(macierz_b)):
		 print(macierz_b[i])
	if input("Sprawdź poprawność powyższych macierzy, czy te macierze chcesz przemnożyć.\nKontynuować działanie programu?\n[t/n]: ").lower()=="t":
		iloczyn(macierz_a,macierz_b)
	else:
		body(poprzedni)
	#Zbędna lambda do obracania macierzy, pozostawiona na względny użytek.
#	transformuj= lambda g: [[new[i] for new in g] for i in range(len(g))]
#	if len(macierz_b)==len(macierz_b[0]):
#		macierz_bt=transformuj(macierz_b)
#		print ("Macierz B obrócona", macierz_bt)


def iloczyn(a,b):
#Zmienne tymczasowe
	ln_a, ln_b=len(a), len(b)
	wyzszy=max(ln_a, ln_b)
	szerszy=max(len(b[0]),len(a[0]))

#Stwórz listę zerową do podliczania:
	c=[[0]*szerszy for i in range(wyzszy)]

#Oblicz wyrazy:
	for i in range(ln_a):
		for j in range(len(b[0])):
			for g in range(ln_b):
				c[i][j] = c[i][j] + a[i][g] * b[g][j]

#Wyświetl działanie i wyniki:
	print ("Mnożenie macierzy!\n{0:11} X {1:11} = {2:11}".format("Macierz A", "Macierz B", "Macierz C"))
	for i in range(wyzszy+1):
		if ln_a>i and ln_b>i:
			print("{0:11} X {1:11} = {2:11}".format(str(a[i]), str(b[i]), str(c[i])))
		elif ln_a<=i and ln_b>i:
			print("{0:11} X {1:11} = {2:11}".format("", str(b[i]), str(c[i])))
		elif ln_b<=i and ln_a>i:
			print("{0:11} X {1:11} = {2:11}".format(str(a[i]), "", str(c[i])))

#Polecenia kończące
		else:
			if input("Kontynuować pracę?\n[t/n]: ").lower()=="t":
				if input("Wprowadzić wynik do następnego działania jako Macierz A?\n[t/n]: ").lower()=="t":
					body(c)
				else:
					print("Dany macierz nie został przechowany w pamięci")
					body()
			else:
				exit("Dziękuję za skorzystanie z programu")

def sprawdz_zbior(a):
#Sprawdź czy zbiór nie będzie pusty.
	if a!=[]:
		return False
	else:
		return True

def poprawnosc_macierzy(a, b):
	lb,la=len(b),len(a)
#Jeśli żaden macierz nie jest pusty.
	if la>0 and lb>0:
		for i in range(len(a)):
			#Sprawdź czy wszystkie wiersze "a" są równe względem siebie i równe ilości wierszy b.
			if len(a[i])!=len(b):
				print("Źle wprowadzone dane!")
				return False
		#Jeśli jest więcej niż jeden wiersz, sprawdź czy mają tyle samo kolumn względem siebie.
		if len(b)!=1:
			for j in range(len(b)-1):
				if len(b[j])!=len(b[j+1]):
					return False
			#Gdy program przejdzie wszystkie testy zwraca true.
			return True
		else:
			return True
	print("Wysokość macierzy nie może być równa zero lub ujemna")
	return False


if __name__ == "__main__":
	print("Witaj w moim bonusowym programie!\n\t\t\t\t\t~Guaz\n")
	main()
