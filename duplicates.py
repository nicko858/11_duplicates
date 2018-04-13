import argparse
import os
from os.path import join, getsize, exists, basename


def get_args():
    script_usage = 'python dublicates.py  <path to dir>'
    parser = argparse.ArgumentParser(
        description='How to run dublicates.py:',
        usage=script_usage
    )
    parser.add_argument(
        'source_directory',
        help='Specify the directory you want to check'
    )
    args = parser.parse_args()
    return args


def get_reverse_path_content(source_path_content):
    reverse_path_content = {}
    for source_path, source_file_info in source_path_content.items():
        if source_file_info not in reverse_path_content.keys():
            reverse_path_content[source_file_info] = [source_path]
        else:
            reverse_path_content[source_file_info].append(source_path)
    return reverse_path_content


def get_path_content(source_path):
    source_path_content = {}
    for root, directories, files in os.walk(source_path):
        for file in files:
            file_path = join(root, file)
            file_size = getsize(join(root, file))
            file_name = basename(file_path)
            source_path_content[file_path] = str(file_name) + '_size_' + str(file_size)
    return source_path_content


def get_dublicates_list(content):
    dublicates_list = []
    for key, value in content.items():
        if len(value) > 1:
            dublicates_list.append(value)
    return dublicates_list


def print_result(source_path_content, source_dir):
    dublicate_file_list = get_dublicates_list(get_reverse_path_content(source_path_content))
    if dublicate_file_list:
        print('In the directory \'{}\' was found dublicate files:\n'.format(source_dir))
        print('_________________________________________________________________________')
        for file_path in dublicate_file_list:
            print('\n'.join(file_path))
            print('_________________________________________________________________________')
    else:
        print('The are no dublicate files in the \'{}\' '
              'directory!'.format(source_dir))


if __name__ == '__main__':
    args = get_args()
    try:
        if exists(args.source_directory):
            source_path_content = get_path_content(args.source_directory)
            print_result(source_path_content, args.source_directory)
        else:
            raise IOError
    except IOError:
        exit('No such directory - \'{}\' !'.format(args.source_directory))
