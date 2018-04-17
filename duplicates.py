import argparse
import os
import re
from os.path import join, getsize, exists, isdir
from collections import defaultdict


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


def get_files_info(source_path):
    source_path_content = defaultdict(list)
    for root, directories, file_names in os.walk(source_path):
        for file in file_names:
            file_path = join(root)
            file_size = getsize(join(root, file))
            file_info = '{} {} {} '.format(str(file), '_size_', str(file_size))
            source_path_content[file_info].append(file_path)
    return source_path_content


def get_dublicates(content):
    dublicates_dict = {}
    for file_info, paths in content.items():
        file_name = re.sub(' _.*', '', (str(file_info)))
        if len(paths) > 1:
            dublicates_dict[file_name] = [paths]
    return dublicates_dict


def print_result(source_path_content, source_dir):
    dublicate_file_dict = get_dublicates(source_path_content)
    delimiter = '_' * 80
    if dublicate_file_dict:
        print('In the directory "{}" was found dublicate files:'.format(source_dir))
        print(delimiter)
        for file_name, paths in dublicate_file_dict.items():
            for path in paths:
                print('Dublicate file "{}" exists in the following folders:\n{}'
                      .format(file_name, '\n'.join(path)))
                print (delimiter)
    else:
        print('The are no dublicate files in the "{}" '
              'directory!'.format(source_dir))


if __name__ == '__main__':
    args = get_args()
    try:
        if exists(args.source_directory):
            if isdir(args.source_directory):
                source_path_content = get_files_info(args.source_directory)
                print_result(source_path_content, args.source_directory)
            else:
                raise OSError
        else:
            raise FileNotFoundError
    except OSError:
        exit('The "{}" is not a directory!'.format(args.source_directory))
    except FileNotFoundError:
       exit('No such file or directory - "{}" !'.format(args.source_directory))
