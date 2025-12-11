def sum_up(arr:list,summ:int):
    if sum(arr) < summ:return -1
    seen_numbers = set()
    ans = []
    for i in arr:
        remainders = summ - i
        if remainders in seen_numbers:
            ans.append([i,remainders])
        seen_numbers.add(i)
    if ans:
        return ans
    return -1

print(sum_up([1,2,3,7,8],10))
print(sum_up([1,2,3,7,8],9))
print(sum_up([1,2,3,7,8],7))