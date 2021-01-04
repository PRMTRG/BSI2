"""
Authors:
Tymoteusz Mirski,
Igor Motowidło
"""


import os


def message_to_data(message, block_size):
    """Converts a utf-8 string into a bytes object while changing the length to a multiple of the data block size"""
    while len(message) % block_size != 0:
        message += ' '
    return bytes(message, 'utf-8')


def read_file_b(filename):
    """Reads the file and returns bytes"""
    with open(filename, "rb") as f:
        l = list(f.read())
    return bytes(l)


def read_file_s(filename):
    """Reads the file and returns single string"""
    with open(filename, "r") as f:
        lines = f.readlines()
    return ''.join(lines)


def write_to_file_b(filename, content):
    """Overrides existing file / Creates new file using bytes"""
    ensure_dir(filename)
    with open(filename, "wb") as f:
        f.write(content)


def write_to_file_s(filename, lines):
    """Overrides existing file/ Creates new file by lines of strings"""
    ensure_dir(filename)
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)


def ensure_dir(file_path):
    """Ensures that output directory does exist"""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)