def gensquares1(n):
    for i in range(n):
        yield i ** 2

#problem  using return statement        
def gensquares2(n):
    for i in range(n):
        return i ** 2 #return 0**2

#returning a list of result.      
def gensquares3(n):
    l =[]
    for i in range(n):
        l.append(i**2)
    return l 
print 'gensquares1'  

a=gensquares1(5)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)

print 'gensquares2'
b=gensquares2(3)
print b
b = gensquares2(3)
print b
print 'gensquares3'
c=gensquares3(3)
print c 
