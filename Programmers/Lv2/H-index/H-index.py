def solution(c):
    size_c = len(c)                 # parameter로 받은 리스트의 크기를 지정
    tmp = list()                    # h를 구하기위한 리스트
    for i in range(size_c+1):       # 반복문 size_c + 1 까지 돌림
        t = 0                       # 문제에서 논문의 개수에 해당
        for j in c:                 # c 리스트의 원소를 탐색
            if i <= j:              # i가 c원소인 j보다 작거나 같은경우 t를 1증가
                t += 1 
        if t >= i:                  # t가 i보다 크거나 같은경우 i를 tmp리스트에 push
            tmp.append(i)
        else:
            break                   # t가 i보다 작은경우는 조건에 부합하지 않기때문에 반복문 탈출
        
    tmp = max(tmp)                  # 여러개의 h중 최댓값을 추출
    return tmp                      # 출력