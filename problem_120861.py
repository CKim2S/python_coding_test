def solution(keyinput, board):
    position = [0, 0]
    arrow_dictionary = {
        "left": -1,
        "right": 1,
        "up": 1,
        "down": -1,
    }

    for word in keyinput:
        # print(word)
        if word == "left" or word == "right":
            position[0] = position[0] + arrow_dictionary[word]

            if position[0] > round((board[0] - 1) / 2):
                position[0] = position[0] - arrow_dictionary[word]
                continue
            if position[0] < -round((board[0] - 1) / 2):
                position[0] = position[0] - arrow_dictionary[word]

                continue
            # position[0] = position[0] + arrow_dictionary[word]
        else:
            position[1] = position[1] + arrow_dictionary[word]

            if position[1] > round((board[1] - 1) / 2):
                position[1] = position[1] - arrow_dictionary[word]
                continue
            if position[1] < -round((board[1] - 1) / 2):
                position[1] = position[1] - arrow_dictionary[word]
                continue
            # position[1] = position[1] + arrow_dictionary[word]

    answer = position

    return answer


print(solution(["down", "down", "down", "down", "down"], [7, 9]))