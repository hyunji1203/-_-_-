#400~402 문제 풀기

#400
#1로 만들기 - 1463
n = int(input())
d = [0] * (n + 1)  

for i in range(2, n + 1):

    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) 
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])

#1,2,3 더하기 - 9095
import sys
read = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

T = int(read())
for _ in range(T):
    print(cache[int(read())])
    
#쉬운 계단 수 - 10844
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % MOD)

#401
#오르막 수 - 11057
n = int(input())

num = [1]*10

for i in range(n-1):
    for j in range(1, 10):
        num[j] += num[j-1]

print(sum(num)%10007)

#포도주 시식 - 2156
n=int(input())
array=[0]*10000
for i in range(n):
  array[i]=int(input())

d=[0]*10000
d[0]=array[0]
d[1]=array[0]+array[1]
d[2]=max(array[2]+array[0], array[2]+array[1], d[1])
for i in range(3,n):
  d[i]=max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])

print(max(d))

#타일 채우기 - 2133
N = int(input())

d = [0]*31
d[0] = 1

for i in range(2, N+1, 2):
    d[i] = d[i-2] * 3
    for j in range(0, i-2, 2):
        d[i] += d[j] * 2

print(d[N])

#402
#동물원 - 1309
import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
for i in range(n+1) :
    dp[i] = [0,0,0]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1


for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n]) % 9901)