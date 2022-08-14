#200

#스택
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

#단어 뒤집기
import sys
N = int(input())

for _ in range(N):
    str = sys.stdin.readline().rstrip()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = " ".join(reverse_words)
    print(answer)

#괄호
a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')

#스택 수열
n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:    
        stack.pop()         
        answer.append("-")
    else:                   
        print("NO")         
        flag = 1            
        break               

if flag == 0:
    for i in answer:
        print(i)

#에디터
import sys

stack_l = list(input())
stack_r = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == "B" and stack_l:
        stack_l.pop()
    elif command[0] == "P":
        stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))

#큐
import sys

if __name__ == '__main__':
    N = int(input())
    queue = list()
    for i in range(N):
        code = sys.stdin.readline()
        if (code[:4] == 'push'):
            num = int(code[5:])
            queue.append(num)
        elif (code[:3] == "pop"):
            if (len(queue) == 0):
                print(-1)
            else:
                a = queue[0]
                queue.pop(0)
                print(a)
        elif (code[:4] == "size"):
            print(len(queue))
        elif (code[:5] == "empty"):
            if (len(queue) == 0):
                print(1)
            else:
                print(0)
        elif (code[:5] == "front"):
            if (len(queue) == 0):
                print(-1)
            else:
                print(queue[0])
        elif (code[:4] == "back"):
            if (len(queue) == 0):
                print(-1)
            else:
                print(queue[-1])

#요세푸스 문제
N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]  

answer = []  
num = 0

for t in range(N):
    num += K-1  
    if num >= len(arr):    
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')