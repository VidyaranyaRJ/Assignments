def is_power_of_two(n):
    if n == 1:
        return True
    elif n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

# Sample Input
n = 8
print(is_power_of_two(n))  # Output: True
