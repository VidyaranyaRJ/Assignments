def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

# Sample Input
string = "Hello, World!"
print("Number of vowels:", count_vowels(string))  # Output: 3
