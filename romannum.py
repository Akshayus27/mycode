R = {'I': 1, 'V': 5, 'X': 10}
l = str(input())
r = l.upper()
r1 = []
c = 0
for items in r:
    r1.append(R[r[c]])
    c += 1
sum = 0
d = 0
while(d < len(r1)):
    if(d+1 < len(r1)):
      if(r1[d] >= r1[d+1]):
        sum = sum + r1[d]
      else:
        sum = sum + (r1[d+1] - r1[d])
        d += 2
    else:
      sum = sum + r1[d]
    d += 1
print(sum)
