def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n,m % n)

print gcd(24,16)
print gcd(255,25)
