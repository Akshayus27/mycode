n = str(input())
n1 = n.split(" ")
K = int(n1[1])
N = list(range(1,int(n1[0])+1))
sum = 0
i = 1
while(i <= K):
    sum = sum + i
    i += 1
print(sum)
