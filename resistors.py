while True:

    typ_zapojeni = input("Jaký typ obvodu chceš vypočítat sériový/paralelní [s/p]: ").lower()

    '''Funkce pro výpočet sériového obvodu'''
    if typ_zapojeni.startswith("s"):

        numbers = []
        serie = 0

        try:  
            while True:
                number = input(">").strip()
                if number == "":
                    serie += sum(numbers)
                    print("")
                    print("sérioví = {}".format(round(serie, 2)))
                    print("")
                    break
                numbers.append(int(number))

        except Exception as e:
            print("---Error---")
            print(e)
            print("")

    '''Funkce pro výpočet paralelního obvodu'''
    if typ_zapojeni.startswith("p"):

        numbers = []

        try:
            while True:
                number = input(">").strip()
                if number == "":
                    paralela = round(1/sum([1/i for i in numbers]), 2)  
                    print("")  
                    print("paralelní = {}".format(paralela))
                    print("") 
                    break
                numbers.append(int(number))

        except Exception as e:
            print("---Error---")
            print(e)
            print("")

    again = input("Chceš ještě počítat? ").lower()

    if again != "ano":
        break
    else:
        pass
