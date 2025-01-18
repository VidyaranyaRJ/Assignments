def run_length_encoding(input_str):
    result = []
    count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            result.append(f"{input_str[i - 1]}{count}")
            count = 1
    result.append(f"{input_str[-1]}{count}")
    return ''.join(result)

print(run_length_encoding("wwwwaaadebbbbbw"))
