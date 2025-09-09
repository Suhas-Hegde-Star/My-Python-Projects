import tabala

def get_rela_variation(var):
    var = int(input("Enter the variation number (1-7): "))
    if var == 1:
        return tabala.rela_v1
    elif var == 2:
        return tabala.rela_v2
    elif var == 3:
        return tabala.rela_v3
    elif var == 4:
        return tabala.rela_v4
    elif var == 5:
        return tabala.rela_v5
    elif var == 6:
        return tabala.rela_v6
    elif var == 7:
        return tabala.rela_v7
    else:
        return "Invalid variation"