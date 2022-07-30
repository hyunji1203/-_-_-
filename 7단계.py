#7단계

#손익분기점
a,b,c=map(int,input().split())

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
    
#벌집
n = int(input())

nums_pileup = 1  
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  
    cnt += 1  
print(cnt)

#분수찾기
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: 
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))

#달팽이는 올라가고 싶다
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int A,B,V;
    scanf("%d %d %d",&A,&B,&V);
    int day;
    
    if((V-A)%(A-B)==0)
        day= (V-A)/(A-B);
    else
        day= (V-A)/(A-B)+1;
    
    printf("%d\n",day+1);
 
}

#ACM 호텔
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  
        num = n//h
        floor = h
    print(f'{floor*100+num}')
    
#부녀회이 될테야
t = int(input())

for _ in range(t):  
    floor = int(input())  
    num = int(input())  
    f0 = [x for x in range(1, num+1)]  
    for k in range(floor):  
        for i in range(1, num):  
            f0[i] += f0[i-1]  
    print(f0[-1])  
 