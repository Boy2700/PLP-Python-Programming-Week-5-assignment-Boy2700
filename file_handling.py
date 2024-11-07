# File Handling Assignment

# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Write at least three lines of text to the file, including strings and numbers
        file.write("This is the first line of text.\n")
        file.write("The second line contains number: 42\n")
        file.write("Here is the third line, with a float value: 3.14\n")
    
    print("File 'my_file.txt' created and initial content written.")

except PermissionError:
    print("Error: You don't have permission to write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    # Read the contents of "my_file.txt" and display them on the console
    with open("my_file.txt", 'r') as file:
        contents = file.read()
        print("\nContents of 'my_file.txt':")
        print(contents)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading process completed.")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a') and append three additional lines
    with open("my_file.txt", 'a') as file:
        file.write("This is the fourth line added through append mode.\n")
        file.write("The fifth line contains another number: 100\n")
        file.write("Finally, the sixth line with some text: Goodbye!\n")
    
    print("\nNew content appended to 'my_file.txt'.")

except PermissionError:
    print("Error: You don't have permission to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.")
