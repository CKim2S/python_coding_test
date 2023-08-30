def solution(k, score):
    answer = []
    temp = []

    for i in range(0, len(score)):
        answer.append(score[i])

        if i >= k:
            answer.sort()
            answer.pop(0)

        temp.append(min(answer))

    return temp


print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
