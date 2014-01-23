def display_pattern(n):
    x=""
    if 1<=n<=9:    
        for i in range(1,n+1):
            for j in range(i,0,-1):
                x=x+str(j)+" "
            space = (2n + 2i - 4)*" "
        print space + x
