def find_median(number_list):
    number_list.sort()
    n = len(number_list)
    if n % 2 == 1:
        return number_list[n // 2]
    else:
        return (number_list[n // 2 - 1] + number_list[n // 2]) / 2

# Sample Input
number_list = [7, 2, 5, 1, 9, 3]
print("Median:", find_median(number_list))  # Output: 4.0
