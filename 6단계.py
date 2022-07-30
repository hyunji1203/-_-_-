#6단계

#아스키 코드
a = input()
print(ord(a))

#숫자의 합
N = int(input())
X = list(map(int,str(input())))
hab = 0

for i in range(0,N):
    hab = hab +X[i]
    
print(hab)

#알파벳 찾기
s = input()
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in al:
    if i in s:
        print(s.index(i), end= ' ')
    else:
        print( -1, end =' ')

#문자열 반복
T = int(input())

for _ in range(T):
    a, b = map(str, input().split())
    
    for x in b:
      print(x*int(a),end="")
      
    print()
       
#단어 공부
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))])

#단어의 개수
a = list(input().split())

print(len(a))

#상수
a,b = input().split()
x=""
y=""

list(a)
list(b)

for i in range(2,-1,-1):
    x=x+a[i]

for i in range(2,-1,-1):
    y=y+b[i]
    
#다이얼
al=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
x = input()

time=0 

for i in al:
    for j in i:
        for k in x: 
            if k == j:
                time =time + al.index(i) + 3

print(time)
      