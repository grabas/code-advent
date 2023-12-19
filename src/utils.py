import sys


def get_input_file_contents(file_path):
    with open(f"{sys.prefix}/src/resources/{file_path}", 'r', encoding='utf-8') as file:
        return file.readlines()