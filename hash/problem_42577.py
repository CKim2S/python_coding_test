def solution(phone_book):
    phone_book.sort()  # 오름차순 정렬

    for i in range(0, len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


print(solution(["123", "456", "789"]))

# "a"가 "abc"에 포함되어 있는지 확인하기 위해서는,
# if "a" in "abc":
#   print("포함")
# else:
#   print("미포함")
# 으로 확인할 수 있다.
# 또는 "abc".find("a")로도 같은 결과를 확인할 수 있다.
# "a"가 있다면 "a"가 위치한 index 값을 반환하고, 문자열 내에 없다면 -1을 반환한다.
