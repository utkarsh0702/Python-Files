a= input('Enter any string: ')
i=0
while a[i]!='\0':
    if upper(a[i]):
        a[i]= lower(a[i])
        i+=1
    else:
        a[i]= upper(a[i])
        i+=1

print(a)
