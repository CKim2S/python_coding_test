# import math
#
#
# def solution(clothes):
#     answer = 1
#     count_dictionary = {}
#
#     for cloth in clothes:
#         category = cloth[1]
#
#         if not category in count_dictionary.keys():
#             count_dictionary[category] = 1
#         else:
#             count_dictionary[category] += 1
#
#     n = 0
#
#     for count in count_dictionary.values():
#         n += count
#
#     answer = math.comb(n, 2)
#
#     return answer
#
#
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

import math


def solution(clothes):
    closet = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]

    print(closet)

    for value in closet.values():
        print(value)
        answer *= len(value) + 1

    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
