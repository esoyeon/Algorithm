def solution(n, build_frame):
    answer = []

    m = n+1

    bar = [[0]*m for _ in range(m)]
    pillar = [[0]*m for _ in range(m)]

    for f in build_frame: 
        x, y, a, b = f
        # 기둥
        if a == 0 and b == 1:
            # 벽면 초과 x
            if 0<= x <= n and 0 <= y <= n-1:
                # 설치 
                if y == 0 or bar[x-1][y]==1 or bar[x][y]==1 or pillar[x][y-1]==1:
                    answer.append([x, y, 0])
                    pillar[x][y] += 1 

        
        # 보
        elif a == 1 and b == 1: 
            # 벽면 초과 x
            if 0 <= x <= n-1 and 0 < y <= n:
                # 설치
                if pillar[x][y] == 1 or pillar[x+1][y] == 1 or (bar[x-1][y] == 1 and bar[x+1][y]==1):
                    answer.append([x, y, 1])
                    bar[x][y] += 1

        # # 기둥 삭제 
        # elif a == 0 and b == 0:
        #     if_bar = bar.copy()
        #     if_pillar = pillar.copy()
        #     # 해당 기둥 삭제 
        #     if_pillar[x][y] -= 1

        #     check_list = [[x-1, y+1, 1, 1], [x, y+1, 1, 1], [x, y+1, 0, 1]]
        #     for c in check_list:
        #         x, y, a, b = c
        #         # 기둥
        #         if a == 0 and b == 1:
        #             # 벽면 초과 x
        #             if 0<= x <= n and 0 <= y <= n-1:
        #                 # 설치 
        #                 if y == 0 or if_bar[x-1][y]==1 or if_bar[x][y]==1 or if_pillar[x][y-1]==1:
        #                     count += 1
        #                 else:
        #                     break
        #         # 보
        #         elif a == 1 and b == 1: 
        #             # 벽면 초과 x
        #             if 0 <= x <= n-1 and 0 < y <= n:
        #                 # 설치
        #                 if if_pillar[x][y] == 1 or if_pillar[x+1][y] == 1 or (if_bar[x-1][y] == 1 and if_bar[x+1][y]==1):
        #                     count += 1
        #                 else:
        #                     break
            
        #     if count == len(check_list):
        #         answer.drop([x, y, 0])
            
        # # 보 삭제 
        # elif a == 1 and b == 0:
        #     if_bar = bar.copy()
        #     if_pillar = pillar.copy()
        #     # 해당 기둥 삭제 
        #     if_bar[x][y] -= 1

        #     check_list = [[x-1, y, 1,1], [x, y, 1, 1], [x, y, 0, 1], [x+1, y, 0, 1]]
        #     for c in check_list:
        #         x, y, a, b = c
        #         # 기둥
        #         if a == 0 and b == 1:
        #             # 벽면 초과 x
        #             if 0<= x <= n and 0 <= y <= n-1:
        #                 # 설치 
        #                 if y == 0 or if_bar[x-1][y]==1 or if_bar[x][y]==1 or if_pillar[x][y-1]==1:
        #                     count += 1
        #                 else:
        #                     break
        #         # 보
        #         elif a == 1 and b == 1: 
        #             # 벽면 초과 x
        #             if 0 <= x <= n-1 and 0 < y <= n:
        #                 # 설치
        #                 if if_pillar[x][y] == 1 or if_pillar[x+1][y] == 1 or (if_bar[x-1][y] == 1 and if_bar[x+1][y]==1):
        #                     count += 1
        #                 else:
        #                     break
            
        #     if count == len(check_list):
        #         answer.drop([x, y, 1])

    return answer

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5

print(solution(n, build_frame))