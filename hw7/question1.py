import argparse
import sys

from num2words import num2words


def remainder(argument):
    def inner_function(func):
        def output(*args, **kwargs):
            res = func(args[0], args[1]) % int(argument)
            return res

        return output

    return inner_function


def string_p(func):
    def inner_function(*args, **kwargs):
        return num2words(func(args[0], args[1]))

    return inner_function


def cache():
    pass

n=int(input("please enter remainder num:\n"))
@string_p
@remainder(n)
def product(x, y):
    return int(x) * int(y)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='product function decorator')
    parser.add_argument('-x', '--x', metavar='x', action='store', required=True, help='first name in product function')
    parser.add_argument('-y', '--y', metavar='y', action='store', required=True, help='second name in product function')



    args = parser.parse_args()
    print(product(args.x, args.y))

# first_number = int(input("please enter first number:\n"))
# second_number = int(input("please enter second number:\n"))
#
# print(product(first_number, second_number))
