#2단계 풀이

#두 수 비교하기
a,b = map(int, input().split())
if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")

#시험성적
a= int(input())
if 90<=a:
    print("A")
elif 80<=a:
    print("B")
elif 70<=a:
    print("C")
elif 60<=a:
    print("D")
else:
    print("F")
    
#윤년
a=int(input())

if (a%4 == 0 and a%100 != 0 or a%400 == 0):
    print(1)
else:
    print(0)
    
#사분면 고르기
x = int(input())
y = int(input())

if (x>0 and y>0):
    print(1)
elif (x<0 and y>0):
    print(2)
elif (x<0 and y<0):
    print(3)
else:
    print(4)

#알람 시계
h,m=map(int, input().split())

if(m>=45):
    m = m - 45
else:
    if(h == 0):
        h = 23
    else:
        h = h - 1
        
    m = 60 + m - 45

print(h, m)