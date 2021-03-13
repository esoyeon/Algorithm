
# 조건 checking 하는 함수 
def check(i, j, n, m, visited, matrix):
    return (i >= 0 and i <= n-1 and j >= 0 and j <= m-1
    and visited[i][j] == False 
    and matrix[i][j] ) #i, j가 인덱스로 돌기 때문에 -1 해주기! 

# 위에 조건에 맞는 dfs를 돌 때는 count +1 해주기 
def dfs(count, matrix, visited, x, y):
    visited[x][y] = True
    n, m = len(matrix), len(matrix[0])

    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]

    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if check(nx, ny, n, m, visited, matrix):
            count[0] += 1
            dfs(count,matrix,visited, nx, ny)


# dfs 깊이중에 max값으로 출력 
def connectedCell(matrix):
    result = 0
    n, m = len(matrix), len(matrix[0])
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and matrix[i][j] == 1: #초기조건
                count = [1]
                dfs(count, matrix, visited, i, j)
                result = max(result, count[0])
    
    return result 



# grid = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
grid = [
[0, 1, 0, 0, 0, 0, 1, 1, 0],
[1, 1, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 1, 0, 1, 0, 1, 1],
[0, 1, 1, 1, 0, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 1, 0],
[0, 1, 0, 0, 1, 1, 0, 1, 1],
[1, 0, 1, 1, 1, 1, 0, 0, 0]]

print(connectedCell(grid))



        

# 시도1 -> 글로벌 함수 사용, 테스트 케이스 1개 탈락 
# result = 0 

# def dfs(count, matrix, x, y):
#     global result 

#     n, m = len(matrix), len(matrix[0])
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False

#     dx = [0, 0, -1, 1, -1, -1, 1, 1]
#     dy = [1, -1, 0, 0, -1, 1, -1, 1]

#     # 현재 노드를 방문하지 않았다면
#     if matrix[x][y] == 1:
#         count += 1
#         if count > result:
#             result = count 

#         matrix[x][y] = 0
#         temp = []
#         for i in range(8):
#             temp.append(dfs(count,matrix, x+dx[i], y+dy[i]))
#         return max(temp)
#     return False

# def connectedCell(matrix):
#     n, m = len(matrix), len(matrix[0])
#     for i in range(n):
#         for j in range(m):
#             count = 0
#             dfs(count, matrix, i, j)
    
#     return result