#9단계

#팩토리얼
def fa(n):
    if n <= 1:
        return 1
    else:
        return n * fa(n-1)

N = int(input())

print(fa(N))

#피보나치 수5
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))

#재귀함수가 뭔가요?
n = int(input())

def recur(i, n):
    print("____"*i + '"재귀함수가 뭔가요?"')
    if i == n:
        print("____"*i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print("____"*i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print("____"*i + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("____"*i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recur(i+1, n)
    print("____"*i + "라고 답변하였지.")


print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recur(0, n)

#별 찍기 - 10
import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))
