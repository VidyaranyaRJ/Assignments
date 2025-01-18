def count_lines_in_file():
    with open('C:/Users/vrjav/OneDrive/Desktop/ConsultAdd/Python Assignments/Advance/doc.txt', 'r') as file:
        lines = file.readlines()
    return len(lines)

print(count_lines_in_file())
