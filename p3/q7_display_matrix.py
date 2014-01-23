import random
lst=[]

def print_matrix(n):
    for j in range(n):
        for i in range(n):
            lst.append(str(random.randint(0,1)))
            print lst[n*j+i],
        print
            
x = int(input("Please enter an integer: "))
print_matrix(x)    
