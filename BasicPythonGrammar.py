def solution(answers):
    patterns = [[1,2,3,4,5],
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]
    
    scores = [0] * 3

    #답과 패턴을 비교
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns): 
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    #가장 높은 점수
    max_score = max(scores)
    #가장 높은 점수를 가진 패턴을 구하기
    high_scores= []
    
    for i, score in enumerate(scores):
        if max_score == score:
            high_scores.append(i+1)

    return high_scores

answer = [1,2,3,4,5]
print(solution(answer))