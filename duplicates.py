import os
import argparse
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


def get_files_info(directory_walk):
    files_info = defaultdict(list)
    for file in directory_walk:
        files_info[os.path.basename(file)].append(os.path.getsize(file))
    return files_info


def get_duplicates(files_info):
    duplicates = []
    for file_info in files_info:
        if len(files_info[file_info]) != len(set(files_info[file_info])) and len(files_info[file_info]) != 1:
            duplicates.append(file_info)
    return duplicates


if __name__ == '__main__':
    args = get_argparser()
    directory_walk = get_directory_walk(args.filepath)
    files_info = get_files_info(directory_walk)
    duplicates = get_duplicates(files_info)
    print('This files have duplicates: %s' % (', ').join(duplicates))
