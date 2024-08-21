# Task 1
import os

def list_directory_contents(path):
    try:

        if not os.path.isdir(path):
            print(f"The path '{path}' is not valid. Please try another directory.")
            return
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except Exception as e:
        print(f"Error: {e} has occured.")

if __name__ == "__main__":
    directory_path = input("Enter directory path: ")
    list_directory_contents(directory_path)
