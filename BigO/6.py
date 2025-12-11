def sumTriple(arr, summ):
    for i, n1 in enumerate(arr):
        seen_nums = set()
        potential_summ = summ - n1
        for j in range(i + 1, len(arr)):
            n2 = arr[j]
            n3 = potential_summ - n2
            if n3 in seen_nums:
                yield n1, n2, n3
            else:
                seen_nums.add(n2)


print(list(sumTriple([1, -2, 3, 4, 5], 5)))
print(list(sumTriple([1,2,3,4,5],9)))
