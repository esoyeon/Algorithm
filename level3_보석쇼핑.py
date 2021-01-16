from collections import Counter

def solution(gems):
    # 시작은 리스트의 맨 앞과 맨 뒤 인덱스 
    answer = [0, len(gems)]
    # 보석리스트 안에 unique한 원소의 개수
    n = len(set(gems))
    #l, r 포인터를 움직임. r은 최소길이인 n부터 시작
    l, r = 0, n
    # 리스트 안에 각 원소의 개수를 센다 -> 딕셔너리 형태로 나옴
    dic = Counter(gems[l:r]) 

    while (l >= 0 and r < len(gems) and l < len(gems)): # 두 포인터가 인덱스 범위를 넘어가면 탐색 중단
        # 딕셔너리 안에 저장된 개수와 중복되지 않은 원소의 개수가 같을 경우 -> 최선이면 return; 아니면 범위 축소 
        if len(dic) == n: 
            # 이전 포인터 거리보다 현재 포인터 거리가 더 작을 경우
            if answer[1] - answer[0] > r - l:
                # 정답의 위치값갱신
                answer = [l, r]
            
            dic[gems[l]] -= 1
            # 만약 개수가 0이 되면, 아예 삭제 
            if dic[gems[l]] == 0:
                del dic[gems[l]]
                # l 포인터 1 증가 
            l += 1

        # 딕셔너리 안에 저장된 개수와 중복되지 않은 보석의 개수가 같지 않은 경우 -> 즉 범위 증가해야 함
        else: 
            k = gems[r]
            r += 1
            if len(gems) == r:
                break
            else:
                dic[k] += 1

    return [answer[0]+1, answer[1]]

gems1  = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems2  = ["AA", "AB", "AC", "AA", "AC"]
gems3 = ["XYZ", "XYZ", "XYZ"]
# print(solution(gems))
print(solution(gems1))
