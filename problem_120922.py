def solution(M, N):
    answer = 0
    square = [M, N]
    count = 0

    while True:
        if M != 1:
            M = M // 2
            N = N * 2
            count = count + 1
            print(count)
        else:
            for i in range(N, 1, N // 2):
                N = N // 2
                count = count + 1
                print(count)
            break

    return count


print(solution(2, 2))
