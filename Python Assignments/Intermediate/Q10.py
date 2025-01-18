def stone_piles(n):
    piles = []
    stones = 2 if n % 2 == 1 else 1
    while stones <= n:
        piles.append(stones)
        stones += 2
    return piles

# Sample Input
n = 7
print("Stones in a single pile:", stone_piles(n))  # Output: [2, 4, 6]
