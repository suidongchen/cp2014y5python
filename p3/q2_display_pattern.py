def display_pattern(n):
    lst=[]
    lst_last=[]
    for p in range(1,n+1):
        p=str(p)
        lst_last.append(p)
    lst_last.reverse()
    last=" ".join(lst_last)
    k=len(last)

    
    for i in range(1,n+1):
        for j in range(1,i+1):
            j=str(j)
            lst.append(j)
        lst.reverse()
        " ".join(lst)
        print "{0:>20s}".format(lst)
        lst=[]




n = input("Enter a number: ")
display_pattern(n)
