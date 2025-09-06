

def asktabala(wanted):
    while True:
        wanted = input("Write the lesson you want (Basic Words)\n")
        if wanted.lower() == "lesson 1":
            print("Ti Ra Ki Ta")
        elif wanted.lower() == "lesson 2":
            print("Ti Ra Ki Ta Ta Ka")
        elif wanted.lower() == "lesson 3":
            print("Ke Ti Ra Ki Ta Ta Ka Ta")
        elif wanted.lower() == "lesson 4":
            print("Ke Ke Ti Ra Ki Ta Ta Ka Ta Ka")
        elif wanted.lower() == "rela":
            pass
        else:
            print("Invalid Input. Try again ")