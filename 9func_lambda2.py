#jump table

L = [lambda x: x**2,  # Inline function defination
     lambda x: x**3,
     lambda x: x**4]  # A list of three callable function

for f in L:
    print f(2)
print "*"* 50    
print L[2](3)
print L[0](4)

#implementing using def
print '_'*50
print 
def f1(x):        # Define named functions
    return x**2

def f2(x):
    return x**3

def f3(x):
    return x**4

L = [f1,f2,f3]   # Reference by name

for f in L:
    print f(2)

print L[1](3)
