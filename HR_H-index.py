def solution(citations):
    sorted_list = sorted(citations)

    # H-index의 최대값은 논문의 개수이므로 
    n = len(citations)

    for i in range(n):
        # h의 최댓값을 찾기 위해 n-i부터 탐색 
        if sorted_list[i] >= n-i:
            return n - i 

    return 0

citations = [10, 50, 100]
print(solution(citations))


### 첫 코드 ###
# def solution(citations):
#     answer = 0
#     sorted_list = sorted(citations)
#     n = int(len(citations)*0.5)
#     for c in range(0, sorted_list[n]+1):
#         x, y = 0, 0
#         for p in citations: 
#             if p >= c:
#                 x += 1
#             if p <= c:
#                 y += 1
#         if x >= c and c >= y: 
#             answer = c

#     return answer