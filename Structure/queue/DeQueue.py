from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

#큐의 맨 앞 데이터 제거
item = queue.popleft()
print(item) # 출력 : 1

#큐 < 데이터 추가
queue.append(4)
queue.append(5)

# 큐의 맨 뒤 데이터 제거
item = queue.pop()
print(item) # 출력 : 5