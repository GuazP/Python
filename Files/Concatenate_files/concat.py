import sys

def main():
	ilosc_argumentow=len(sys.argv)

	if ilosc_argumentow<3:
		exit("Podaj więcej argumentów linii poleceń!")

#Plik końcowy
	a=sys.argv[1]

#Wprowadzanie kolejnych plików wejściowych
	for i in range(2, ilosc_argumentow)
		filename=sys.argv[i]
	#Twoja treść właściwa programu, w pętli która wprowadza kolejne pliki do niej. Ja bym to wywalił do osobnej funkcji ale twoja wola :).
		with open(a+'.txt', 'a') as outfile:
			with open(fname) as infile:
				 outfile.write(str(fname)+':\n'+infile.read()+'\n')

if __name__ is "__main__":
	main()
