n = int(input())
K = int(input())
N = list(range(1,n+1))
sum = 0
i = 1
while(i <= K):
    sum = sum + i
    i += 1
print(sum)
