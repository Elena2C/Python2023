import os


def rename_files_with_sequence(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")

        file_list = os.listdir(directory)

        for index, file_name in enumerate(file_list, start=1):
            old_path = os.path.join(directory, file_name)
            new_name = f"file{index}{os.path.splitext(file_name)[-1]}"
            new_path = os.path.join(directory, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")
            except Exception as e:
                print(f"Error renaming '{file_name}': {e}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")

    rename_files_with_sequence(directory_path)
