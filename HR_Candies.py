
def candies(n, arr):
    c=[]
    for _ in range(n):
        c.append(1)
    for i in range(n-1):
        j=i+1
        if arr[j]>arr[i]:
            c[j]=c[i]+1
    for i in range(n-1,0,-1):
        j=i-1
        if arr[j]>arr[i]:
            if c[j]<=c[i]:
                c[j] = c[i]+1
    return sum(c)



arr = [2, 4 ,2, 6, 1, 7, 8, 9, 2, 1]
n = 10
print(candies(n, arr)) #19

arr = [1, 2, 2]
n = 3
print(candies(n, arr)) # 4

arr = [2, 4, 3, 5, 2, 6, 4, 5]
n = 8
print(candies(n, arr)) #12