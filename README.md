



# Anti-Dublicator

The code accept a path to  file-system's directory and find dublicate files.


# Quickstart

The program is represented by the module ```dublicates.py```.
Module ```dublicates.py``` contains the following functions:

- ```get_args()``` - parses script command-line arguments
- ```get_files_info()``` - accepts the path to file-system directory and returns info about representing files and files-size
- ```get_dublicates()``` - accepts dictionary and returns dict having paths-count > 1
- ```print_result()``` - prints info about finding files



The program uses these libs from Python Standart Library:

```python
argparse
os
join, getsize, exists, basename from os.path
defaultdict from collections 
```

How in works:
- The program reads  the first command-line argument(path to directory)
- parsing directory's content using  ```get_path_content()``` -function
- checking for dublicate files using ``` get_dublicates()``` - function
- prints info about dublicate_files using ```print_result()```-function

Example of script launch on Linux, Python 3.5:

```bash

$ python dublicates.py  <path to dir>

```
in the console  output you will see something  like this:
```bash
In the directory 'C:\Devman\' was found dublicate files:
________________________________________________________________________________
Dublicate file "bars_new.py" exists in the following folders:
C:\Devman
C:\Devman\3_bars
C:\Devman\5_lang_frequency
```
If haven't dublicate files in the directory, you will see such message:
```The are no dublicate files in the 'C:\Devman\' directory!```

In the cases below, the program will not run:

The program check command-line arguments and if it is wrong,  you will see the warning message ```error: unrecognized arguments``` and usage-message.

If the the directory doesnt't present in the file-system, you will see the warning message:
```No such directory <directory> !```
If the input-value is not a directory,  you will see the warning message:
```The <dir_name> is not a directory!```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)




