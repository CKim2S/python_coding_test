def solution(s):
    number_dictionary = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    print(number_dictionary.values())

    for key in number_dictionary.keys():
        print(key)
        if key in s:
            s = s.replace(key, str(number_dictionary[key]))

    return int(s)


print(solution("one4seveneight"))

# "문자열".replace(): 문자열 자체에서 replace 되는 것이 아니라, 그저 해당 값을 반환한다.
