<br>

# 🎢 [1083 소트](http://www.acmicpc.net/problem/1083) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/12.svg"/>
<br>

## 📚 문제
![image](https://github.com/user-attachments/assets/1a84ae0e-1c47-41bf-a8a9-cf4174cd9c03)
<br>

## ⌨️ 입력
![image](https://github.com/user-attachments/assets/e037c7ad-e9fc-4e7e-b978-c16c3208ab82)
<br>

## 🏃‍♂️ 출력
> 첫째 줄에 문제의 정답을 출력한다.

<br>
<details>

  <summary> 
  
  ## 🎈 문제 풀이
  </summary>
  
## 🙈 문제에 대한 생각
> 1. 연속된 두 개의 원소만 교환할수 있기 때문에 양옆의 원소를 swap하는 방식으로 구상하였다.
> > - 조건
> > - 1. 사전순으로 가장 뒷서는 것 ->  내림차순으로 으로 정렬
> > - 2. S가 0이 될때 까지 정렬을 수행
> > - 3. 여기서 중요한 포인트 : 전체의 원소를 비교하는게 아니라 s의 범위를 고려해 양옆의 크기를 비교
> 2. 조건을 고려하면서 최댓값을 찾는다.
> 3. 최댓값의 index를 추출한다.

</br>

## 📄 중요 로직
>  최댓값을 찾기위해서 슬라이싱할때 현재 탐색중인 index위치부터 s만큼 더한 index까지의 범위를 선정
> 
>  두번째 for문에서 정렬되고 난 후 최댓값의 인덱스를 1 감소.

</br>

## 📜 전체 로직
> 1. 입력 3개 받기
> 2. N만큼 반복문을 수행
> 3. 최댓값과 최댓값의 index를 추출
> 4. 두번째 반복문 수행 (최댓값의 index가 현재 탐색중인 index와 같다면 종료 and s가 0이면 종료)
> 5. 내림차순 정렬 수행
> 6. s와 최댓값의 index를 1씩 감소시킨다.

## 🪄 참고 자료 
- https://letalearns.tistory.com/146

</details>
