import tabala

def asktabala(wanted):
    while True:
        wanted = input("Write the lesson you want (Basic Words)\n")
        if wanted.lower() == "lesson 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "lesson number 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "lesson 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "lesson number 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "lesson 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "lesson number 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "lesson 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "lesson number 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "i want lesson 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "i want lesson number 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "i want lesson 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "i want lesson number 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "i want lesson 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "i want lesson number 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "i want lesson 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "i want lesson number 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "want lesson 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "want lesson number 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "want lesson 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "want lesson number 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "want lesson 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "want lesson number 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "want lesson 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "want lesson number 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "rela":
            print(tabala.rela)
        elif wanted.lower() == "i want rela":
            print(tabala.rela)
        elif wanted.lower() == "want rela":
            print(tabala.rela)
        elif wanted.lower() == "want rela variation 1":
            print(tabala.rela_v1)
        elif wanted.lower() == "i want rela variation 1":
            print(tabala.rela_v1)
        elif wanted.lower() == "want rela variation 1":
            print(tabala.rela_v1)
        elif wanted.lower() == "rela_v1":
            print(tabala.rela_v1)
        elif wanted.lower() == "rela variation 1":
            print(tabala.rela_v1)
        elif wanted.lower() == "rela 1":
            print(tabala.rela_v1)
        elif wanted.lower() == "exit":
            break
        else:
            print("Invalid Input. Try again ")