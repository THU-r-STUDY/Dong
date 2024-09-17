cot = int(input()) # 회의 개수 입력
dta = [0]*cot # 회의를 담을리스트
n = 0

for i in range(cot):    # 회의 시작 시간, 끝나는 시간 리스트로 받기
    dta[i] = list(map(int, input().split()))

dta.sort(key=lambda x : x[1])              #회의끝나는 시간 기준으로 정렬

while n < len(dta) - 1:
    if dta[n][1] > dta[n+1][0]:        # 끝나는 시간, 시작 시간
        dta.pop(n+1)
    else:
        n += 1
print(len(dta))