from collections import deque
import sys

ds_count = int(sys.stdin.readline())
li_a = list(map(int, sys.stdin.readline().split()))
li_b = list(map(int, sys.stdin.readline().split()))
count = int(sys.stdin.readline())
li_c = list(map(int, sys.stdin.readline().split()))

queue = deque()

for i in range(ds_count):
    if li_a[i] == 0:
        queue.append(li_b[i])

for j in range(count):
    queue.appendleft(li_c[j])
    print(queue.pop(), end=' ')