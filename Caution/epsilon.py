import sys
#엡실론 출력
print(sys.float_info.epsilon) #2.220446049250313e-16
#부동소수점 수의 오차 검사
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a - b) #0이 아닌 5.551115123125783e-17값인 것을 확인할 수 있다.
if abs(a - b) < sys.float_info.epsilon:
    print("a와 b는 같은 값 입니다.")
else:
    print("a와 b는 다른 값 입니다.")
