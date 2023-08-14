import string


def solution(numbers):
    answer = 0

    number_dictionary = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    for word in number_dictionary.keys():
        numbers = numbers.replace(word, str(number_dictionary[word]))

    answer = numbers

    return answer


print(solution("onetwothreefourfivesixseveneightnine"))
