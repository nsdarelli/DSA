def sortedSquares(nums: list[int]) -> list[int]:
    l, r = 0, len(nums) - 1
    result = []

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            result.append(nums[l] ** 2)
            l += 1
        else:
            result.append(nums[r] ** 2)
            r -= 1

    return result[::-1]
            
print(sortedSquares([-4,-1,0,3,10]))