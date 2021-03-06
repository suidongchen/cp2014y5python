def gcd(n1, n2):
    if n1 > n2:
        small=n2
        big=n1
    else:
        small=n1
        big=n2

    if small == 0:
        return big
    else:
        return gcd(small, big-small)

n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))

gcd = gcd(n1, n2)
print gcd

# This method might be more efficient than the suggested method, especially when dealing with huge numbers!
# However, it fails when n1 and n2 are too far away, such as gcd(2512,2). 
