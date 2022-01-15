def serial(nums: [float]) -> float:
	return sum(nums)

def parallel(nums: [float]) -> float:
	return round(1/sum([1/i for i in nums]), 2)

prompt = "Zadej cislo\n> "

while True:

	x = input("Paralelne/seriove [p/s], exit pro ukonceni [e]\n> ").lower()

	func = parallel
	if x.startswith("s"):
		func = serial
	elif x.startswith("e"):
		break

	nums = []
	try:
		while True:
			num = input("> ").strip()
			if num == "":
				break
			nums.append(int(num))

	except Exception as e:
		print(f"Chyba: nebud dement\n\t{e}")

	print(func(nums))
