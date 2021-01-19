"""
Simple example of encryption/decryption using blowfish algorithm

Source:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html

Author:
Tymoteusz Mirski
"""


from Crypto.Cipher import Blowfish
from encryption_n_decryption import utils
import time


def encrypt(key_file, message_file, ciphertext_file):
    """
    Encrypt a file using Blowfish.
    
    :param key_file: path to the file containing key
    :param message_file: path to the message file which we want to encrypt
    :param ciphertext_file: path where the encrypted file shall be saved.
    :return: nothing
    """
    block_size = Blowfish.block_size
    key = utils.read_file_b(key_file)
    message = utils.read_file_s(message_file)
    data = utils.message_to_data(message, block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(data)
    utils.write_to_file_b(ciphertext_file, ciphertext)


def decrypt(key_file, ciphertext_file, output_file):
    """
    Decrypt a file using Blowfish.
    
    :param key_file: path to the file containing key
    :param ciphertext_file: path to the file which we want to decrypt
    :param output_file: path where the decrypted file shall be saved.
    :return: nothing
    """
    bs = Blowfish.block_size
    key = utils.read_file_b(key_file)
    ciphertext = utils.read_file_b(ciphertext_file)
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    utils.write_to_file_s(output_file, plaintext.decode('utf-8'))


def test_time():
    """Print execution times for encryption and decryption with Blowfish."""
    key_file = "input/blowfish_key.txt"
    message_file = "input/message.txt"
    ciphertext_file = "output/blowfish_ciphertext.txt"
    output_file = "output/blowfish_output.txt"
    encrypt_start = time.perf_counter()
    encrypt(key_file, message_file, ciphertext_file)
    encrypt_time = time.perf_counter() - encrypt_start
    decrypt_start = time.perf_counter()
    decrypt(key_file, ciphertext_file, output_file)
    decrypt_time = time.perf_counter() - decrypt_start
    print("=== Blowfish ===")
    print("Encrypt data:", encrypt_time)
    print("Decrypt data:", decrypt_time)
    print()


def main():
    """Example of encryption and decryption with Blowfish."""
    key_file = "input/blowfish_key.txt"
    message_file = "input/message.txt"
    ciphertext_file = "output/blowfish_ciphertext.txt"
    output_file = "output/blowfish_output.txt"
    encrypt(key_file, message_file, ciphertext_file)
    decrypt(key_file, ciphertext_file, output_file)


if __name__ == "__main__":
    main()





