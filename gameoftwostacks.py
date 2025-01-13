def game_of_two_stacks(x, stack1, stack2):
    # Total sum of picked elements
    current_sum = 0
    # Count of elements picked
    count = 0

    # First, pick as many elements as possible from stack1
    i = 0
    while i < len(stack1) and current_sum + stack1[i] <= x:
        current_sum += stack1[i]
        i += 1
    count = i  # Initial count of elements from stack1

    # Now try including elements from stack2
    j = 0
    while j < len(stack2) and (i >= 0):
        current_sum += stack2[j]
        j += 1

        # If the sum exceeds x, remove elements from stack1
        while current_sum > x and i > 0:
            i -= 1
            current_sum -= stack1[i]

        # Update the maximum count
        if current_sum <= x:
            count = max(count, i + j)

    return count


# Test Example
x = 10  # Maximum sum
stack1 = [4, 2, 4, 6, 1]
stack2 = [2, 1, 8, 5]

result = game_of_two_stacks(x, stack1, stack2)
print(f"Maximum elements picked: {result}")  # Output: 4
