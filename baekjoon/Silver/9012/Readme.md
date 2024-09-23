<br>

# 🎢 [9012 괄호](http://www.acmicpc.net/problem/9012) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/7.svg"/>
<br>

## 📚 문제
![image](https://github.com/user-attachments/assets/1d8c7902-3c8c-41b4-b51c-5962187e6009)
<br>

## ⌨️ 입력
![image](https://github.com/user-attachments/assets/c76a071e-8712-4758-870f-58e59d5e578f)
<br>

## 🏃‍♂️ 출력
> 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

<br>
<details>

  <summary> 
  
  ## 🎈 문제 풀이
  </summary>
  
## 🙈 문제에 대한 생각
> 생각을 곰곰히 해본 결과 처음이 ')'이 아닐때 무조건 ()의 개수가 같으면 VPS이다.
>
> '('일때는 리스트에 append() 해주고 ')'일때는 pop()을 해준다.
>
> 파이썬에서는 리스트를 사용했지만 자료구조 '스택'을 생각 

</br>

## 📄 중요 로직
> 1. 처음이 ')'이 아닐경우
> 2. '('일때는 리스트에 append() 해주고 ')'일때는 pop()을 해준다.
> 3. 정상적으로 종료가 된 후 스택의 길이가 0 즉 스택이 empty상태가 되었을 때 'YES'를 출력
> 4. 다른 모든 경우는 'NO'를 출력한다.

</br>

## 📜 전체 로직
> 1. 입력 데이터 수를 저장하기 위한 변수를 선언 및 입력받기
> 2. 반복문을 입력데이터 수 만큼 수행
> 3. 테스트 케이스를 입력받음
> 4. 테스트 케이스 리스트를 전부 돌면서 위의 중요 로직 수행
> 5. 반복문이 잘 끝났을경우 'YES' 출력

</br>

## ⏳ 시간복잡도
> 시간복잡도 : O(N^2)
</details>
<!-- ## 🪄 참고 자료 --!>
