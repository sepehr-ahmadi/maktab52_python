from nltk import tokenize

filepath = "H:\python\series5\Maktab52-Hw5/input-q-2.txt"
f = open(filepath, 'r')
input_string = f.read()
output_list = tokenize.sent_tokenize(input_string)
print(len(output_list))
f = open("output-q-2-1.txt", 'w')
for i in output_list:
    print(i + "\n", file=f)
f.close()
