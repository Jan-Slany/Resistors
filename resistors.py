def serial(number1, number2):
	z = number1+number2
	print(z)

def parallel(number1, number2):
	z = 1 / (1 / number1 + 1 / number2)
	z = round(z, 2)
	print(z)

while True:

	x = input("Paralelne/seriove [p/s]\n> ").lower()
	
	try:
		if x.startswith("s"):
			s1 = int(input())
			s2 = int(input())
			serial(s1, s2)

		elif x.startswith("p"):
			p1 = int(input())
			p2 = int(input())
			parallel(p1, p2)

	except Exception as e:
		print(f"Chyba: nebud dement\n\t{e}")
	
	if x.startswith("exit"):
		break