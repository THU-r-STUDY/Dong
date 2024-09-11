import sys

stack = []
# 실행할 명령의 개수를 담을 변수 선언
count = int(sys.stdin.readline())
# 명령어 입력
for i in range(count):
    # 명령어 입력
    command = sys.stdin.readline().split()
    #명령 1
    if command[0] == '1':
        stack.append(command[1])
    #명령 2
    elif command[0] == '2':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    #명령 3
    elif command[0] == '3':
        print(len(stack))
    #명령 4
    elif command[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    #명령 5
    elif command[0] == '5':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)