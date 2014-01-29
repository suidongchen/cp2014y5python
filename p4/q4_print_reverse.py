def reverse_int(n):
    n=str(n)
    lst=[]
    for digit in n:
        lst.append(str(digit))
    lst.reverse()
    ans=''
    for item in lst:
        ans+=str(item)
    return ans

print reverse_int(12345)
