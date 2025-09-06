import asker_math

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
            pass
        elif wante.lower() == "do some tabala":
            pass
        elif wante.lower() == "i want to do some tabala":
            pass
        elif wante.lower() == "i want to learn tabala":
            pass
        elif wante.lower() == "tabala":
            pass
        else:
            print("Invalid Input. Try again ")