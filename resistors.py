def serial(number1, number2):
	z = number1+number2
	print(z)

def parallel(number1, number2):
	z = 1 / (1 / number1 + 1 / number2)
	z = round(z, 2)
	print(z)

prompt = "Zadej cislo\n> "

while True:

	x = input("Paralelne/seriove [p/s], exit pro ukonceni [e]\n> ").lower()
	try:
		n1 = int(input())
		n2 = int(input())
	except Exception as e:
		print(f"Chyba: nebud dement\n\t{e}")

	if x.startswith("s"):
		serial(n1, n2)
	elif x.startswith("p`"):
			parallel(n1, n2)
	elif x.startswith("e"):
		break
