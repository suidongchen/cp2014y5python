def build_list(n):
    lst_last=[]
    for p in range(1,n+1):
        p=str(p)
        lst_last.append(p)
    lst_last.reverse()
    return lst_last

def display_pattern(m):
    for i in range(1,m+1):
        l_i = build_list(X)
        for item in l_i:
            if int(item) > i:
                l_i[l_i.index(item)] = " "*len(item)
        last=" ".join(l_i)
        print last

X = int(input("Enter a number: "))

display_pattern(X)
