import aes
import blowfish
import triple_des

if __name__ == "__main__":

    while True:
        algorithm = input("Choose the algorithm to use: ")
        print("1. AES")
        print("2. Blowfish")
        print("3. Triple DES")

        action = input("Select action to perform: ")
        print("1. Encrypt")
        print("2. Dedrypt")

        if algorithm == 1:
            if action == 1:
                key = input("Path to the key file: ")
                message = input("Path to the message file: ")
                nonce = input("Path to the nonce file: ")
                tag_file = input("Path to the tag file: ")
                destination = input("Path to the destination file")
                aes.encrypt(key,message,nonce,destination,tag_file)
            if action == 2:
                key = input("Path to the key file: ")
                message = input("Path to the encrypted file: ")
                nonce = input("Path to the nonce file: ")
                tag_file = input("Path to the tag file: ")
                destination = input("Path to the destination file")
                aes.decrypt(key,message,nonce,destination,tag_file)
        elif algorithm == 2:
            if action == 1:
                key = input("Path to the key file: ")
                message = input("Path to the message file: ")
                destination = input("Path to the destination file")
                blowfish.encrypt(key, message, destination)
            if action == 2:
                key = input("Path to the key file: ")
                message = input("Path to the encrypted file: ")
                destination = input("Path to the destination file")
                blowfish.decrypt(key, message, destination)
        elif algorithm == 3:
            if action == 1:
                key = input("Path to the key file: ")
                message = input("Path to the message file: ")
                destination = input("Path to the destination file")
                triple_des.encrypt(key, message, destination)
            if action == 2:
                key = input("Path to the key file: ")
                message = input("Path to the encrypted file: ")
                destination = input("Path to the destination file")
                triple_des.decrypt(key, message, destination)
        elif algorithm > 3:
            break
