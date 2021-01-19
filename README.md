# BSI Project
This project consists of two different tasks:
- Python example of Socket and BeautifulSoup libraries usage
- Python examples of encryption/decryption

-----
## Python example of Socket and BeautifulSoup libraries usage
Can be found within [this](https://github.com/PRMTRG/BSI2/tree/main/scraper_n_socket) directory.

### Main goal
Main goal of this task was to create:
- server && client through usage of Socket Library

- Simple web scraper with task of finding top 10 articles related to "pc hardware"

### server && client
- Server:
Listening on host: 127.0.0.1 within port: 65432 ( can be changed ). Its main task is to recieve encoded information from client and decode it
- Client: 
Takes input from the user then sends encoded input to the server

### Web Scrapers:
Can be found within [this](https://github.com/PRMTRG/BSI2/tree/main/scraper_n_socket) directory

- webscrape.py:
Searches for "nvidia" 10 related articles within google search and saves found sites to the pdf files.
- scraper.py:
Finds top 10 articles within [this]() website related to "cpus" then prints out all of article titles with links to the article.

----- 

## Python examples of encryption/decryption

Can be found within [this](https://github.com/PRMTRG/BSI2/tree/main/encryption_n_decryption) directory.

This simple program allows for encryption and decryption of files using the following algorithms:
- AES
- Blowfish
- DES3
- RSA
- ECC (ECIES)

It also contains an example of secure password storage using hashing and salting.

### Usage

#### Required python packages

- pycryptodome
- eciespy

Install them by running "pip install pycryptodome eciespy".

#### Symmetrical algorithms

1. Run main.py from your terminal of choice.
2. Select the algorithm to use.
3. Select the action to perform (encryption / decryption).
4. Input the paths to the necessary files as prompted.
If the entered path to any of the files is incorrect an error message will be shown and you will be prompted to reenter the paths. You can skip reentering the correctly entered paths by pressing Enter.
 
#### Asymmetrical algorithms

1. Run main.py from your terminal of choice.
2. Select the algorithm to use.
3. Select the action to perform (generate keys / encryption / decryption).
4. Input the paths to the necessary files as prompted.
If the entered path to any of the files is incorrect an error message will be shown and you will be prompted to reenter the paths. You can skip reentering the correctly entered paths by pressing Enter.

#### Test execution times of all algorithms

1. Run main.py from your terminal of choice.
2. Select the option "test execution times of algorithms".
3. The results will be printed to the terminal.

#### Password hashing and salting example

1. Run salting_example.py from your terminal of choice.
2. The "register" option allows to you to add a new user. The "log in" allows you to perform a fake log in (an adequate message will be printed to the terminal depending on whether the credentials were correct or not).
3. You may inspect the file db.json to see what the saved data looks like. It will contain fields for the username, hashed password and a unique salt of the user.

### Key files

Example key files for the symmetrical algorithms are provided. When providing your own files keep in mind these restrictions:
- the AES key must be 16, 24 or 32 bytes long
- the Blowfish key must be 4 to 56 bytes
- the DES3 key must be 24 bytes

### Execution time comparison

Tests were performed with a 9.48MB input data file. 

| Algorithm | Generate keys | Encrypt | Decrypt |
| --- | --- | --- | --- |
| AES | N/A | 0.06351929999999939 | 2.069915999999999 |
| Blowfish | N/A | 0.10284099999999796 | 2.140706999999999 |
| DES3 | N/A | 2.0419265000000024 | 4.017602100000005 |
| RSA | 0.8999211000000003 | 0.06317519999999632 | 2.0660840999999976 |
| ECC (ECIES) | 0.009185800000004463 | 0.05205550000000159 | 0.11352680000000248 |

Observations:
- time to encrypt was negligible for all algorithms except DES3 which was considerably slower
- time to decrypt was very similar for AES, Blowfish and RSA, about twice as long for DES3 and by far the fastest for ECIES
- generating keys was way faster with ECIES than with RSA

Recommendations:
- the best choice for a symmetrical algorithm appears to be AES
- the best choice for an asymmetrical algorithm appears to be ECIES
