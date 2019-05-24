#函数

import math
#print("hello world","wenjie jiang");
#name = input()
#print(name)
a = 100
if a > 100:
 print(a)
else: 
 print(-a)

 #函数
def move(x,y,step,angle):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
print(move(1,2,10,30))

#默认参数
def power(x,n=3):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))

#可变参数
def calu(*number):
    sum=0
    for n in number:
        sum=sum+n*n
    return sum
nums=[1,2,3]
print(calu(*nums))
print(calu(1,2))

#必选参数、默认参数、可变参数、关键字参数和命名关键字参数
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
def f1(a,b,c=0,*args,**kw):
       print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)  

f1(1, 2, 3, 'a', 'b', x=99)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print("递归函数",fact(50))





