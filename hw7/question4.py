import os
import itertools


# for dirpath, dirnames, filenames in os.walk(r"H:\python\series7"):
#   print(filenames)
def generator_directory_file_printer(dircetory: str):
    for dirpath, dirnames, filenames in os.walk(dircetory):
        yield filenames


def find_formatted_file(directory: str, file_format: str):
    filenameslist = list(generator_directory_file_printer(directory))
    filenameslist = list(itertools.chain.from_iterable(filenameslist))
    res = [i for i in filenameslist if file_format in i]
    return res


g = generator_directory_file_printer(r"/home/sepehr/maktab_52/python/series7/")
print(list(g))
m = find_formatted_file(r"/home/sepehr/maktab_52/python/series7/", "py")
print(m)
