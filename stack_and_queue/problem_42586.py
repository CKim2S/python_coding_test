def solution(progresses, speeds):
    answer = []

    for i in range(0, len(progresses)):
        count = 0

        if progresses[i] != 100:
            while progresses[i] < 100:
                progresses[i] += speeds[i]
                count += 1

        answer.append([progresses[i], count])

    print(answer)
    answer2 = []
    count = 1
    for i in range(0, len(progresses) - 1):
        print(answer[i][1])

        if answer[i][0] < answer[i + 1][0]:
            count += 1
        else:
            answer2.append(count)
            count = 1

    return answer2


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
