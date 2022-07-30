#8단계

#소수 찾기
n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)

#소수
start_num = int(input())
last_num = int(input())

sosu_list = []
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수리스트에 추가
            
if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)
    
#소수
N = int(input())  
d = 2  
while N != 1:
    if N % d != 0:
        d += 1
    else:
        N //= d
        print(d)
        
#소수 구하기
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
        
#소인수분해
n = int(input())

if n == 1:
    print('')

for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = n / i
        
#베르트랑 공준
import math
import sys

def is_prime(n) :
    if n == 2 :
        return True

    if n % 2 == 0 :
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False

    return True

while True:
    n = int(sys.stdin.readline())

    if n == 0 :
        break

    prime_cnt = 0

    for i in range(n+1, (2*n)+1) :
        if is_prime(i) :
            prime_cnt += 1

    print(prime_cnt)