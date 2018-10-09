# Python matches names by position from left to right
def afunc(a,b,c):
    print a,b,c
afunc(1,2,3)
afunc(3,2,1)

print '*'*40

# Keyword arguments allow us to match by name, instead of by position.
def afunc(a,b,c):
    print a,b,c
    print c,a,b
    print b,a,c
afunc(c=3,a=1,b=2)

print '*'*40

# Defaults specify values for optional arguments that aren't passed
def afunc(a,b=2,c=3):
    print a,b,c
afunc(1)
afunc(1,4,5)

print '*'*40

# Arbitrary arguments
# '*' collects unmatched positional arguments in a tuple
def afunc(a,*args):
    print a,args
afunc(1,2,3)
afunc(1,2,3,4,5)

#'**' collects unmatched keyword arguments into a new dictionary.
def afunc(a,**args):
    print a,args
afunc(a=1,b=2,c=3)
afunc(1,b=2,c=3,d=4)

print '*'*40

# Unpacking arguments
def afunc(a,b,c,d):
    print a,b,c,d
args = (1,2,3,4)
afunc(*args)
args = [5,6,7,8]
afunc(*args)
args = {'a':1,'b':2,'c':3,'d':4}
afunc(**args)

