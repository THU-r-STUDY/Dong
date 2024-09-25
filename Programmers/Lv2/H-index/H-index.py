def solution(c):
    size_c = len(c)
    tmp = 0
    for i in range(size_c):
        t = 0
        for j in c:
            if i <= j:
                t += 1
        else:
            if t >= i:
                tmp = t
            else:
                break
    if size_c == 1:
        tmp = 0
    elif tmp == size_c:
        return c[0]
    return tmp