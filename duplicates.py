import os
import argparse
from itertools import combinations_with_replacement
from collections import defaultdict


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


def is_duplicate_name_files(file_one, file_two):
    return os.path.basename(file_one) == os.path.basename(file_two)


def is_duplicate_size_files(file_one, file_two):
    return os.path.getsize(file_one) == os.path.getsize(file_two)


def get_duplicates(directory_walk):
    duplicates = defaultdict(set)
    subsequences_length = 2
    for file_one, file_two in combinations_with_replacement(directory_walk, subsequences_length):
        if is_duplicate_name_files(file_one, file_two) and is_duplicate_size_files(file_one, file_two):
            duplicates[os.path.basename(file_one)].add(file_two)
    return duplicates


if __name__ == '__main__':
    args = get_argparser()
    directory_walk = get_directory_walk(args.filepath)
    duplicates = get_duplicates(directory_walk)
    for file, duplicates in duplicates.items():
        print('Find duplicates: File - %s, Duplicates - %s' %
              (file, ', '.join(duplicates)))
