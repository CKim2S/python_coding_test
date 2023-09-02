def solution(participant, completion):
    hash_dictionary = {}
    hash_sum = 0

    for part in participant:
        hash_dictionary[hash(part)] = part
        hash_sum += hash(part)

    for comp in completion:
        hash_sum -= hash(comp)

    return hash_dictionary[hash_sum]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
