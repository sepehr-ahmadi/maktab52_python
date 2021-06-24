from pymongo import MongoClient
from random import randint
 #Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db=client.call_note

call_note={}
call_note["first_name"]=input("please enter first name: ")
call_note["last_name"]=input("please enter last name: ")
number_of_phone=int(input("please enter the number of phones: "))

for i in range(number_of_phone):
    call_note[str(f"phone {i+1}")]=input(f"please enter {i+1} phone number: ")
    #phone.append(input(f"please enter {i+1} phone number "))

print(call_note)
result=db.reviews.insert_one(call_note)
for x in db.reviews.find():
    print(x)

