def solution(nums):
    can_choose = int(len(nums) / 2)
    total = set(nums)

    return min(len(total), can_choose)

print(solution([3, 1, 2, 3]))
