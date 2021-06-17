import re

email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def email_validation(email):
    if (re.search(email_regex, email)):
        return True

    else:
        return False
print(email_validation("sepehr.ahamdi@gamil.com"))