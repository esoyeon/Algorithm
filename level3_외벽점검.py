#idea 1: 제한조건에서 weak리스트와 dist리스트의 길이가 매우 짧다 -> 완전탐색 고려

#idea 2: 문제에서 찾는 값은 "투입해야 하는 친구의 최솟값"인데, 전체 친구의 수는 최대 8이다(dist의 길이)
#모든 친구를 무작위 나열해도(순열) -> 8! = 40,320으로 계산할 만한 수
# 따라서, 친구를 나열하는 경우의 수를 각각 확인 -> 최소 몇명 배치하면 되는 지를 게산하자

#idea 3: 원형 -> 원형을 일자로 -> 길이 두배 하면 됨

#idea 4: 시계방향, 반시계방향 -> 어차피 경로는 하나!, 시계방향에서 그 길을 가는 다른 점이 count될 것이므로, 굳이 방향고려 안해도 됨. 

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer

n, weak, dist = 12, [1, 5, 6, 10], [1,2,3,4] 
print(solution(n, weak,dist
))