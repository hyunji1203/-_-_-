#11단계 - 정렬

#수 정렬하기
x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])
    
#수 정렬하기2
import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')

#수 정렬하기3
import sys
input = sys.stdin.readline

counts = [0] * 10001  
for _ in range(int(input())):
    counts[int(input())] += 1

for num in range(1, 10000+1):
    if counts[num] > 0:
        for _ in range(counts[num]):
            print(num)

#커트라인
def sol(nums,k):
    nums.sort(reverse=True)
    print(nums[k - 1])
 
n,k=map(int, input().split())
nums=list(map(int, input().split()))
sol(nums,k)

#통계학
import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_s = Counter(nums).most_common()
print(round(sum(nums) / n))
print(nums[n // 2])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(nums[-1] - nums[0])

#소트인사이드
n = int(input())
 
li = []
for i in str(n):
    li.append(int(i))
    
li.sort(reverse=True)
 
for i in li:
    print(i,end='')
    
#좌표 정렬하기
N=int(input())
arr=[]
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])
    
#좌표 정렬하기2
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[1], x[0]))
for i in so:
    print(i[0], i[1])

#단어 정렬
import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)