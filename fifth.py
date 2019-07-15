s = str(input())
s1 = s.split(" ")
a = s1[0]
b = s1[1]
c = s1[2]
if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
else:
    print(c)
