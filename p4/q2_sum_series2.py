def sum_series2(i):
    if i==1:
        return 1.0/3.0
    else:
        return sum_series2(i-1)+i/float(2*i+1)
