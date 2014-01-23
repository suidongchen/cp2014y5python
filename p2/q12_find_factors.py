import math

def is_prime(x):
    if x == 1:
        return False # 1 is neither a prime nor a composite number!
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x))+1, 2):
            if x % i == 0:
                return False
                break
        return True

def factorise(y):
    factors = []
    while y % 2 == 0:
        y = y/2
        factors.append(2)

    for j in range(3, y+1, 2):
        k = y/j
        if y%j==0 and is_prime(k):
            factors.append(k)
    factors.sort()
    return factors


num = int(input("Enter a number: "))

print factorise(num)
