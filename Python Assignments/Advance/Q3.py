def JtoI():
    try:
        with open('C:/Users/vrjav/OneDrive/Desktop/ConsultAdd/Python Assignments/Advance/words.txt', 'r') as file:
            content = file.read() 
        corrected_content = content.replace('J', 'I')

        print(corrected_content)
    except FileNotFoundError:
        print("The file 'words.txt' does not exist.")

JtoI()
