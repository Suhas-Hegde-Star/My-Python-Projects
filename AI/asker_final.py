import asker_math
import asker_tabala

def askfinal(wante):
    while True:
        wante = input("Write the topic you want")
        if wante.lower() == "math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "i want to do some math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "do some math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "i want to learn math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "maths":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "i wanna to do some math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "i wanna learn math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "i wanna do some tabala":
            asker_tabala.asktabala(wanted = any)
        elif wante.lower() == "do some tabala":
            asker_tabala.asktabala(wanted = any)
        elif wante.lower() == "i want to do some tabala":
            asker_tabala.asktabala(wanted = any)
        elif wante.lower() == "i want to learn tabala":
            asker_tabala.asktabala(wanted = any)
        elif wante.lower() == "tabala":
            asker_tabala.asktabala(wanted = any)
        else:
            print("Invalid Input. Try again ")