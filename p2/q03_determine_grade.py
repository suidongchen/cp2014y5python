x = int(input("Enter score: "))

if x<0 or x>100:
    print("Invalid! Score must be within 0 - 100. ")
elif x>=70:
    print("A")
elif x>=60:
    print("B")
elif x>=55:
    print("C")
elif x>=50:
    print("D")
elif x>=45:
    print("E")
elif x>=35:
    print("S")
elif x>=0:
    print("U")
