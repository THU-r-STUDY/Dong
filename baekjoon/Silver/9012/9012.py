import sys

cot = int(sys.stdin.readline())

for i in range(cot):
    #스택 선언 및 for문 돌때마다 초기화
    stack = []
    # 입력 받기
    arr = sys.stdin.readline()
    for j in arr:
        # ( 일때 push
        if j == '(':
            stack.append('(')
        # ) 일때 pop
        elif j == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    else:  
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")