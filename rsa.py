from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import utils
import time


def generate_keys(private_key_file, public_key_file):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    utils.write_to_file_b(private_key_file, private_key)
    utils.write_to_file_b(public_key_file, public_key)
    

def encrypt(public_key_file, input_file, output_file):
    data = utils.read_file_s(input_file).encode("utf-8")
    recipient_key = RSA.import_key(open(public_key_file).read())
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    utils.ensure_dir(output_file)
    file_out = open(output_file, "wb")
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()


def decrypt(private_key_file, input_file, output_file):
    file_in = open(input_file, "rb")
    private_key = RSA.import_key(open(private_key_file).read())
    enc_session_key, nonce, tag, ciphertext = \
       [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
    file_in.close()
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
    utils.write_to_file_s(output_file, plaintext.decode('utf-8'))
    

def test_time():
    private_key_file = "rsa/private.pem"
    public_key_file = "rsa/public.pem"
    input_data_file = "input/message.txt"
    encrypted_data_file = "output/rsa_encrypted_data.txt"
    decrypted_data_file = "output/rsa_decrypted_data.txt"
    gen_keys_start = time.perf_counter()
    generate_keys(private_key_file, public_key_file)
    gen_keys_time = time.perf_counter() - gen_keys_start
    encrypt_start = time.perf_counter()
    encrypt(public_key_file, input_data_file, encrypted_data_file)
    encrypt_time = time.perf_counter() - encrypt_start
    decrypt_start = time.perf_counter()
    decrypt(private_key_file, encrypted_data_file, decrypted_data_file)
    decrypt_time = time.perf_counter() - decrypt_start
    print("=== RSA ===")
    print("Generate keys:", gen_keys_time)
    print("Encrypt data:", encrypt_time)
    print("Decrypt data:", decrypt_time)
    print()   


def main():
    private_key_file = "rsa/private.pem"
    public_key_file = "rsa/public.pem"
    input_data_file = "input/message.txt"
    encrypted_data_file = "output/rsa_encrypted_data.txt"
    decrypted_data_file = "output/rsa_decrypted_data.txt"
    generate_keys(private_key_file, public_key_file)
    encrypt(public_key_file, input_data_file, encrypted_data_file)
    decrypt(private_key_file, encrypted_data_file, decrypted_data_file)


if __name__ == "__main__":
    main()
    
