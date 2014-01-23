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

lst=[]
line=[]

for i in range(1,10000):
    if len(lst)==1000:
        break
    elif is_prime(i):
        lst.append(i)

for k in range(0,100):
    for n in range(0,10):
        print str(lst[k*10+n])+" "*(4-len(str(lst[k*10+n]))),
    print 

# I increased the distance between two consecutive prime numbers by 1*" " so that the numbers will not stick together.
