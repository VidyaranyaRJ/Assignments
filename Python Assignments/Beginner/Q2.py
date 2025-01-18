# Question 2: Count digits and letters in a string
user_input = input("Enter a string: ")
letters = sum(c.isalpha() for c in user_input)
digits = sum(c.isdigit() for c in user_input)

print(f"Alphabets: {letters} & Number: {digits}")
