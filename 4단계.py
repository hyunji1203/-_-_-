#4단계

#최소, 최대
n = int(input())

array=list(map(int,input().split()))
print(min(array), max(array))

#최댓값
list=[]

for i in range(9):
    x = int(input())
    list.append(x)

print(max(list))
print(list.index(max(list))+1)

#숫자의 개수
A=int(input())
B=int(input())
C=int(input())

result = list(str(A*B*C))

for i in range(10):
    print(result.count(str(i)))

#나머지
arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
print(len(set(arr)))

#평균
n = int(input())  
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list :
    new_list.append(score/max_score *100)  
test_avg = sum(new_list)/n
print(test_avg)