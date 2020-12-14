import os


def message_to_data(message, block_size):
    while len(message) % block_size != 0:
        message += ' '
    return bytes(message, 'utf-8')


def read_file_b(filename):
    with open(filename, "rb") as f:
        l = list(f.read())
    return bytes(l)


def read_file_s(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return ''.join(lines)


def write_to_file_b(filename, content):
    ensure_dir(filename)
    with open(filename, "wb") as f:
        f.write(content)


def write_to_file_s(filename, lines):
    ensure_dir(filename)
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)