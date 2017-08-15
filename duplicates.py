import os
from itertools import combinations


def get_directory_walk(filepath):
    directory_entrails = os.walk(filepath)
    directory_walk = []
    for directory, folders, files in directory_entrails:
        file_path = [os.path.join(directory, file) for file in files]
        directory_walk.extend(file_path)
    return directory_walk


def get_duplicate_name_files(directory_walk):
    duplicates = {}
    for file_one, file_two in combinations(directory_walk, 2):
        if os.path.basename(file_one) == os.path.basename(file_two):
            duplicates[file_one] = file_two
    return is_duplicate_size_files(duplicates)


def is_duplicate_size_files(duplicates):
    for file in duplicates:
        if os.path.getsize(file) != os.path.getsize(duplicates[file]):
            duplicates.popitem()
    return duplicates.items()


if __name__ == '__main__':
    filepath = input('Please enter filepath: ')
    directory_walk = get_directory_walk(filepath)
    duplicates = get_duplicate_name_files(directory_walk)
    for file_one, file_two in duplicates:
        print('Find duplicates: %s - %s' % (file_one, file_two))