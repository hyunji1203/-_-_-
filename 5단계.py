#5단계 - 함수

#셀프넘버
numbers = list(range(1,10001))
remove_list=[]    
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_list.append(num)
for remove_num in set(remove_list):
    numbers.remove(remove_num)
for self_num in numbers:
    print(self_num)

#한수
N=int(input())
han = 99

if N < 100:
    han = N
else:
    for i in range(100, N+1):
        a=list(map(int,str(i)))
        if a[0]-a[1] == a[1]-a[2]:
            han+=1
            
print(han)

