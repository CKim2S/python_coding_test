def solution(num):
    answer = 0
    count = 0

    while True:
        if num == 1:
            if count > 500:
                count = -1

            return count
        elif num % 2 == 0:
            num /= 2
            count += 1
        elif num % 2 != 0:
            num = num * 3 + 1
            count += 1


print(solution(626331))
