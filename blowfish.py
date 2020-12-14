from Crypto.Cipher import Blowfish
import utils


def encrypt(key_file, message_file, ciphertext_file):
    block_size = Blowfish.block_size
    key = utils.read_file_b(key_file)
    message = utils.read_file_s(message_file)
    data = utils.message_to_data(message, block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(data)
    utils.write_to_file_b(ciphertext_file, ciphertext)


def decrypt(key_file, ciphertext_file, output_file):
    bs = Blowfish.block_size
    key = utils.read_file_b(key_file)
    ciphertext = utils.read_file_b(ciphertext_file)
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    utils.write_to_file_s(output_file, plaintext.decode('utf-8'))


if __name__ == "__main__":
    key_file = "input/blowfish_key.txt"
    message_file = "input/message.txt"
    ciphertext_file = "output/blowfish_ciphertext.txt"
    output_file = "output/blowfish_output.txt"
    
    encrypt(key_file, message_file, ciphertext_file)
    decrypt(key_file, ciphertext_file, output_file)

