filepath = "H:\python\series5\Maktab52-Hw5/input-q-1.txt"
f = open(filepath, 'r')
input_string = f.read()
# print(x)
my_dict = {
    'one': 1,
    'two': 2,
    'three' : 3,
    'four': 4,
    'five' : 5,
    'six' : 6,
    'seven': 7,
    'eight' : 8,
    'nine' : 9,
    'ten' : 10,
    'eleven' : 11,
    'twelve' : 12,
    'thirteen' : 13,
    'fourteen' : 14,
    'fifteen' : 15,
    'sixteen' : 16,
    'seventeen' : 17,
    'eighteen' : 18,
    'nineteen' : 19,
    'twenty' : 20
}
f = open("output-q-1.txt", 'w')
for num in my_dict:
    input_string = input_string.replace(str(num), str(my_dict[num]))
    print(input_string, file=f)
f.close()



