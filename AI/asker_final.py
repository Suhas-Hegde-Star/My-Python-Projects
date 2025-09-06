import asker_math

def askfinal(wante):
    while True:
        wante = input("Write the topic you want")
        if wante.lower() == "math":
            asker_math.askmath(wanted = any)
        elif wante.lower() == "tabala":
            pass
        else:
            print("Invalid Input. Try again ")