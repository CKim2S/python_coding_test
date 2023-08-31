def solution(a, b):
    answer = []

    day_dictionary = {
        2: "SUN",
        3: "MON",
        4: "TUE",
        5: "WED",
        6: "THU",
        0: "FRI",
        1: "SAT",
    }

    month_dictionary = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    day_string = []

    while len(day_string) < 366:
        for i in range(0, 7):
            day_string.append(day_dictionary[i])

    while True:
        for i in range(1, 13):
            total_day = month_dictionary[i]
            answer.append(day_string[0:total_day])
            day_string = day_string[total_day:]
        break

    return answer[a - 1][b - 1]


print(solution(5, 24))
