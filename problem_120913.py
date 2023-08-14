def solution(my_str, n):
    answer = []

    string_length = len(my_str)
    count = round(string_length / n)

    for i in range(0, count):
        answer.append(my_str[:n])
        my_str = my_str[n:]

    # print(count)

    return answer

print(solution("abc1Addfggg4556b", 6))

# 1. len(): 문자열에 속한 문자들의 총 개수를 반환한다.
# 2. round(): input으로 들어 온 숫자 값에 대해 반올림 연산을 진행한다.
# my_str[:n]: 0부터 n-1까지의 문자열을 출력한다.
# my_str[n:]: n부터 마지막까지의 문자열을 출력한다.