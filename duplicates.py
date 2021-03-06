import argparse
import os
from os.path import join, getsize, exists, isdir
from collections import defaultdict


def dir_check(dir_name):
    if not exists(dir_name):
        msg_exist = 'No such file or directory - "{}" !'.format(dir_name)
        raise argparse.ArgumentTypeError(msg_exist)
    elif not isdir(dir_name):
        msg_isdir = '"{}" is not a directory'.format(dir_name)
        raise argparse.ArgumentTypeError(msg_isdir)
    else:
        return dir_name


def get_args():
    script_usage = 'python duplicates.py  <path to dir>'
    parser = argparse.ArgumentParser(
        description='How to run duplicates.py:',
        usage=script_usage
    )
    parser.add_argument(
        'source_directory',
        type=dir_check,
        help='Specify the directory you want to check'
    )
    args = parser.parse_args()
    return args


def get_files_info(source_path):
    files_info = defaultdict(list)
    for root, directories, file_names in os.walk(source_path):
        for file_name in file_names:
            file_path = root
            file_size = getsize(join(root, file_name))
            files_info[(file_name, file_size)].append(file_path)
    return files_info


def get_duplicates_info(files_info):
    duplicates_dict = {}
    for (file_name, file_size), paths in files_info.items():
        if len(paths) > 1:
            duplicates_dict[file_name] = paths
    return duplicates_dict


def print_duplicates(duplicate_file_dict, source_dir):
    delimiter = '_' * 80
    if duplicate_file_dict:
        print('In the directory "{}" was found the following duplicate files:'
              .format(source_dir))
        print(delimiter)
        for file_name, paths in duplicate_file_dict.items():
            print('Duplicate file "{}" exists in the following '
                  'sub-directories:\n{}'
                  .format(file_name, '\n'.join(paths)))
            print(delimiter)
    else:
        print('The are no duplicate files in the "{}" '
              'directory!'.format(source_dir))

if __name__ == '__main__':
    args = get_args()
    source_path_info = get_files_info(args.source_directory)
    duplicate_file_dict = get_duplicates_info(source_path_info)
    print_duplicates(
        duplicate_file_dict,
        args.source_directory
    )
