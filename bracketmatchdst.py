def is_balanced(s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    return len(stack) == 0

# Test
print(is_balanced(input("enter a brackets")))
