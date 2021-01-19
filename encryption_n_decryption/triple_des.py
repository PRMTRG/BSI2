"""
Simple example of encryption/decryption using triple des algorithm

Source:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html

Authors:
Igor Motowidło,
Tymoteusz Mirski
"""


from Crypto.Cipher import DES3
from encryption_n_decryption import utils
import time


def encrypt(key_file, input_file, output_file):
    """
    Encrypt a file using DES3.
    
    :param key_file: path to the file containing key
    :param input_file: path to the message file which we want to encrypt
    :param output_file: path where the encrypted file shall be saved.
    :return: nothing
    """
    k = utils.read_file_b(key_file)
    message = utils.read_file_s(input_file)
    data = utils.message_to_data(message, DES3.block_size)
    while True:
        try:
            key = DES3.adjust_key_parity(k)
            break
        except ValueError:
            pass
    cipher = DES3.new(key, DES3.MODE_CFB)
    msg = cipher.iv + cipher.encrypt(data)
    utils.write_to_file_b(output_file, msg)


def decrypt(key_file, input_file, output_file):
    """
    Decrypt a file using DES3.
    
    :param key_file: path to the file containing key
    :param input_file: path to the file which we want to decrypt
    :param output_file: path where the decrypted file shall be saved.
    :return: nothing
    """
    block_size = DES3.block_size
    key = utils.read_file_b(key_file)
    ciphertext = utils.read_file_b(input_file)
    iv = ciphertext[:block_size]
    ciphertext = ciphertext[block_size:]
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    utils.write_to_file_s(output_file, plaintext.decode('utf-8'))


def test_time():
    """Print execution times for encryption and decryption with DES3."""
    key_file = "input/3des_key.txt"
    message_file = "input/message.txt"
    output_file1 = "output/3des_ciphertext.txt"
    output_file2 = "output/3des_output.txt"
    encrypt_start = time.perf_counter()
    encrypt(key_file, message_file, output_file1)
    encrypt_time = time.perf_counter() - encrypt_start
    decrypt_start = time.perf_counter()
    decrypt(key_file, output_file1, output_file2)    
    decrypt_time = time.perf_counter() - decrypt_start
    print("=== DES3 ===")
    print("Encrypt data:", encrypt_time)
    print("Decrypt data:", decrypt_time)
    print()


def main():
    """Example of encryption and decryption with DES3."""
    key_file = "input/3des_key.txt"
    message_file = "input/message.txt"
    output_file1 = "output/3des_ciphertext.txt"
    output_file2 = "output/3des_output.txt"
    encrypt(key_file, message_file, output_file1)
    decrypt(key_file, output_file1, output_file2)  


if __name__ == "__main__":
    main()
    
    
    
    