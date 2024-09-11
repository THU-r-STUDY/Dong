queue = []

#큐 < 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

#큐 < 맨 앞 데이터 제거
item = queue.pop(0)
print(item) # 출력 : 1

# 큐 < 데이터 추가
queue.append(4)
queue.append(5)

#큐 < 맨 앞 데이터 제거
item = queue.pop(0)
print(item) # 출력 : 2