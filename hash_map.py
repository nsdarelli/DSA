def contains_dup(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

print(contains_dup([1,2,3,4,4,5]))

def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram"))

from collections import Counter
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

print(is_anagram("anagram", "nagaram"))

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # canonical form
        print(key)
        groups[key].append(s)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))