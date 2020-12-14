from Crypto.Cipher import AES


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


def encrypt_with_aes(key_file, message_file, nonce_file, ciphertext_file, tag_file):
    block_size = 16
    key = read_file_b(key_file)
    message = read_file_s(message_file)
    data = message_to_data(message, block_size)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    write_to_file_b(nonce_file, nonce)
    write_to_file_b(ciphertext_file, ciphertext)
    write_to_file_b(tag_file, tag)


def decrypt_with_aes(key_file, nonce_file, ciphertext_file, tag_file, output_file):
    key = read_file_b(key_file)
    nonce = read_file_b(nonce_file)
    ciphertext = read_file_b(ciphertext_file)
    tag = read_file_b(tag_file)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
    except ValueError:
        print("Key incorrect or message corrupted")
    print(plaintext)
    write_to_file_s(output_file, plaintext.decode('utf-8'))


key_file = "key.txt"
message_file = "message.txt"
nonce_file = "nonce.txt"
ciphertext_file = "ciphertext.txt"
tag_file = "tag.txt"
output_file = "output.txt"

encrypt_with_aes(key_file, message_file, nonce_file, ciphertext_file, tag_file)
decrypt_with_aes(key_file, nonce_file, ciphertext_file, tag_file, output_file)

