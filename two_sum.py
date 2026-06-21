#Two sum with hashmap
def twosum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in hashmap:
            return [hashmap[num2], i]
        hashmap[num] = i

print(twosum([2, 7, 11, 15], 9))