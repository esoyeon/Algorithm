from collections import defaultdict

def solution(gems):
    # 첫 시작은 맨 앞과 맨 뒤의 인덱스 값이다.
    answer = [0, len(gems)]
    d = defaultdict(int)

    # 중복되지 않은 보석의 총 개수를 구한다.
    gems_size = len(set(gems))
    
    # gems에 들어있는 제일 처음 보석과 보석의 위치를 딕셔너리에 저장
    d[gems[0]] = 1

    # 투 포인터를 사용하여 탐색하므로 두 개의 포인터의 시작 값을 0으로 지정
    s, e = 0, 0
    
    # 두 개의 포인터가 gems의 인덱스 범위 밖으로 넘어가면 탐색 중단 
    while s < len(gems) and e < len(gems):
        # 중복되지 않은 보석의 총 개수와 딕셔너리에 저장된 개수가 같을 경우 
        if gems_size == len(d):
            # 이전의 포인터 사이의 거리보다 현재 포인터 사이의 거리가 더 작을 경우  
            if answer[1] - answer[0] > e - s:
                # 위치 값을 갱신
                answer = [s+1, e+1]
            # 딕셔너리에 저장된 시작 보석 인덱스 값을 -1 감소
            d[gems[s]] -= 1
            if d[gems[s]] == 0:
                del d[gems[s]]
            s += 1
        else:
            e += 1
            if e == len(gems):
                break
            d[gems[e]] += 1
    return answer

gems1  = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems2  = ["AA", "AB", "AC", "AA", "AC"]
gems3 = ["XYZ", "XYZ", "XYZ"]
# print(solution(gems))
print(solution(gems1))
