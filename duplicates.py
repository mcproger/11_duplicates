import os
import argparse
from itertools import combinations


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str,
                        help='Path to directory for searching duplicates')
    args = parser.parse_args()
    return args


def get_directory_walk(filepath):
    directory_entrails = os.walk(filepath)
    directory_walk = []
    for directory, folders, files in directory_entrails:
        file_path = [os.path.join(directory, file) for file in files]
        directory_walk.extend(file_path)
    return directory_walk


def get_duplicate_name_files(directory_walk):
    duplicate_name_files = {}
    subsequences_length = 2
    for file_one, file_two in combinations(directory_walk, subsequences_length):
        if os.path.basename(file_one) == os.path.basename(file_two):
            duplicate_name_files[file_one] = file_two
    return get_duplicate_name_and_size_files(duplicate_name_files)


def get_duplicate_name_and_size_files(duplicates):
    for file in duplicates:
        if os.path.getsize(file) != os.path.getsize(duplicates[file]):
            duplicates.popitem()
    return duplicates.items()


if __name__ == '__main__':
    args = get_argparser()
    directory_walk = get_directory_walk(args.filepath)
    duplicates = get_duplicate_name_files(directory_walk)
    for file_one, file_two in duplicates:
        print('Find duplicates: %s - %s' % (file_one, file_two))
    else:
        print('No duplicates in current directory')
