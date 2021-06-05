filepath = "H:\python\series5\Maktab52-Hw5/input-q-2.txt"
f = open(filepath, 'r')
input_string = f.read()
def word_count(str):
    counts = dict()
    words = str.split(" ")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
f = open("output-q-2-2.txt", 'w')
for i in word_count(input_string):
    print(str(i), str(word_count(input_string)[i]), file=f)
f.close()