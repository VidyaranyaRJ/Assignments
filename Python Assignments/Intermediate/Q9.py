def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

# Sample Input
lst = [1, 2, 3]
index = 5
print(access_element(lst, index))  # Output: Index out of range!
