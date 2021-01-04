from tinydb import TinyDB, Query
import random
import string
import hashlib


def generate_salt():
    salt_length = 16
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(salt_length))


def hash_password(password, salt):
    return hashlib.md5((password + salt).encode()).hexdigest()


def register(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    with TinyDB('db.json') as db:
        db.insert({'username': username, 'password': hashed_password, 'salt': salt})


def log_in(username, password):
    user = Query()
    with TinyDB('db.json') as db:
        res = db.search(user.username == username)
    if len(res) == 0:
        return False
    hashed_password = res[0]['password']
    salt = res[0]['salt']
    if hash_password(password, salt) == hashed_password:
        return True
    return False


def main():
    while True:
        print("Select action: ")
        print("1. log in")
        print("2. register")
        print("3. exit")
        choice = input()
        if choice not in ["1","2","3"]:
            print("\nInvalid option!\n")
        elif choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            if log_in(username, password):
                print("\nLogin successful\n")
            else:
                print("\nIncorrect credentials\n")
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            register(username, password)
            print("\nAccount created\n")
        elif choice == "3":
            return


if __name__ == "__main__":
    main()


