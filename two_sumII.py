#Bruteforce
def two_sum2(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i+1, j+1] #As per problem +1
    return []

print(two_sum2([1,3,4,5,7,10], 9))

#Greedy
def two_sum2(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        curSum = nums[l] + nums[r]
        if curSum == target:
            return [l+1, r+1]
        elif curSum > target:
            r -= 1
        else:
            l += 1
            
    return []

print(two_sum2([1,3,4,5,7,10], 9))