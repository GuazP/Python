def zlicz(znaki):
	suma={}
	for i in znaki:
		suma[i]=suma.get(i,0)+1
	return suma

def main():
	test = zlicz(input("Wprowadź łańcuch znaków do sprawdzenia: "))
	print(test)
	test = open(input("Wprowadź nazwę pliku do sprawdzenia: "), "r")
	print(zlicz(test.read()))
    test.close()

if __name__ == "__main__":
    main()
