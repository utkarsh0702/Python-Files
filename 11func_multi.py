def multi_result(x,y):
    x = 2
    y = [2,3]
    return y,x #return multiple new values in a tuple with optional
               #parenthesis omitted
a = 1
l = [1,2]
print 'a and l initially',a,l
a,l =  multi_result(a,l)
print 'now:',a,l


#print multi_result(a,l)
