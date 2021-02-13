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
import copy
def binary_sort(temp, p):
    a, b = 0, len(temp)
    while a < b:
        c = (a+b) // 2
        a, b = (a, c) if temp[c] < p else (c+1, b)
    p[]

def climbingLeaderboard(ranked, player):
    board = sorted(list(set(ranked)), reverse=True)
    result = []
    for p in player:
        temp = copy.copy(board)
        if p in board:
            result.append(board.index(p)+1)
        else:
            temp.append(p)
            result.append(binary_sort(temp, p)+1)
    return result



ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

result = climbingLeaderboard(ranked, player)

