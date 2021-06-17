import re


def phone_validation(number):
    if re.search("(09)|([+]989)\d{9,9}$", number):
        return True
    else:
        return False


print(phone_validation('09123583858'))
