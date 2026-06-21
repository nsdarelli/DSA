#Two sum with brute force
def twosum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(twosum([2, 7, 11, 15], 9))

#Two sum with hashmap
def twosum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in hashmap:
            return [hashmap[num2], i]
        hashmap[num] = i

print(twosum([2, 7, 11, 15], 9))