"""
Simple example of encryption/decryption using AES algorithm

Source:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

Author:
Tymoteusz Mirski
"""


from Crypto.Cipher import AES
from encryption_n_decryption import utils
import time


def encrypt(key_file, message_file, nonce_file, ciphertext_file, tag_file):
    """
    Encrypt a file using AES.
    
    :param key_file: path to the file containing key
    :param message_file: path to the message file which we want to encrypt
    :param nonce_file: path to (bytes, bytearray, memoryview) file
    :param ciphertext_file: path where the encrypted file shall be saved.
    :param tag_file: path to message authentication code file
    :return: nothing
    """
    block_size = 16
    key = utils.read_file_b(key_file)
    message = utils.read_file_s(message_file)
    data = utils.message_to_data(message, block_size)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    utils.write_to_file_b(nonce_file, nonce)
    utils.write_to_file_b(ciphertext_file, ciphertext)
    utils.write_to_file_b(tag_file, tag)


def decrypt(key_file, nonce_file, ciphertext_file, tag_file, output_file):
    """
    Decrypt a file using AES.
    
    :param key_file: path to the file containing key
    :param nonce_file: path to (bytes, bytearray, memoryview) file
    :param ciphertext_file: path to the file which we want to decrypt
    :param tag_file: path to message authentication code file
    :param output_file: path where the decrypted file shall be saved.
    :return: nothing
    """
    key = utils.read_file_b(key_file)
    nonce = utils.read_file_b(nonce_file)
    ciphertext = utils.read_file_b(ciphertext_file)
    tag = utils.read_file_b(tag_file)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
    except ValueError:
        print("Key incorrect or message corrupted")
    utils.write_to_file_s(output_file, plaintext.decode('utf-8'))


def test_time():
    """Print execution times for encryption and decryption with AES."""
    key_file = "input/aes_key.txt"
    message_file = "input/message.txt"
    nonce_file = "output/aes_nonce.txt"
    ciphertext_file = "output/aes_ciphertext.txt"
    tag_file = "output/aes_tag.txt"
    output_file = "output/aes_output.txt"
    encrypt_start = time.perf_counter()
    encrypt(key_file, message_file, nonce_file, ciphertext_file, tag_file)
    encrypt_time = time.perf_counter() - encrypt_start
    decrypt_start = time.perf_counter()
    decrypt(key_file, nonce_file, ciphertext_file, tag_file, output_file)    
    decrypt_time = time.perf_counter() - decrypt_start
    print("=== AES ===")
    print("Encrypt data:", encrypt_time)
    print("Decrypt data:", decrypt_time)
    print()


def main():
    """Example of encryption and decryption with AES."""
    key_file = "input/aes_key.txt"
    message_file = "input/message.txt"
    nonce_file = "output/aes_nonce.txt"
    ciphertext_file = "output/aes_ciphertext.txt"
    tag_file = "output/aes_tag.txt"
    output_file = "output/aes_output.txt"
    encrypt(key_file, message_file, nonce_file, ciphertext_file, tag_file)
    decrypt(key_file, nonce_file, ciphertext_file, tag_file, output_file)


if __name__ == "__main__":
    main()








