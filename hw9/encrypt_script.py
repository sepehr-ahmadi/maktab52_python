from cryptography.fernet import Fernet
import argparse

# 1-A part
key = Fernet.generate_key()
f = open("key.txt", 'wb')
f.write(key)
f.close()


# 1-B part
class Encryption:
    # 1-B_I
    def Encrypt(self, input_string, encrypt_key):
        f = Fernet(encrypt_key)
        encrypted_string = f.encrypt(input_string)
        temp = open("Encrypt.txt", 'wb')
        temp.write(encrypted_string)

    # 1-B-II

    def file_Encrypt(self, input_file, encrypt_key):
        f = Fernet(encrypt_key)
        opened_file = open(input_file, 'rb')
        encrypted_string = f.encrypt(opened_file.read())
        temp = open("encrypt_file.txt", 'wb')
        temp.write(encrypted_string)
        temp.close()


# 1_B_3 part
def encrypted_decorator(func):
    def inner(*args, **kwargs):
        func_output = func(*args, **kwargs)
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_string = f.encrypt(bytes(func_output))

    return inner


# 1-c part
class decryption:
    # 1-c-I
    def decrypt(self, encrypted_input, encrypt_key):
        f = Fernet(encrypt_key)
        return f.decrypt(encrypted_input)

    # 1-c-II
    def file_decrypt(self, input_file, encrypt_key):
        f = Fernet(encrypt_key)
        opened_file = open(input_file, 'rb')
        decrypted_string = f.decrypt(opened_file.read())
        temp = open("decrypt_file.txt", 'w')
        temp.write(decrypted_string.decode("utf-8"))
        temp.close()
        return "decrypt_file.txt"


# 1_c_III
class En_Decryptin_Context_Manager():
    def __init__(self, file_name, key):
        f = Fernet(key)
        temp_string = open(file_name, 'rb')
        self.file_name = file_name
        self.file = f.decrypt(temp_string.read())
        temp_string.close()


    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        f = Fernet(key)
        encrypted_string = f.encrypt(self.file)
        temp_string = open(self.file_name, 'wb')
        temp_string.write(encrypted_string)
        temp_string.close()
        pass



# test 1_B_I and 1_B_II
m = Encryption()
m.Encrypt(b'hello', key)
m.file_Encrypt('test_file.txt', key)

# #test 1_B_III
# @encrypted_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
# a, b = 1, 2
# sum_two_numbers(a, b)

# test 1-c-I and 1-c-II
#l = decryption()
#l.file_decrypt("encrypt_file.txt", key)
# with En_Decryptin_Context_Manager("Encrypt.txt", key) as f:
#     f.write('Test')
# with En_Decryptin_Context_Manager('Encrypt.txt', key) as opened_file:
#     print(opened_file)
#     pass
if __name__ == '__main__':
    # arser = argparse.ArgumentParser(description='Test project')
    # parser.add_argument('-i', '--id', metavar='ID', action='store', required=True, help='ID field')
    # parser.add_argument('-n', '--name', action='store', default='Akbar', help='Name field')
    #
    # args = parser.parse_args()
    pass
