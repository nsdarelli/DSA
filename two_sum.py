def three_sum_brute_force(nums: List[int]) -> List[List[int]]:
    """
    Check every triplet of indices, dedupe with a set.
    
    Time:  O(n^3) - three nested loops over all triplets
    Space: O(n)   - to store unique triplets (using a set of sorted tuples)
    """
    n = len(nums)
    triplets = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    
    return [list(t) for t in triplets]

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