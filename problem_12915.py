# def solution(strings, n):
#     answer = []
#     real_answer = []
#
#     for string in strings:  # 문자열의 n 번째에 위치하는 문자를 따로 모은다.
#         nth_word = string[n]
#         answer.append(nth_word)
#
#     answer.sort()  # 모은 문자를 오름차순으로 정렬한다.
#
#     for word in answer:  # 정렬된 문자를 활용해서,
#         for string in strings:
#             if string[n] == word:  # 문자열의 n 번째 문자와 정렬된 문자가 같으면 반환할 값에 추가한다.
#                 real_answer.append(string)
#
#     real_answer = set(real_answer)
#     real_answer = list(real_answer)
#     real_answer.sort()
#
#     return real_answer
#
#
# def solution(strings, n):  # ChatGPT의 도움을 받아 작성된 code이다.
#     sorted_strings = sorted(strings, key=lambda x: (x[n], x))
#
#     return sorted_strings


def solution(strings, n):
    sorted_strings = sorted(sorted(strings), key=lambda x: x[n])

    return sorted_strings


print(solution(["abce", "abcd", "cdx"], 2))

# lambda x: x[n]: x를 매개 변수로 사용하여, x의 n번째 문자를 반환한다.
# lambda의 다른 예로는 다음과 같다.
# lambda x, y: x + y는 x와 y를 매개 변수로 사용하며, x + y를 계산하고 해당 값을 반환한다.
