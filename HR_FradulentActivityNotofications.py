
# ver 2 : 계수정렬 활용!!
#  정렬해야 할 값의 범위기 정해져 있을 때 O(N+K)로 동작

def countsort_median_double(counter, d):
    count = 0
    for i in range(201): # 지출범위가 200이하라고 했으므로
        count += counter[i]
        if count > d // 2: # 중간값 나옴 (window의 길이가 d니까! d//2보다 카운트가 오바되는 순간이 중간값)
            median = i
            break

    if d % 2 == 1: # 홀수
        return median* 2

    else: 
         # 짝수는 가운데 두 개의 평균으로 구해야 하므로 
         # 위에 찾은 중간값 바로 왼쪽에 위치하는 숫자를 찾아야 한다
         # 위에 중간값이 2개 이상일수도 있으므로, 중간값부터 왼쪽으로 탐색해서
         # count를 유의미하게 줄이는 숫자가 왼쪽! 
        for left in range(i, -1, -1): 
            count -= counter[left]
            if count < d//2:
                return left+median



def activityNotifications(expenditure, d):
    note = 0
    counter = [0] * 201 # expenditure가 200이하이므로 1-200까지 몇개 나오는지 counter 생성
    
    # expenditure 초기 d값만큼 counter 업데이트
    for exp in expenditure[:d]:
        counter[exp] += 1
    

    for i in range(d, len(expenditure)):
        start = expenditure[i-d]
        end = expenditure[i]

        median = countsort_median_double(counter, d)

        # 정보수집일 이후 각 날짜들의 지출이 중간값*2 이상인지 판단
        if median <= end:
            note += 1
        
        # counter배열 다음 배열로 이동 -> update
        counter[start] -= 1
        counter[end] += 1
    
    return note
    


n, d = 5, 3
e = [10, 20, 30, 40, 50]
print(activityNotifications(e, d))

n,d = 9, 5
e = [2, 3, 4, 2, 3, 6, 8, 4, 5]
print(activityNotifications(e, d))



# # ver1 - timeout
# from statistics import median
# def activityNotifications(expenditure, d):
#     note = 0
#     for idx, e in enumerate(expenditure):
#         if idx < d:
#             pass
#         else:
#             m = median(expenditure[idx-d:idx])
#             if e >= 2*m: 
#                 note += 1

#     return note