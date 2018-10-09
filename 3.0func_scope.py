#scope of variables

x = 11 # global to entire file
def first():
    #x = 22 local to first, nonlocal to second
    #here x is a new variable only in the scope of function 'first'
    x = 22
    print x
    def second():
        #nonlocal is 3.X specific
        #here x is again a new variable only in the scope of function 'second'
        #global x
        x = 33
        print x
    second()


#accessing global x
print x

#calling function
first()

#after calling function value of global x will be:
print x
