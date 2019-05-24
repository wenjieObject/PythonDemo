#高级特性

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#print([L[0], L[1], L[2]]);
 
def trim(s):
    result=''
    n=0
    length=len(s)
    while n<length:
        m=s[n:n+1]
        n=n+1
        if m==" ":
            continue
        else:
            result=result+m
            print(result)


#trim('  hello  world  ')
         
    

