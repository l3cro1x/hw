def excludeRepetitions(nums: list[int]) -> int:
    result = nums[0]
    for i in range(1, len(nums)):
        result = result ^ nums[i]
    return result
lst1 = [4, 1, 2, 1, 2]
lst2 = [10, 5, 3, 5, 3, 9, 9]
print(excludeRepetitions(lst1))
print(excludeRepetitions(lst2))