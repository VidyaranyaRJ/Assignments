def count_pairs_with_sum(arr, k):
    count = 0
    seen = set()
    for num in arr:
        if k - num in seen:
            count += 1
        seen.add(num)
    return count

# Sample Input
arr = [1, 2, 3, 4, 5]
k = 6
print("Pair count:", count_pairs_with_sum(arr, k))  # Output: 2
