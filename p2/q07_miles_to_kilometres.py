print("Miles Kilometers Kilometres Miles")


for miles in range(1,11):
    kilometers = 1.609*miles
    kilometres = 15 + 5*miles
    miles1 = kilometres/1.609
    
    miles = str(miles)
    kilometers = str("{0:.3f}".format(kilometers))
    kilometres = str(kilometres)
    miles1 = str("{0:.3f}".format(miles1))
    
    s1 = (6-len(miles))*" "
    s2 = (11-len(kilometers))*" "
    s3 = (11-len(kilometres))*" "

    print("{0}{1}{2}{3}{4}{5}{6}".format(miles,s1,kilometers,s2,kilometres,s3,miles1))
