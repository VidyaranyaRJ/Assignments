# Question 12: Reverse a number using a while loop
num = 12345
rev_num = 0
while num > 0:
    rev_num = rev_num * 10 + num % 10
    num //= 10
print(f"Reversed number: {rev_num}")
