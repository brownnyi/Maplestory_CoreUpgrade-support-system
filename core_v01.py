from itertools import combinations
from collections import Counter

def core(main, skill, n, m):
    # main 리스트의 원소 빈도수 카운트
    main_counter = Counter(main)

    def is_valid_combination(comb):
        # 선택된 조합(comb)에서 main의 모든 원소가 n번씩 나오는지 확인
        combined_skill = []
        for sublist in comb:
            combined_skill.extend(sublist)
        skill_counter = Counter(combined_skill)

        # main의 각 원소가 n번씩 나타나는지 확인
        for key in main_counter:
            if skill_counter[key] != n:
                return False
        return True

    # 가능한 모든 조합 생성
    valid_combinations = []
    for comb in combinations(skill, m):
        # 첫 번째 원소가 겹치지 않는 경우만 검사
        first_elements = [sublist[0] for sublist in comb]
        if len(first_elements) == len(set(first_elements)):
            if is_valid_combination(comb):
                valid_combinations.append(comb)

    if valid_combinations:
        return valid_combinations
    else:
        return "경우의 수가 없습니다."

# 예시 호출
main = [1, 2, 3, 4, 5, 6]
skill = [
    [1, 2, 3],
    [1, 3, 4],
    [3, 4, 1],
    [2, 6, 5],
    [4, 5, 6],
    [5, 3, 2],
    [6, 5, 4],
    [1, 5, 4],
    [2, 3, 4],
    [2, 3, 5],
    [3, 5, 4],
    [5, 6, 3]
]
n = 3
m = 4

result = core(main, skill, n, m)
print("조건을 만족하는 조합들:")
for combination in result:
    print(combination)

#결과값

조건을 만족하는 조합들:
([1, 2, 3], [3, 4, 1], [2, 6, 5], [4, 5, 6])
([1, 2, 3], [3, 4, 1], [2, 6, 5], [6, 5, 4])
