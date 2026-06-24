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