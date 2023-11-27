import os
import sys


def read_and_print_files(directory, file_extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                            print(f"Contents of '{file_path}':\n{content}")
                    except Exception as e:
                        print(f"Error reading '{file_path}': {e}")

    except Exception as e:
        print(f"Error: {e}")

        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)
