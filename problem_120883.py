def solution(id_pw, db):
    answer = ''

    id = id_pw[0]
    pw = id_pw[1]

    for i in range(0, len(db)):
        if id == db[i][0] and pw == db[i][1]:
            answer = "login"
            return answer
        elif id == db[i][0] and pw != db[i][1]:
            answer = "wrong pw"
        # elif id != db[i][0] and pw != db[i][1]:
        #     answer = "wrong pw"
        else:
            answer = "fail"

    return answer


print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))