<br>

# 🎢 [H-index](https://school.programmers.co.kr/learn/courses/30/lessons/42747) **[ Lv 2 ]**
<br>

## 📚 문제
![image](https://github.com/user-attachments/assets/f389fc78-f52e-443a-bcb2-97c3f269e5e9)
<br>
## 🗒️ 제한사항
![image](https://github.com/user-attachments/assets/9ffed4f6-f11a-43fd-80b2-968ebd3831d1)
<br>
## ⌨️ 입출력
![image](https://github.com/user-attachments/assets/a5e31732-bbad-4d6d-a4af-8ec74c7f209b)
<br>
## 💻 입출력 예 설명
> 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다.
> 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.
<br>
<details>

  <summary> 
  
  ## 🎈 문제 풀이
  </summary>
  
## 🙈 문제에 대한 생각
> 논문이 인용된 횟수를 h , h 번이상 인용된 논문의 개수를 t , h번 이하 인용된 논문의 개수를 m 이라고 할때
> - ### m <= h <= t 가 성립된다.
> 위의 조건을 생각하며 문제를 풀자.

</br>

## 📄 중요 로직
> 이중 반복문 중 첫 번째 반복문을 리스트의 크기 + 1 만큼 수행한다.
> t >= h(code에서 i에 해당) 일때 현재 h의 값을 리스트에 저장한다.
> t < h(code에서 i에 해당) 일때 이중 반복문 중 마지막 반복문을 빠져나간다.
> h의 최댓값을 구한다.

</br>

## 📜 전체 로직
> 1. parameter로 받은 리스트의 크기를 저장
> 2  h를 구하기위한 리스트
> 3. 반복문 size_c + 1 까지 돌림
> 4. 문제에서 논문의 개수에 해당하는 변수 t를 선언 및 0으로 초기화
> 5. 반복문을 통해 c 리스트의 원소를 탐색
> 6. i가 c원소인 j보다 작거나 같은경우 t를 1증가
> 7. t가 i보다 크거나 같은경우 i를 tmp리스트에 push
> 8. t가 i보다 작은경우는 조건에 부합하지 않기때문에 반복문 탈출
> 9. 여러개의 h중 최댓값을 추출
> 10. 출력

</details>
<!-- ## 🪄 참고 자료 --!> 
