import os
import sys


def count_files_by_extension(directory):
    try:
        # Check if the specified directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Verify that the specified path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        file_counts = {}

        for root, _, files in os.walk(directory):
            for file in files:
                _, file_extension = os.path.splitext(file)
                if file_extension:
                    file_extension = file_extension.lower()  # Normalize to lowercase
                    if file_extension not in file_counts:
                        file_counts[file_extension] = 1
                    else:
                        file_counts[file_extension] += 1

        if not file_counts:
            print(f"No files found in '{directory}'.")
        else:
            print("File counts by extension:")
            for extension, count in file_counts.items():
                print(f"{extension}: {count} file(s)")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
