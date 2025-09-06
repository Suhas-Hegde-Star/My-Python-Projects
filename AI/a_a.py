import math

def square(num, sq):
    num = int(input("Enter the number "))
    sq = num ** 2
    print("The square of", num, "is", sq)

def root(num, rot):
    num = int(input("Enter the number "))
    rot = math.sqrt(num)
    print("The square root of", num, "is", rot)

def cube(num, cu):
    num = int(input("Enter the number "))
    cu = num ** 3
    print("The cube of", num, "is", cu)

def cube_root(num, cr):
    num = int(input("Enter the number "))
    cr = math.pow (num, 1/3)
    print("The cube root of", num, "is", cr)

def exponentation(num, ra, ans):
    num = int(input("Enter the base "))
    ra = int(input("Enter the exponent "))
    ans = num ** ra
    print("The number", num, "raised to", ra, "is", ans)

def circle(rad, area):
    rad = float(input("Enter the Radius of the Circle "))
    area = math.pow(rad, 2) * math.pi
    print("The area of the circle with", rad, "as the radius is", area)

def square(side, area):
    side = float(input("Enter the Length of the Square "))
    area = math.pow(side, 2)
    print("The area of the square with", side, "as the length is", area)

def volume(length, breadth, height, vol):
    length = float(input("Enter the Length of the Cuboid "))
    breadth = float(input("Enter the Breadth of the Cuboid "))
    height = float(input("Enter the Height of the Cuboid "))
    vol = length * breadth * height
    print("The volume of the cuboid with", length, "as the length,", breadth, "as the breadth, and", height, "as the height is", vol)

def surface(length, breadth, height, sa):
    length = float(input("Enter the Length of the Cuboid "))
    breadth = float(input("Enter the Breadth of the Cuboid "))
    height = float(input("Enter the Height of the Cuboid "))
    sa = 2 * (length * breadth + breadth * height + height * length)
    print("The surface area of the cuboid with", length, "as the length,", breadth, "as the breadth, and", height, "as the height is", sa)

def fibonacci(n):
    n = int(input("Till Which fibonacci number do you want? "))
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(fib_sequence)