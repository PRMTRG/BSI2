from Crypto.Cipher import DES3
import utils

def encrypt(key_file, input_file, output_file):
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
    utils.write_to_file_b(output_file,msg)


def decrypt(key_file, input_file, output_file):
    block_size = DES3.block_size
    key = utils.read_file_b(key_file)
    ciphertext = utils.read_file_b(input_file)
    iv = ciphertext[:block_size]
    ciphertext = ciphertext[block_size:]
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    utils.write_to_file_s(output_file, plaintext.decode('utf-8'))


if __name__ == "__main__":
    key_file = "input/3des_key.txt"
    message_file = "input/message.txt"
    output_file1 = "output/3des_ciphertext.txt"
    output_file2 = "output/3des_output.txt"

    encrypt(key_file, message_file, output_file1)
    decrypt(key_file, output_file1, output_file2)