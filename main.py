import aes
import blowfish
import triple_des
import sys


prompts = {
    "key_in": "Path to the (input) key file: ",
    "message_in": "Path to the (input) message file: ",
    "message_out": "Path to the (output) decrypted message file: ",
    "nonce_in": "Path to the (input) nonce file: ",
    "nonce_out": "Path to the (output) nonce file: ",
    "tag_in": "Path to the (input) tag file: ",
    "tag_out": "Path to the (output) tag file: ",
    "ciphertext_in": "Path to the (input) ciphertext file: ",
    "ciphertext_out": "Path to the (output) ciphertext file: "
    }


class InputHelper:
    def __init__(self):
        pass
    def get_input(self, keys):
        self.result = {}
        for key in keys:
            self.result[key] = input(prompts[key])
        return [ self.result[key] for key in keys ]
    def retry(self):
        keys = self.result.keys()
        for key in keys:
            while True:
                val = input(prompts[key])
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


def take_inputs_and_run(algorithm_function, inputs):
    arguments = input_helper.get_input(inputs)
    try:
        algorithm_function(*arguments)
    except Exception as e:
        print(e)
        while True:
            print("Something went wrong. Reenter the filenames and try again.")
            print("Leave input empty to use previously entered value.")
            arguments = input_helper.retry()
            try:
                algorithm_function(*arguments)
                break
            except Exception as e:
                print(e)


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

        input_helper = InputHelper()

        if algorithm == "1":
            if action == "1":
                inputs = [ "key_in", "message_in", "nonce_out", "tag_out", "ciphertext_out" ]
                take_inputs_and_run(aes.encrypt, inputs)
            elif action == "2":
                inputs = [ "key_in", "nonce_in", "tag_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(aes.decrypt, inputs)
        elif algorithm == "2":
            if action == "1":
                inputs = [ "key_in", "message_in", "ciphertext_out" ]
                take_inputs_and_run(blowfish.encrypt, inputs)
            elif action == "2":
                inputs = [ "key_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(blowfish.decrypt, inputs)
        elif algorithm == "3":
            if action == "1":
                inputs = [ "key_in", "message_in", "ciphertext_out" ]
                take_inputs_and_run(triple_des.encrypt, inputs)
            elif action == "2":
                inputs = [ "key_in", "ciphertext_in", "message_out" ]
                take_inputs_and_run(triple_des.decrypt, inputs)

