#10단계 브루트 포스

#블랙잭
n, m = map(int, input().split())
num = list(map(int, input().split()))
l = len(num)
ans = 0
for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if(num[i] + num[j] + num[k] > m):
                continue
            else:
                ans = max(ans ,num[i] + num[j] + num[k])

print(ans)

#분해합
N = int(input())
result = 0

for i in range(1, N + 1):
    tmp = i + sum(map(int,str(i)))

    if tmp == N:
        result = i
        break

print(result)

#덩치
n = int(input())
 
data = [] # 입력받은 정보를 저장할 리스트 data
ans = [] # 등수정보를 저장할 리스트 ans
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) 
 
for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: 
            count += 1 
    ans.append(count + 1) 
 
for d in ans:
    print(d,end=" ")
    
#체스판 다시 칠하기
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
