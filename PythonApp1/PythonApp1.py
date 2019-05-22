import math
#print("hello world","wenjie jiang");
#name = input()
#print(name)
a = 100
if a > 100:
 print(a)
else: 
 print(-a)
def move(x,y,step,angle):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
print(move(1,2,10,30))

