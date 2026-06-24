def longest_substring(s: str) -> int:
    char_index = {}
    max_len = 0
    l = 0

    for r, char in enumerate(s):
        if char in char_index and char_index[char]>=l:
            l = char_index[char] + 1
        
        char_index[char] = r
        max_len = max(max_len, r-l+1)

    return max_len

print(longest_substring("abcabcbb"))

def longest_substring_(s: str) ->int:
    max_len = 0
    for i in range(len(s)):
        set_t = set()
        for j in range(i, len(s)):
            if s[j] in set_t:
                break
            set_t.add(s[j])
            max_len = max(max_len, j-i+1)

    return max_len

print(longest_substring_("abcdabdcbb"))

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
    n = len(nums)
    max_sum = 0
    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum+=nums[j]
            if cur_sum>max_sum:
                max_sum = cur_sum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def maxSubArray(nums):
    n=len(nums)
    max_sum = float('-inf')
    cur_sum = 0

    for i in range(n):
        cur_sum += nums[i]
        if cur_sum>max_sum:
            max_sum = cur_sum
        if cur_sum<0:
            cur_sum = 0
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))