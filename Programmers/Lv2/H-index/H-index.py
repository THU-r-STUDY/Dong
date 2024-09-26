def solution(c):
    size_c = len(c)
    tmp = list()
    for i in range(size_c+1):
        t = 0
        for j in c:
            if i <= j:
                t += 1
        else:
            if t >= i:  
                tmp.append(i)
            else:
                break
                
    tmp = max(tmp)
    return tmp