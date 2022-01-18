'''Funkce pro výpočet sériového obvodu'''
def serial(number1, number2):
    z = number1+number2
    print(z)
    print("")

'''Funkce pro výpočet paralelního obvodu'''
def parallel(number1, number2):
    z = 1 / (1 / number1 + 1 / number2)
    z = round(z, 2)
    print(z)
    print("")

while True:

    x = input("Jaký typ obvodu chceš vypočítat sériový/paralelní [s/p] pro ukončení napiš [e]\n> ").lower()

    if x.startswith("s"):
        s1 = int(input(">"))
        s2 = int(input(">"))
        print("――――――")
        serial(s1, s2)
  
    elif x.startswith("p"):
        p1 = int(input(">"))
        p2 = int(input(">"))
        print("――――――")
        parallel(p1, p2)

    elif x.startswith("e"):
        break
