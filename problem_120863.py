def solution(polynomial):
    polynomial = polynomial.split()
    # polynomial = polynomial.split("+")
    answer = ""
    x_number = 0
    number = 0
    count = 0

    for word in polynomial:
        if "x" in word:
            x_count = []
            x_count = word.split("x")
            if x_count[0] == "":
                x_number += 1
                continue
            x_number += int(x_count[0])
            print(x_count[0])
        elif "+" in word:
            continue
        else:
            count = count + int(word)
            number = count

    answer = f"{x_number}x + {number}"
    if x_number == 1 and number == 0:
        answer = "x"

    elif number == 0:
        answer = f"{x_number}x"
    elif x_number == 1:
        answer = f"x + {number}"
    elif x_number == 1 and number == 0:
        answer = f"x"
    elif x_number == 0:
        answer = f"{number}"


    return answer


print(solution("x + 0"))
