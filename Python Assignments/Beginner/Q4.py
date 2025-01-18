# Question 4: Sum of odd numbers between two numbers
start, stop = 1, 10
sum_of_odds = sum(num for num in range(start, stop+1) if num % 2 != 0)
print(f"Sum of odd numbers: {sum_of_odds}")
