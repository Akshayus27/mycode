n = int(input())
n1 = []
for i in range(1, n+1):
  i = str(input())
  n1.append(sorted(i))
count = 0
g = 0
for g in range(g, len(n1)):
  if g < len(n1)-1:
    if n1[g]!= n1[g+1]:
      count += 1
    else:
      continue
  g -= 1
print(abs(len(n1)-count))
