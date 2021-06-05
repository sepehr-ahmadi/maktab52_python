def string_calculation():
    input_string = input('please write your equation')
    print(eval(input_string))
try:
    string_calculation()
except SyntaxError:
    print('please enter the correct format \n', SyntaxError)
    string_calculation()
