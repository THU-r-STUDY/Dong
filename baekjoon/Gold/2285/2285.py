# 함수 정의
import sys

cot = int(sys.stdin.readline())              # 마을의 수 입력
sum = 0.0                         # 마을의 수의 합/2를 저장할 변수
n = 0.0                           # 각 마을에 도착할때마다 각 마을의 사람수를 더하는 변수
dt = [0]*cot


for x in range(cot):   # 마을수와 사람수를 입력
    dt[x] = list(map(int, sys.stdin.readline().split()))

dt.sort()              # 정렬

for a in dt:
    sum += a[1]
else:
    sum = sum / 2

for ans in dt:
    n += ans[1]
    if n >= sum:
        print(ans[0])
        break