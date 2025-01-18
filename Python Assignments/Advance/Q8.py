def parse_string(encoded_str):
    parts = [part for part in encoded_str.split('0') if part]

    if len(parts) == 3:
        return {
            "first_name": parts[0],
            "last_name": parts[1],
            "id": parts[2]
        }
    else:
        return "Invalid input format"

print(parse_string("Robert000Smith000123"))
