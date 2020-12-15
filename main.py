import aes
import blowfish
import triple_des
import sys


if __name__ == "__main__":

    while True:
        while True:
            print()
            print("Choose the algorithm to use")
            print("1. AES")
            print("2. Blowfish")
            print("3. Triple DES")
            print("4. exit program")
            algorithm = input()
            if algorithm not in ("1", "2", "3", "4"):
                print("\nInvalid option!\n")
            elif algorithm == "4":
                print("Goodbye")
                sys.exit()
            else:
                break

        while True:
            print("Select the action to perform")
            print("1. encrypt")
            print("2. decrypt")
            print("3. go back")
            action = input()
            if action not in ("1", "2", "3"):
                print("\nInvalid option!\n")
            elif action == "3":
                algorithm = "0"
                print()
                break
            else:
                break
            
        if algorithm == "1":
            if action == "1":
                key_file = input("Path to the (input) key file: ")
                message_file = input("Path to the (input) message file: ")
                nonce_file = input("Path to the (output) nonce file: ")
                tag_file = input("Path to the (output) tag file: ")
                ciphertext_file = input("Path to the (output) ciphertext file: ")
                aes.encrypt(key_file, message_file, nonce_file, ciphertext_file, tag_file)
            elif action == "2":
                key_file = input("Path to the (input) key file: ")
                nonce_file = input("Path to the (input) nonce file: ")
                tag_file = input("Path to the (input) tag file: ")
                ciphertext_file = input("Path to the (input) ciphertext file: ")
                output_file = input("Path to the (output) decrypted message file: ")
                aes.decrypt(key_file, nonce_file, ciphertext_file, tag_file, output_file)
        elif algorithm == "2":
            if action == "1":
                key_file = input("Path to the (input) key file: ")
                message_file = input("Path to the (input) message file: ")
                ciphertext_file = input("Path to the (output) ciphertext file: ")
                blowfish.encrypt(key_file, message_file, ciphertext_file)
            elif action == "2":
                key_file = input("Path to the (input) key file: ")
                ciphertext_file = input("Path to the (input) ciphertext file: ")
                output_file = input("Path to the (output) decrypted message file: ")
                blowfish.decrypt(key_file, ciphertext_file, output_file)
        elif algorithm == "3":
            if action == "1":
                key_file = input("Path to the (input) key file: ")
                message_file = input("Path to the (input) message file: ")
                ciphertext_file = input("Path to the (output) ciphertext file: ")
                triple_des.encrypt(key_file, message_file, output_file)
            elif action == "2":
                key_file = input("Path to the (input) key file: ")
                ciphertext_file = input("Path to the (input) ciphertext file: ")
                output_file = input("Path to the (output) decrypted message file: ")
                triple_des.decrypt(key_file, message_file, output_file)

