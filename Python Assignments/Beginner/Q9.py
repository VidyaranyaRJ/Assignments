# Question 9: Count frequency of elements in a list
input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency_count = {}
for num in input_list:
    frequency_count[num] = frequency_count.get(num, 0) + 1

print(frequency_count)
