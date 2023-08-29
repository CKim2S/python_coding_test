def solution(strings, n):
    answer = []
    real_answer = []

    for string in strings:
        nth_word = string[n]
        answer.append(nth_word)

    answer.sort()

    for word in answer:
        for string in strings:
            if string[n] == word:
                real_answer.append(string)

    real_answer = set(real_answer)
    real_answer = list(real_answer)
    real_answer.sort()
    return real_answer


print(solution(["abce", "abcd", "cdx"], 2))