def exp(x,n):
    if n == 0:
        return 1
    else:
        return x*exp(x,n-1)
exponential = exp(2,3)
print exponential
