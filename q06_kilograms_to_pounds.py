print "Kilograms Pounds"
for a in range(1,11):
    b = 2.2 * a
    a = str(a)
    s = (10 - len(a))*" "
    print "{0}{1}{2:.1f}".format(a,s,b)
