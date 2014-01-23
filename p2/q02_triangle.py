side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
perimeter = side1 + side2 + side3
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("Perimeter = {0}".format(perimeter))
else:
    print("Invalid triangle!")
    
