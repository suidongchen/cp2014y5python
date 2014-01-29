def sum_series1(i):
    if i==1:
        return 1
    else:
        return sum_series1(i-1)+1/float(i)
