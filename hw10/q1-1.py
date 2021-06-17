import re
def name_validation(name):
    if re.fullmatch('[A-Za-z_]{5,14}', name):
        return True
    else:
        return False
print(name_validation('sepehr_ahmadi'))