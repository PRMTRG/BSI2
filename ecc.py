import ecies
import utils
import time


def generate_keys(private_key_file, public_key_file):
    eth_k = ecies.utils.generate_eth_key()
    private_key = eth_k.to_hex()
    public_key = eth_k.public_key.to_hex()
    utils.write_to_file_s(private_key_file, private_key)
    utils.write_to_file_s(public_key_file, public_key)


def encrypt(public_key_file, input_data_file, encrypted_data_file):
    public_key = open(public_key_file).read()
    data = utils.read_file_s(input_data_file).encode("utf-8")
    encrypted_data = ecies.encrypt(public_key, data)
    utils.write_to_file_b(encrypted_data_file, encrypted_data)


def decrypt(private_key_file, encrypted_data_file, output_file):
    private_key = open(private_key_file).read()
    encrypted_data = utils.read_file_b(encrypted_data_file)
    plaintext = ecies.decrypt(private_key, encrypted_data)
    utils.write_to_file_b(output_file, plaintext)


def test_time():
    private_key_file = "ecc/private.txt"
    public_key_file = "ecc/public.txt"
    input_data_file = "input/message.txt"
    encrypted_data_file = "output/ecc_encrypted_data.txt"
    decrypted_data_file = "output/ecc_decrypted_data.txt"
    gen_keys_start = time.perf_counter()
    generate_keys(private_key_file, public_key_file)
    gen_keys_time = time.perf_counter() - gen_keys_start
    encrypt_start = time.perf_counter()
    encrypt(public_key_file, input_data_file, encrypted_data_file)
    encrypt_time = time.perf_counter() - encrypt_start
    decrypt_start = time.perf_counter()
    decrypt(private_key_file, encrypted_data_file, decrypted_data_file)
    decrypt_time = time.perf_counter() - decrypt_start
    print("=== ECC (ECIES) ===")
    print("Generate keys:", gen_keys_time)
    print("Encrypt data:", encrypt_time)
    print("Decrypt data:", decrypt_time)
    print()


def main():
    private_key_file = "ecc/private.txt"
    public_key_file = "ecc/public.txt"
    input_data_file = "input/message.txt"
    encrypted_data_file = "output/ecc_encrypted_data.txt"
    decrypted_data_file = "output/ecc_decrypted_data.txt"
    generate_keys(private_key_file, public_key_file)
    encrypt(public_key_file, input_data_file, encrypted_data_file)
    decrypt(private_key_file, encrypted_data_file, decrypted_data_file)    


if __name__ == "__main__":
    main()
    
    