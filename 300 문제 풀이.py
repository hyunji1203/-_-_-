#300,301,303 문제 풀이

#300
#나머지 - 10430
A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#소수 찾기 - 1978
n = int(input()) 
nums = list(map(int, input().split(' '))) 
resCnt = 0 

for i in nums:
    cnt = 0 
    if(i == 1): 
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        resCnt += 1
print(resCnt)

#팩토리얼 - 10872
def fa(n):
    if n <= 1:
        return 1
    else:
        return n * fa(n-1)

N = int(input())

print(fa(N))

#최소공배수 -1934
import sys

T=int(input())

for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    aa,bb=a,b

    while a%b!=0:
        a,b=b,a%b

    print(aa*bb//b)

# 최대 공약수와 최소공배수 - 2609
import math
a,b=map(int,input().split())
print(math.gcd(a,b),math.lcm(a,b))

#301
#2진수 8진수-1373
print(oct(int(input(),2))[2:])

#8진수 2진수 - 1212
print(bin(int(input(), 8)[2:]))