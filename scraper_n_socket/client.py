"""
Author:
Tymoteusz Mirski
"""


import socket
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


HOST = '127.0.0.1'
PORT = 65432
MAX_SIZE = 1024


def encrypt(recipient_key, data):
    """
    Encrypt data using RSA.

    Parameters
    ----------
    recipient_key : RsaKey
        RSA public key.
    data : bytes
        Data to encrypt.

    Returns
    -------
    bytes
        RSA encrypted data.

    """
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)   
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    return enc_session_key + cipher_aes.nonce + tag + ciphertext


def divide_and_send(s, data):
    """
    If needed divide data into blocks of size MAX_SIZE and send blocks to socket.
    Follow each block with b'0' if there are more blocks coming or b'1' otherwise.

    Parameters
    ----------
    s : socket
        Socket to which the data will be sent.
    data : bytes
        Data to send.

    Returns
    -------
    None.

    """
    size = len(data)
    while True:
        if size > MAX_SIZE:
            s.sendall(data[:MAX_SIZE])
            s.sendall(b'0')
            data = data[MAX_SIZE:]
            size -= MAX_SIZE
        else:
            s.sendall(data)
            s.sendall(b'1')
            break


def main():
    """ client connected to the server listening on 127.0.0.1:65432 able to send message with size=MAX_SIZE """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # receive server's public key
        data = s.recv(MAX_SIZE)
        recipient_key = RSA.import_key(data.decode("utf-8"))
        
        while True:
            message = input(">")
            if message == "quit()":
                break
            message = message.encode("utf-8")
            data = encrypt(recipient_key, message)
            divide_and_send(s, data)


if __name__ == "__main__":
    main()



