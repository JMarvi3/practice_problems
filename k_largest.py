def k_largest(arr, k):
    arr.sort(reverse=True)
    return arr[:k]

print(k_largest([5, 16, 7, 9, -1, 4, 3, 11, 2], 3))
