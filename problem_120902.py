def solution(my_string):
    splitted_my_string = my_string.split()
    answer = int(splitted_my_string[0])

    for i in range(0, len(my_string.split())):
        if my_string.split()[i] == "+":
            answer = answer + int(my_string.split()[i + 1])
        elif my_string.split()[i] == "-":
            answer = answer - int(my_string.split()[i + 1])

    return answer


print(solution("3 + 4"))
