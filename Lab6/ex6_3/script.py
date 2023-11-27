import os
import sys


def calculate_total_size(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        total_size = 0

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except Exception as e:
                    print(f"Error accessing '{file_path}': {e}")

        print(f"Total size of all files in '{directory}': {total_size} bytes")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    calculate_total_size(directory_path)
