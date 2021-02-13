#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player

from collections import defaultdict

# p보다 크면서 가장 가까운 값 찾기 / 이진탐색 응용 
def search_bigger(ranked, p):
    start, end = 0, len(ranked)
    while start <= end:
        mid = (start + end) // 2
        # 보드 값들보다 작으면 보드 중 마지막값
        if ranked[-1] >= p:
            return ranked[-1]

        # 리턴 조건 
        if (ranked[mid] >= p and p >= ranked[mid+1]):
            return ranked[mid]

        # 출발값 조정
        elif ranked[mid] > p:
            start = mid+1
        # 마지막 값 조정
        else: 
            end = mid -1        
    
def climbingLeaderboard(ranked, player):
    board = defaultdict(lambda: len(board)+1)
    result = []
    # board 생성
    for r in ranked:
        if r not in board:
            board[r]
    print(board)

    # player 검사 
    for p in player:
        # 최댓값보다 크면 1순위
        if p >= ranked[0]:
            result.append(1)

        # 보드에 있는 값이면 기존 순위
        elif p in board:
            result.append(board[p])

        # 보드값들 중 가장 가까우면서 p보다 큰 값 찾아서 + 1
        else:
            key = search_bigger(ranked, p)
            new_rank = board[key] + 1
            result.append(new_rank)
    
    return result

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

result = climbingLeaderboard(ranked, player)

### 타임리밋에 걸림...
# import copy
# from bisect import bisect_left, bisect_right

# def climbingLeaderboard(ranked, player):
#     board = sorted(list(set(ranked)))
#     result = []
#     for p in player:
#         temp = copy.copy(board)
#         if p in board:
#             result.append(len(board)-board.index(p))
#         else:
#             index = len(temp)-bisect_right(temp,p) + 1
#             result.append(index)
#     return result