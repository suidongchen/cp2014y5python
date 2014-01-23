def m_series(i):
    i=float(i)
    if i==1:
        return 0.5000
    else:
        return m_series(i-1) + i/(i+1)

print "i         m(i)     "
for i in range(1,21):
    print str(i)+" "*(10-len(str(i)))+"{0:.4f}".format(m_series(i))
