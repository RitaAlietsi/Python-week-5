# file_handling_assignment.py

# File Creation
try:
    # Create and open a file in write mode
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2, which contains a number: 42.\n")
        file.write("Finally, this is line 3.\n")
    print("File 'my_file.txt' created and written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error while creating the file: {e}")

finally:
    # Ensure the file is closed if it was opened
    print("File creation section executed.")

# File Reading and Display
try:
    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        content = file.read()
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError as e:
    print(f"Error while reading the file: {e}")

finally:
    print("File reading section executed.")

# File Appending
try:
    # Open the file in append mode
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("Appending line 4: Python is fun!\n")
        file.write("Appending line 5: The answer is 7.\n")
        file.write("Appending line 6: Have a great day!\n")
    print("Additional lines appended to 'my_file.txt' successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error while appending to the file: {e}")

finally:
    print("File appending section executed.")
