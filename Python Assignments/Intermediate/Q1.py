def common_elements(l1, l2):
    return list(set(l1) & set(l2))

# Sample Input
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
print(common_elements(l1, l2))  # Output: [4, 5]
