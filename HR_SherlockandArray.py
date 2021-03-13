# 첫시도 -> 당연하게도 타임리밋에 걸림 

def balancedSums(arr):
    n = len(arr)
    s = sum(arr)  # 오른쪽 sum = 전체 sum - left sum - 해당 x 
    l = 0

    for idx, i in enumerate(arr):
        if l == s - i - l: 
            return "YES"

        l += i  

    return "NO"


arr = [1, 2, 3]
print(balancedSums(arr))

arr = [1, 2, 3, 3]
print(balancedSums(arr))

# # 첫시도 -> 당연하게도 타임리밋에 걸림 
# def balancedSums(arr):
#     n = len(arr)
#     for idx, i in enumerate(arr):
#         if sum(arr[:idx]) == sum(arr[idx+1:]):
#             return "YES"
    
#     return "NO"