n = int(input())
val = list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_val = max(val[i : i+1+s])
    max_index = val.index(max_val)
    while max_index != i and s:
        val[max_index], val[max_index - 1] = val[max_index - 1], val[max_index]
        max_index -= 1
        s -= 1

print(*val)