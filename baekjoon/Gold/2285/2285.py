# 함수 정의
import sys

def Calc_left(p):  #이러면 리스트를 새로 넘겨주어야함
    ds = 0
    for x in range(len(p)):
        ds += sum(p[ : x+1])
    return ds


def Calc_right(p):
    ds = 0
    for x in range(len(p)):
        ds += sum(p[x : ])
    return ds

cot = int(input())              # 마을의 수 입력
town = [None]*cot               # 마을 리스트
people = [None]*cot             # 사람의 수 리스트
dt = []                         # 최댓값 처리할 리스트


for x in range(cot):   # 마을수와 사람수를 입력
    town[x], people[x] = map(int, sys.stdin.readline().split())

for i in range(len(people)):
    #왼쪽리스트 생성
    if i == 0:
        dt.append(Calc_right(people[i+1 : ]))
    elif i == len(people):
        dt.append(Calc_left(people[ : i]))
    else:
        dt.append(Calc_left(people[ : i]) + Calc_right(people[i-1: ]))

dt_max = max(dt)

for x in range(len(dt)):
    if dt_max == dt[x]:
        print(x+1)
        break