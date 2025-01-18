def rotate_array(arr, d):
    return arr[-d:] + arr[:-d]

# Sample Input
arr = [1, 2, 3, 4, 5]
D = 2
print("Array after rotation:", rotate_array(arr, D))  # Output: [4, 5, 1, 2, 3]
