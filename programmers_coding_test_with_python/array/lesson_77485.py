def solution(rows, columns, queries):
    answer = []
    map = []
    i = 1

    for row in range(0, rows):
        temp_list = []

        for column in range(0, columns):
            # print(f"{row}행 {column}열")
            temp_list.append(i)
            i += 1

        map.append(temp_list)

    for query in queries:
        print(query)

        row1, column1 = query[0], query[1]
        row2, column2 = query[2], query[3]
        print(row1, column1, row2, column2)

        start = [row1, column1]
        end = [row2, column2]
        print(start, end)

        width = abs(start[1] - end[1]) + 1
        height = abs(start[0] - end[0]) + 1

        print(f"가로: {width}, 세로: {height}")

        for w in range(width, width * 2):
            for h in range(height, height * 2):
                print(w, h)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
