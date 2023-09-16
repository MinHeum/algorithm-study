def solution(clothes):
    answer = 0

    # 1. 의상 종류별로 분류
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = [cloth[0]]
        else:
            clothes_dict[cloth[1]].append(cloth[0])

    # 2. 경우의 수 계산
    answer = 1
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    answer -= 1

    return answer