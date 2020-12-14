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
    with open(filename, "wb") as f:
        f.write(content)


def write_to_file_s(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)

