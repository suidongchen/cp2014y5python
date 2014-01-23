def check_even(x):
    if x % 2 == 0:
        p = "even"
    else:
        p = "odd"
    print("{0} is {1}".format(x, p))
        
x = int(input("Enter number: "))
check_even(x)
