#Ide ne írjatok egyedi bekérést, azt a def-be rakjátok pl def METÓDUSNEVE(szam1,szam2 stb..): és utána a DEF-ben kérjetek be számot az usertől
#Írta:
def haromszogKerulet(szam):
number1 = float(input (" Kerület <cm>: "))
number2 = float(input (" Terület <cm>: "))
number1 = float(input (" Kerulet <cm>: "))
number2 = float(input (" Terulet <cm>: "))
	return szam
def haromszogTerulet(szam):
	return szam
#Írta:
def korTerulet(szam):
	result = number1*number2
	return result
def korTerulet(szam):
	return szam
	
#Írta:
def teglalapKerulet(szam):
	return szam
def teglalapTerulet(szam):
	return szam
	
	
#Írta:Patrícia
	a=float(input("Adja meg a téglalap a oldalát <cm>:"))
	b=float(input("Adja meg a téglalap b oldalát <cm>:"))
def teglalapKerulet(szam):
	szam1=a*2 + b*2
	return szam1
def teglalapTerulet(szam):
	szam2= a*b
	return szam2
	
	
#Írta:
def nyolcszogKerulet(szam):
	return szam
def nyolcszogTerulet(szam):
	return szam


#Fő program: Dávid
print("Válassz:")
print("1: Háromszög terület-kerület")
print("2: Kör terület-kerület")
print("3: Téglalap terület-kerület")
print("4: Nyolcszög terület-kerület")
szamValasztas=int(input("Írd be a megfelelő számot, melyik induljon el:"))
#Háromszög
if szamValasztas == 1:
	print("A háromszög kerülete",haromszogKerulet(szam))
	print("A háromszög területe",haromszogTerulet(szam))
#Kör
elif szamValasztas == 2:
	print("A kör kerülete",korKerulet(szam))
	print("A kör területe",korTerulet(szam))
#Téglalap
elif szamValasztas == 3:
	print("A téglalap kerülete",teglalapKerulet(a,b))
	print("A téglalap területe",teglalapTerulet(a,b))
#Nyolcszög
elif szamValasztas == 4:
	print("A nyolcszög kerülete",nyolcszogKerulet(szam))
	print("A nyolcszög területe",nyolcszogTerulet(szam))
else:
	print("Nem jó számot írtál be!")
	