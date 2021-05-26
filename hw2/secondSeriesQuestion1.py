def stringReverse(normalString):
    txt=normalString[::-1]
    return txt
inputString=input()
if inputString==stringReverse(inputString):
    print("True")
else:
    print("False")