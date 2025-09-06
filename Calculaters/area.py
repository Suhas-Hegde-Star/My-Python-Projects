import math
import sys

def circle(rad, area):
    rad = float(input("Enter the Radius of the Circle"))
    area = math.pow(rad, 2) * math.pi
    print("The area of the circle with", rad, "as the radius is", area)

def square(side, area):
    side = float(input("Enter the Length of the Square"))
    area = math.pow(side, 2)
    print("The area of the square with", side, "as the length is", area)

def rect(length, breadth, area):
    length = float(input("Enter the Length of the Rectangle"))
    breadth = float(input("Enter the Breadth of the Rectangle"))
    area = length * breadth
    print("The area of the square with", length, "length", "and", breadth, "breadth is", area)

def tri(o, t, th, waa, area, s):
    while True:
        waa = input("Is the tiangle equlateral(Type y or n)")
        if waa.lower() == "y":
            o = float(input("Enter the length of the side"))
            s = (o + o + o) / 2
            area = math.sqrt(s * (s - o) * (s - o) * (s - o))
            print("The area of the triangle is:", area)
        elif waa.lower() == "n":
            o = float(input("Enter the length of side a: "))
            t = float(input("Enter the length of side b: "))
            th = float(input("Enter the length of side c: "))
            s = (o + t + th) / 2
            area = math.sqrt(s * (s - o) * (s - t) * (s - th))
            print("The area of the triangle is:", area)
        else:
            print("Invalid Input. Try again")

def ask(wanted):
    while True:
        print("1. Area of Circle\n2. Area of a square\n3. Area of a Rectangle\n4. Area of a Triangle")
        wanted = input("Enter the Suitable Number or e to exit")
        if wanted == "1":
            circle(rad= any, area= any)
        elif wanted == "2":
            square(side= any, area= any)
        elif wanted == "3":
            rect(length= any, breadth= any, area= any)
        elif wanted == "4":
            tri(o= any, t=any, th= any, waa= any, area= any, s= any)
        elif wanted.lower() == "e":
            print("See you later.\nBye!!")
            sys.exit
        else:
            print("Sorry. Invalid Input")

ask(wanted= any)