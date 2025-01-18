def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    retries = 0
    while retries < 3:
        retype_password = input("Re-type password: ")
        if password == retype_password:
            print("Login successful!")
            break
        else:
            print("Passwords do not match. Try again.")
            retries += 1
    if retries == 3:
        print("Login failed! Maximum attempts reached.")

# Sample Run
login()
