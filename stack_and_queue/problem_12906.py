def solution(arr):
    queue = []
    count = 0

    for a in arr:
        if count == 0:
            queue.append(a)
            count += 1
        else:
            popped_number = queue.pop()
            queue.append(popped_number)
            if popped_number == a:
                continue
            else:
                queue.append(a)

    return queue


print(solution([4, 4, 4, 3, 3]))
