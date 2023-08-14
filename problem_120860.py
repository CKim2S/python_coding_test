def solution(dots):
    answer = 0
    width = 0
    height = 0

    for i in range(1, 4):
        if dots[0][0] == dots[i][0]:  # [1, 1]의 x 좌표를 다른 원소들의 x 좌표들과 비교
            height = abs(dots[0][1] - dots[i][1])
        elif dots[0][1] == dots[i][1]:
            width = abs(dots[0][0] - dots[i][0])

    return width * height
