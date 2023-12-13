import os
import re
from collections import Counter

def read_dict_file(C:\Users\User\Downloads\b1_1\b1_1\input):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            key1 = file.readline().strip()
            key2 = file.readline().strip()
            key3 = file.readline().strip()

         except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None, None, None


def process_directory(C:\Users\User\Downloads\b1_1\b1_1\input):
    dict_files = [file for file in os.listdir(C:\Users\User\Downloads\b1_1\b1_1\input) if file.endswith('.txt')]
    total_files_processed = 0
    total_file_size = 0

    for dict_file in dict_files:
      file_path = os.path.join()


""" o"""