def reverse_int(n):
    n=str(n)
    lst=[]
    for i in n:
        lst.append(i)

    lst.reverse()
    return "".join(lst)

x = input("Please enter a number: ")
print reverse_int(x)
