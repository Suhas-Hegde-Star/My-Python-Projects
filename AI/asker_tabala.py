from AI.tab import get_rela_variation as t
from AI.tab import teen_taal as tt

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
            return t.get_rela_variation(var = any)
        elif wanted.lower() == "i want rela":
            return t.get_rela_variation(var = any)
        elif wanted.lower() == "want rela":
            return t.get_rela_variation(var = any)
        elif wanted.lower() == "want rela variations":
            return t.get_rela_variation(var = any)
        elif wanted.lower() == "i want rela variations":
            return t.get_rela_variation(var = any)
        elif wanted.lower() == "want rela variations":
            return t.get_rela_variation(var = any)
        elif wanted.lower() == "want 7 rela variations":
            return t.get_rela_variation(var = any)
        else:
            tt.teen_taal()