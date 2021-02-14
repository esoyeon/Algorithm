from itertools import permutations, combinations

# 타임오버 
def nonDivisibleSubset(k, s):
    # Write your code here
    left = [i%k for i in s]
    for n in range(len(s), 0, -1):
        for com in combinations(left, n):
            if sum(com) % k 
            
                    




k = 3
s = [1,7,2,4]
print(nonDivisibleSubset(k, s))

# # 타임오버 
# def nonDivisibleSubset(k, s):
#     # Write your code here
#     ans = len(s)
#     for n in range(len(s), 0, -1):
#         for com in combinations(s, n):
#             for i in combinations(com, 2):
#                 sum_ =  i[0] + i[1] 
#                 if sum_ % k != 0:
#                     count += 1
#                 else: break

#             if len(sum_) == count:
#                 return n 