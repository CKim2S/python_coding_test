def solution(s):
    answer = True

    s_length = len(s)

    if s_length == 4:
        for s_word in s:
            if 48 <= ord(s_word) <= 57:  # ascii code에서 문자열로 숫자(0 ~ 9)를 표현했을 때의 범위
                continue
            else:  # 문자열로 숫자를 표현하지 않을 때
                return False
    elif s_length == 6:
        for s_word in s:
            if 48 <= ord(s_word) <= 57:  # ascii code에서 문자열로 숫자(0 ~ 9)를 표현했을 때의 범위
                continue
            else:  # 문자열로 숫자를 표현하지 않을 때
                return False
    else:  # 문자열의 길이가 4 혹은 6이 아닐 때
        return False

    return answer


print(solution("1234"))

# "문자열".isdigit(): 문자열에 숫자로만 이루어져 있는지를 확인한다. 숫자로만 구성되어 있다면 True를, 아니라면 False를 반환한다.