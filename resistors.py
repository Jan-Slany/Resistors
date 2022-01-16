#funkce na vypočítání sériovích rezistorů
def serial(number1, number2):
	z = number1+number2
	print(z)
	print("")

#funkce na vypočítání paralelních rezistorů
def parallel(number1, number2):
	z = 1 / (1 / number1 + 1 / number2)
	z = round(z, 2)
	print(z)
	print("")

while True:

	x = input("Choose: Serial/Parallel ")

#třídění inputu, na typ rezistorů které chceme vypočítat

	#pokud napíšeme s, aktivuje se funkce na výpočet sériovích rezistorů
	if x.startswith("s"):
		s1 = int(input())
		s2 = int(input())
		print("――――――")
		serial(s1, s2)

	#pokud napíšeme p, aktivuje se funkce na výpočet paralelních rezistorů	
	elif x.startswith("p"):
		p1 = int(input())
		p2 = int(input())
		print("――――――")
		parallel(p1, p2)

	#ukončení loopu
	elif x.startswith("e"):
		break