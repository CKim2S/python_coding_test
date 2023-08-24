# 부분 통과한 code이다. 수정이 필요하다.

def solution(N, stages):
    answer = []
    total_players = len(stages)

    print(f"answer: {answer}, total_players: {total_players}")

    fail_percents = {}

    for stage in range(1, N + 1):
        failed_players = stages.count(stage)

        fail_percent = failed_players / total_players

        fail_percents[stage] = fail_percent

        total_players = total_players - failed_players

        print(
            f"stage: {stage}, failed_player: {failed_players}, fail_percent: {fail_percent}"
        )

    def sort_key(stage):
        return fail_percents[stage]

    print(fail_percents)

    answer = sorted(fail_percents, key=sort_key, reverse=True)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# Print like [3,4,2,1,5]

# .count(): list, string, tuple과 같은 반복 가능한 객체에서 사용 가능하다.
# 특정 원소의 개수를 반환한다.
# list = [1, 1, 3, 4]
# list.count(1)은 int type인 2가 반환된다.

# sorted(): python 내장 함수로, 특정 인수 없이는 기본적으로 오름차순으로 정렬시킨다.
# 인수에는 key, reverse가 있으며, key 인수의 활용 방법은 다음과 같다.
# words = ["apple", "banana", "cherry"]
# sorted_words = sorted(words, key=len)
# 출력은 ['apple', 'cherry', 'banana']이 된다.
# reverse 인수의 활용 방법은 다음과 같다.
# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list = sorted(my_list, reverse=True)
# 출력은 [9, 5, 4, 3, 1, 1]이 된다.
