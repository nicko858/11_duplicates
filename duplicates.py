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


def get_dublicate_files(source_path_content):
    checked_files = {}
    for source_path, source_file_info in source_path_content.items():
        if not source_file_info in checked_files.values():
            checked_files[source_path] = source_file_info
        else:
            dublicate_files = []
            for dubl_path, dubl_file_info in source_path_content.items():
                if dubl_file_info == source_file_info:
                    dublicate_files.append(dubl_path)
            return dublicate_files, len(dublicate_files)


def get_path_content(source_path):
    source_path_content = {}
    for root, directories, files in os.walk(source_path):
        for file in files:
            file_path = join(root, file)
            file_size = getsize(join(root, file))
            file_name = basename(file_path)
            source_path_content[file_path] = [file_name, file_size]
    return source_path_content


def print_result(source_path_content, source_dir):
    if get_dublicate_files(source_path_content):
        dublicate_files_list, dublicate_files_count = get_dublicate_files(source_path_content)
        print('In the directory \'{}\' was found {} dublicate files:\n'.format(source_dir, dublicate_files_count))
        for files in dublicate_files_list:
            print(files)
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
        exit('No such directory - {} !'.format(args.source_directory))
