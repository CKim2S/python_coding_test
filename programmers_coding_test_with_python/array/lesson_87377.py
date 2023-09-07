# def solution(line):
#     answer = []
#     x_and_y = []
#
#     #
#     for i in range(0, len(line)):
#         A, B, E = line[i]
#         for j in range(i + 1, len(line)):
#             C, D, F = line[i + 1]
#
#             x = (B * F - E * D) / (A * D - B * C)
#             y = (E * C - A * F) / (A * D - B * C)
#
#             # 소수점을 가지고 있으면 정수로 변환하지 않는다.
#             if int(x) == x:
#                 x = int(x)
#             else:
#                 continue
#
#             if int(y) == y:
#                 y = int(y)
#             else:
#                 continue
#
#             x_and_y.append([x, y])
#
#     print(x_and_y)
#
#     maximum_x = max(x_y[0] for x_y in x_and_y)
#     maximum_y = max(x_y[1] for x_y in x_and_y)
#
#     print(maximum_x, maximum_y)
#
#     width = maximum_x * 2 + 1
#     height = maximum_y * 2 + 1
#
#     for i in range(0, width):
#         answer.append("." * height)
#
#
#
#     # x = (BF - ED) / (AD - BC), y = (EC - AF) / (AD - BC), Ax + By + E = 0, Cx + Dy + F = 0
#
#     return answer
#
#
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))

def solution(line):
    answer, pos = [], []

    for i in range(0, len(line)):
        A, B, E = line[i]
        # print(A, B, E)
        for j in range(i + 1, len(line)):
            C, D, F = line[j]
            # print(C, D, F)

            # 비교하려는 두 직선이 평행인 경우, 지나친다.
            if A * D == B * C:
                continue

            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)



    return answer


print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
