def invalid_parntsis(s: str) -> bool:
    stack = []
    hashmap_ = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char not in hashmap_:
            stack.append(char)
        elif not stack:
            return False
        else:
            popped = stack.pop()
            if popped != hashmap_[char]:
                return False
    return not stack

print(invalid_parntsis("[(){}]"))