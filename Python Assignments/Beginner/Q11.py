# Question 11: Sum of digits until a single-digit number is reached
num = 987
while num >= 10:
    num = sum(int(digit) for digit in str(num))
print(f"Final Output: {num}")
