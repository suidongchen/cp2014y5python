def find_largest(alist):
    if len(alist)==1:
        return alist[0]
    elif alist[0] > alist[1]:
        del alist[1]
        return find_largest(alist)
    else:
        del alist[0]
        return find_largest(alist)


lst=[5, 1, 8, 7, 2 , 5, 6, 2, 7, 0, 16, 134, 33, -7, 0]
print find_largest(lst)
