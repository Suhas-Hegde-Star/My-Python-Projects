import tabala
from AI.asker_tabala import wanted as h

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
    
def teen_taal():
    if h.lower() == "teen taal":
        return tabala.teen_taal
    elif h.lower() == "i want teen taal":
        return tabala.teen_taal
    elif h.lower() == "want teen taal":
        return tabala.teen_taal
    elif h.lower() == "i want to learn teen taal":
        return tabala.teen_taal
    elif h.lower() == "learn teen taal":
        return tabala.teen_taal
    elif h.lower() == "teach me teen taal":
        return tabala.teen_taal
    elif h.lower() == "teach teen taal":
        return tabala.teen_taal
    elif h.lower() == "want to learn teen taal":
        return tabala.teen_taal
    else:
        return teen_v1()
    
def teen_v1():
    if h.lower() == "teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "teach me teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "teach teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "want to learn teen taal v1":
        return tabala.teen_taal1
    elif h.lower() == "teen taal variation 1":
        return tabala.teen_taal1
    elif h.lower() == "teen taal variation one":
        return tabala.teen_taal1
    elif h.lower() == "teen taal v one":
        return tabala.teen_taal1
    elif h.lower() == "teen taal v 1":
        return tabala.teen_taal1
    elif h.lower() == "teen taal version 1":
        return tabala.teen_taal1
    elif h.lower() == "teen taal version one":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal variation 1":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal variation one":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal v one":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal v 1":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal version 1":
        return tabala.teen_taal1
    elif h.lower() == "i want teen taal version one":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal variation 1":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal variation one":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal v one":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal v 1":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal version 1":
        return tabala.teen_taal1
    elif h.lower() == "want teen taal version one":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal variation 1":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal variation one":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal v one":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal v 1":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal version 1":
        return tabala.teen_taal1
    elif h.lower() == "i want to learn teen taal version one":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal variation 1":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal variation one":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal v one":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal v 1":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal version 1":
        return tabala.teen_taal1
    elif h.lower() == "learn teen taal version one":
        return tabala.teen_taal1
    elif h.lower() == "teach me teen taal variation 1":
        return tabala.teen_taal1
    else:
        return "Invalid variation"