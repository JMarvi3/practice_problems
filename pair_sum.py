def pair_sum(arr, k):
    s = set()
    result = []
    for num in arr:
        if num != k - num and k - num in s:
            result.append([num, k - num])
        s.add(num)
    return result


print(pair_sum([1, 9, 6, 3, 5, 4], 10))
