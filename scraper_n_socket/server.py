"""
Author:
Tymoteusz Mirski
"""


import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


HOST = '127.0.0.1'
PORT = 65432
MAX_SIZE = 1024


def decrypt(private_key, data):
    """
    Decrypt data encrypted with RSA.

    Parameters
    ----------
    private_key : RsaKey
        RSA private key.
    data : bytes
        RSA encrypted data.

    Returns
    -------
    string
        Decrypted data.

    """
    key_size = private_key.size_in_bytes()
    enc_session_key, nonce, tag, ciphertext = \
        data[:key_size], \
        data[key_size:key_size+16], \
        data[key_size+16:key_size+32], \
        data[key_size+32:]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode("utf-8")


def main():
    """ server listening on 127.0.0.1:65432  waiting for encrypted message to decrypt """
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connection from', addr)
            print()
            conn.sendall(public_key.export_key())
            message = b''
            while True:
                data = conn.recv(MAX_SIZE)
                if not data:
                    break
                message += data
                over = conn.recv(1)
                if not over:
                    break
                if over == b'1':
                    print("Data received:")
                    print(message)
                    print()
                    decrypted_message = decrypt(private_key, message)
                    message = b''
                    print("Decrypted message:")
                    print(decrypted_message)
                    print()
                    
            
if __name__ == "__main__":
    main()