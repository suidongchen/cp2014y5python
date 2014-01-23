def convert_ms(n):
    h=0
    m=0
    s=n//1000
    while s>= 3600:
        h+=1
        s-=3600
    while s>= 60:
        m+=1
        s-=60
    while m>= 60:
        h+=1
        m-=60
    return "{0}:{1}:{2}".format(h,m,s)

x=int(input("Please enter a period of time in milliseconds: "))
print convert_ms(x)
