def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []

    for i in arr1:
        temp = bin(i)[2:]

        while len(temp) < n:
            temp = "0" + temp

        map1.append(temp)

    for i in arr2:
        temp = bin(i)[2:]

        while len(temp) < n:
            temp = "0" + temp

        map2.append(temp)

    for i in range(0, n):
        temp = ""
        for j in range(0, n):
            if map1[i][j] == "0" and map2[i][j] == "0":
                temp = temp + " "
            else:
                temp = temp + "#"

        answer.append(temp)

    return answer