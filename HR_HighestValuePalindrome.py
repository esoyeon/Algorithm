import time

start = time.time() 
def highestValuePalindrome(s, n, k):
    count = set()
    string = [l for l in s]
    # print(string)
    # 좌우 대칭 아닌 것들 우선 바꾸기 
    for i in range(n+1//2):
        if string[i] != string[n-i-1]:
            if k <= 0:
                return -1
            else:
                if int(string[i]) > int(string[n-i-1]):
                    string[n-i-1] = string[i] # 큰값으로 변경
                    count.add(n-i-1)
                elif int(string[i]) < int(string[n-i-1]):
                    string[i] = string[n-i-1]
                    count.add(i)
    
    ## count check
    if len(count) > k:
        return '-1'
    
    # 왼쪽부터 큰 숫자로 바꾸기
    for i in range(0, n//2+1):
        if string[i] != '9':
            if k - len(count) <= 0:
                break

            if k - len(count) >= 2:
                string[i], string[n-i-1] = '9', '9'
                count.update([i, n-i-1])
            
            elif i in count or n-i-1 in count:
                string[i], string[n-i-1] = '9', '9'
                count.update([i, n-i-1])

            elif n%2 != 0 and i == n-i-1 and k-len(count)>=0:
                string[i] = '9'
                count.add(i)

    answer = ''.join(string)
    return answer

# n, k = 29329, 21724
# debugging = highestValuePalindrome(s, n, k)

# with open('debugging.txt', 'w') as f:
#     f.writelines(debugging)

n, k = 6, 2
s = '932239'
print(highestValuePalindrome(s, n, k))

n, k = 6,  3 
s = '092282'
print(highestValuePalindrome(s, n, k))

n, k = 1, 1
s = '5'
print(highestValuePalindrome(s, n, k))

n, k = 5, 1
s = '12321'
print(highestValuePalindrome(s, n, k))

n, k = 4, 1
s = '0011'
print(highestValuePalindrome(s, n, k))



# n, k = 9072, 57175

# print(highestValuePalindrome(s, n, k))
# print("time :", time.time() - start) 

# # version 1 -> timeout
# def highestValuePalindrome(s, n, k):
#     count = set()
#     string = [l for l in s]
#     # print(string)
#     # 좌우 대칭 아닌 것들 우선 바꾸기 
#     for i in range(n+1//2):
#         if int(string[i]) > int(string[n-i-1]):
#             string[n-i-1] = string[i] # 큰값으로 변경
#             count.add(n-i-1)
#         elif int(string[i]) < int(string[n-i-1]):
#             string[n-i-1] = string[i]
#             count.add(i)
    
#     ## count check
#     if len(count) > k:
#         return '-1'

    
#     # 왼쪽부터 큰 숫자로 바꾸기
#     for i in range(0, n//2+1):
#         if string[i] != '9':
#             if k - len(count) < 0:
#                 break

#             if k - len(count) >= 2:
#                 string[i], string[n-i-1] = '9', '9'
#                 count.update([i, n-i-1])
            
#             elif k-len(count)>=1 and (i in count or n-i+1 in count):
#                 string[i], string[n-i-1] = '9', '9'
#                 count.update([i, n-i-1])

#             elif n%2 != 0 and i == n-i-1 and k-len(count)>=1:
#                 string[n//2] = '9'
#                 count.add(n//2)

#     answer = ''.join(string)
#     return answer