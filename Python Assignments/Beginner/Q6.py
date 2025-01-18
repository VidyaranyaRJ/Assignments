# Question 6: Check if a number is a perfect number
def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

num = int(input("Enter a number: "))
if is_perfect_number(num):
    print("Yes")
else:
    print("No")
