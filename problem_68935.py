def solution(n):
    answer = ""
    quotient = 0  # 몫
    remainder = 0  # 나머지
    while True:
        quotient = n // 3
        remainder = n - quotient * 3
        n = quotient

        answer = answer + str(remainder)

        print(f"n: {n}, 몫: {quotient}, 나머지: {remainder}")

        if quotient == 0:
            break

    total = 0
    jisu = len(answer)

    for word in answer:
        jisu -= 1
        total = total + int(int(word) * (3 ** jisu))
        print(word, total)

    return total


print(solution(125))

# bin(): 10 진수를 2 진수로 변환하여 반환한다.

# int(a, b): b 진수로 표현된 a 문자열을, b 진수로 계산하여 반환한다.
# int("101", 2)는 int 형의 5를 반환한다.