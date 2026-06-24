def findMaxSubArray(nums: list[int], k: int) -> int:
    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(window_sum, max_sum)

    return max_sum

print(findMaxSubArray([1,2,3,4,5,6], 4))


#Maximum Average SubArray:
def findMaxAvg(nums: list[int], k: int) -> float:
    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)

    max_avg = max_sum / k

    return max_avg

print(findMaxAvg([1, 12, -5, -6, 50, 3], 4))


