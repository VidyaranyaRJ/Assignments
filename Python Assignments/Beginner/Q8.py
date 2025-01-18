# Question 8: LCM of two numbers
def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

number1 = 12
number2 = 18
print(f"LCM of {number1} and {number2} is: {lcm(number1, number2)}")
