def solution(gems):
    unique = len(list(set(gems)))
    answer = [1, len(gems)]

    if len(gems) == unique:
        return [1, len(gems)]
    if unique == 1:
        return [1, 1]

    length = len(gems)
    for i in range(len(gems)):
        temp = []
        index = []
        count = 0
        for j in range(i, len(gems)):
            count += 1
            if len(temp) == unique:
                break
            elif count < length and gems[j] not in temp: 
                temp.append(gems[j])
                index.append(j)

        if len(temp) == unique and count < length:
            length = count
            answer[0] = index[0]+1
            answer[1] = index[-1]+1
    return answer

gems1  = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems2  = ["AA", "AB", "AC", "AA", "AC"]
gems3 = ["XYZ", "XYZ", "XYZ"]
# print(solution(gems))
print(solution(gems3))