import json


class UserRegistration:
    def __init__(self):
        self.fname = None
        self.lname = None
        self.phone = None
        self.national_code = None
        pass

    def set_registration(self, fname, lname, phone, national_code):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.national_code = national_code

    def reg_save_json(self, file_name):
        content = {'first_name': self.fname, 'last_name': self.lname, 'phone': self.phone,
                   'national_code': self.national_code}
        with open(file_name + '.json', 'a') as f:
            json.dump(content, f)
            f.write("\n")
            f.close()

    def reg_by_json(self,file_name):
        with open(file_name+'.json', 'r') as f:
            content = json.load(f)
            self.set_registration(content["first_name"],content["last_name"],content["phone"],content["national_code"])
            f.close()


# m = UserRegistration()
# m.set_registration('sepehr', 'ahmadi', 358394, 23048230)
# m.reg_save_json('test')
h = UserRegistration()
h.reg_by_json("test")
h.reg_save_json("test1")
# content = {
#     'users': [
#         {
#             'first_name': 'akbar',
#             'last_name': 'babaii',
#             'phone': '09379880665',
#             'is_admin': True
#         }
#     ]
# }
# with open('test.json', 'w') as f:
#     json.dump(content, f)

