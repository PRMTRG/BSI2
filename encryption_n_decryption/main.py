"""
Authors:
Tymoteusz Mirski,
Igor Motowidło
"""

from encryption_n_decryption import aes, blowfish, ecc, rsa, triple_des
import sys


PROMPTS = {
    "key_in": "Path to the (input) key file: ",
    "message_in": "Path to the (input) message file: ",
    "message_out": "Path to the (output) decrypted message file: ",
    "nonce_in": "Path to the (input) nonce file: ",
    "nonce_out": "Path to the (output) nonce file: ",
    "tag_in": "Path to the (input) tag file: ",
    "tag_out": "Path to the (output) tag file: ",
    "ciphertext_in": "Path to the (input) ciphertext file: ",
    "ciphertext_out": "Path to the (output) ciphertext file: ",
    "private_key_in": "Path to the (input) private key file: ",
    "private_key_out": "Path to the (output) private key file: ",
    "public_key_in": "Path to the (input) public key file: ",
    "public_key_out": "Path to the (output) public key file: ",
    }


class InputHelper:
    def __init__(self):
        pass
    def get_input(self, keys):
        self.result = {}
        for key in keys:
            self.result[key] = input(PROMPTS[key])
        return [ self.result[key] for key in keys ]
    def retry(self):
        keys = self.result.keys()
        for key in keys:
            while True:
                val = input(PROMPTS[key])
                if val == "":
                    try:
                        if self.result[key] != "":
                            break
                    except:
                        pass
                else:
                    self.result[key] = val
                    break
        return [ self.result[key] for key in keys ]


def take_inputs_and_run(input_helper, algorithm_function, inputs):
    arguments = input_helper.get_input(inputs)
    try:
        algorithm_function(*arguments)
    except Exception as e:
        print()
        print(e)
        print()
        while True:
            print("Something went wrong. Reenter the filenames and try again.")
            print("Leave input empty to use previously entered value.")
            arguments = input_helper.retry()
            try:
                algorithm_function(*arguments)
                break
            except Exception as e:
                print()
                print(e)
                print()


def select_action(actions):
    available_choices = [ f'{i}' for i in range(1, len(actions) + 2) ]
    while True:
        print("Select the action to perform")
        for i in range(len(available_choices) - 1):
            print(f'{available_choices[i]}. {actions[i]}')
        print(f'{available_choices[-1]}. go back')
        action = input()
        if action not in available_choices:
            print("\nInvalid option!\n")
        else:
            break
    return action


def main():
    while True:
        while True:
            print()
            print("Choose the algorithm or action")
            print("1. AES")
            print("2. Blowfish")
            print("3. Triple DES")
            print("4. RSA")
            print("5. ECIES")
            print("6. test execution times of algorithms")
            print("7. exit program")
            choice = input()
            if choice not in ("1", "2", "3", "4", "5", "6", "7"):
                print("\nInvalid option!\n")
            elif choice == "7":
                print("Goodbye")
                sys.exit()
            else:
                break

        input_helper = InputHelper()

        if choice == "1":
            action = select_action([ "encrypt", "decrypt" ])
            if action == "1":
                inputs = [ "key_in", "message_in", "nonce_out", "tag_out", "ciphertext_out" ]
                take_inputs_and_run(input_helper, aes.encrypt, inputs)
            elif action == "2":
                inputs = [ "key_in", "nonce_in", "tag_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(input_helper, aes.decrypt, inputs)
        elif choice == "2":
            action = select_action([ "encrypt", "decrypt" ])
            if action == "1":
                inputs = [ "key_in", "message_in", "ciphertext_out" ]
                take_inputs_and_run(input_helper, blowfish.encrypt, inputs)
            elif action == "2":
                inputs = [ "key_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(input_helper, blowfish.decrypt, inputs)
        elif choice == "3":
            action = select_action([ "encrypt", "decrypt" ])
            if action == "1":
                inputs = [ "key_in", "message_in", "ciphertext_out" ]
                take_inputs_and_run(input_helper, triple_des.encrypt, inputs)
            elif action == "2":
                inputs = [ "key_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(input_helper, triple_des.decrypt, inputs)
        elif choice == "4":
            action = select_action([ "generate_keys", "encrypt", "decrypt" ])
            if action == "1":
                inputs = [ "private_key_out", "public_key_out" ]
                take_inputs_and_run(input_helper, rsa.generate_keys, inputs)
            elif action == "2":
                inputs = [ "public_key_in", "message_in", "ciphertext_out" ]
                take_inputs_and_run(input_helper, rsa.encrypt, inputs)
            elif action == "3":
                inputs = [ "private_key_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(input_helper, rsa.decrypt, inputs)
        elif choice == "5":
            action = select_action([ "generate_keys", "encrypt", "decrypt" ])
            if action == "1":
                inputs = [ "private_key_out", "public_key_out" ]
                take_inputs_and_run(input_helper, ecc.generate_keys, inputs)
            elif action == "2":
                inputs = [ "public_key_in", "message_in", "ciphertext_out" ]
                take_inputs_and_run(input_helper, ecc.encrypt, inputs)
            elif action == "3":
                inputs = [ "private_key_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(input_helper, ecc.decrypt, inputs)
        elif choice == "6":
            aes.test_time()
            blowfish.test_time()
            triple_des.test_time()
            rsa.test_time()
            ecc.test_time()
            

if __name__ == "__main__":
    main()