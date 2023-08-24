def solution(absolutes, signs):
    answer = 0

    for i in range(0, len(absolutes)):
        if signs[i] == True:
            continue
        else:
            absolutes[i] = 0 - absolutes[i]
    
    for absolute in absolutes:
        answer = answer + absolute

    return answer


print(solution([4, 7, 12], [True, False, True]))
