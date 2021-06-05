import os

def size_calculator(str):
    file_list=os.listdir(str)
    total_file_size=0
    for i in file_list:
        x=i.split(".")
        if os.path.isfile(str+"/"+i) and len(x[-1])>2:
            total_file_size=os.path.getsize(str+"/"+i)+total_file_size
    return total_file_size
print(size_calculator("H:\python\series5"))