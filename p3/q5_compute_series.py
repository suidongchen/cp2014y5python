def m(x):
    s=0.0
    for p in range(2,2*x+1,4):
        s+=1/float(p*p-1)
    return 8*s


print "i    m(i)"

for i in range(1,20,2):
    print str(i) + (5-len(str(i)))*" " + "{0:.11f}".format(m(i))


