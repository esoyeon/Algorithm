# 조건
# 기둥(0)일 경우 -> 바닥(y=0), 왼쪽 보(x-1, y, 1), 제자리 보(x, y, 1), 다른 기둥 위(x, y-1, 0)
# 보(1)일 경우 -> 아래 기둥(x,y-1,0), 오른쪽 기둥(x+1, y-1, 0), 왼쪽과 오른쪽에 보 (x-1, y, 1)&(x+1, y, 1)


def check(answer):
    for x, y, structure in answer: 
        if structure == 0 : #기둥
            if y == 0 or (x, y-1,0) in answer or (x-1, y, 1) in answer or (x, y, 1) in answer:
                continue
            else:
                return False
        else: #보
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x-1, y, 1) in answer and (x+1, y, 1) in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = set() #set으로 중복제거하는 것이 in 연산자에서 효율적

    for x, y, structure , action in build_frame:
        xys = (x, y, structure)
        if action == 1: #설치
            answer.add(xys) #일단 설치 
            if not check(answer): #문제발생하면 삭제
                answer.remove(xys)
        else: # 삭제
            answer.remove(xys) #일단 삭제
            if not check(answer): #문제 발생하면 다시 추가
                answer.add(xys)
    
    # 정렬
    answer = [list(ans) for ans in answer]
    answer.sort()

    return answer



build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5

print(solution(n, build_frame))