def find_largest(lst):
    if not lst:
        return None  # Return None if the list is empty
    max_num = lst[0]
    index = 1
    while index < len(lst):
        if lst[index] > max_num:
            max_num = lst[index]
        index += 1
    return max_num

# Example usage
print(find_largest([3, 7, 2, 8, 4]))  # Output: 8
print(find_largest([-5, -2, -1, -3]))  # Output: -1
