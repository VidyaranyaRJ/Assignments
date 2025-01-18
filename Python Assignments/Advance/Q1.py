def read_even_length_strings():
    with open('C:/Users/vrjav/OneDrive/Desktop/ConsultAdd/Python Assignments/Advance/doc.txt', 'r') as file:
        content = file.readlines()

    processed_lines = []
    for line in content:
        even_words = [word for word in line.split() if len(word) % 2 == 0]
        processed_lines.append(" ".join(even_words))  # Rejoin words to form a line

    return processed_lines


result = read_even_length_strings()
for line in result:
    print(line)
