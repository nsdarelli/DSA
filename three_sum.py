#Three sum solution by brute force:
def threeSum(nums: list[int]) -> list[list[int]]:
    l = len(nums)
    answer = set()

    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans = tuple(sorted([nums[i], nums[j], nums[k]]))
                    answer.add(ans)
    return [list(t) for t in answer]   

print(threeSum([-1, 0, 1, 2, -1, -4]))

#Three sum solution by greedy approach:
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    answer = []

    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, n-1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                answer.append([nums[i], nums[l], nums[r]])
                l, r = l+1, r-1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return answer

print(threeSum([-1, 0, 1, 2, -1, -4]))