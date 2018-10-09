x = 11 #global
def first():
    y = 22 #local to first() nonlocal to second()
    print 'y: ',y
    def second():
        z = 33 #local
        print 'z: ',z
    second()
print 'x: ',x
first()
