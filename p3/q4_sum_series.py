def m_series(i):
    i=float(i)
    if i==1:
        return 1/2
    else:
        return m_series(i-1) + i/(i+1)

print "i         m(i)     "
for i in range(1,21):
    print " "*(10-len(i))+str(i)+"{0:.4f}".format(m_series(i))
