#3단계

#구구단
n = int(input())

for i in range(1,10):
    print(n,'*',i,'=',n*i)
    
#A+B-3
t = int(input())

for i in range(t):
    a,b=map(int, input().split())
    print(a+b)
    
#합
n = int(input())
sum =0

for i in range(1,n+1,1):
    sum +=i

print(sum)

#빠른 A+B
import sys
n = int(sys.stdin.readline())

for i in range(n):
    a,b =map(int, sys.stdin.readline().split())
    print(a+b)
    
#N 찍기
n =int(input())

for i in range(1,n+1):
    print(i)
    
#기찍 N
n = int(input())

for i in range(n,0,-1):
    print(i)

#A+B - 7
n = int(input())

for i in range(1, n+1):
    a,b=map(int,input().split())
    print("Case #"+str(i)+":",a+b)
    
#A+B - 8
n = int(input())

for i in range(1, n+1):
    a,b=map(int,input().split())
    print("Case #"+str(i)+":",a,"+",b,"=",a+b)
    
#별 찍기 -1
n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()
    
#별 찍기 -2
n = int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*",end="")
    print()