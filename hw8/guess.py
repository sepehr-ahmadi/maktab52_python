import random
import argparse

def guess(start_number, end_number, guess_number):
    random_number = random.randint(start_number, end_number)
    print(random_number)
    i = 0
    guessed = int(input('please enter number'))
    while i < guess_number:
        if guessed == random_number:
            return "Excellent you won!!!!"
        elif guessed > random_number:
            guessed = int(input("please enter lower number: \n"))
        else:
            guessed = int(input("please enter higher number: \n"))
        i += 1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='guess number game')
    parser.add_argument('-f', '--first', action='store', metavar='FLOAT', required=True, type=int, help='first number in random domain range')
    parser.add_argument('-t', '--target', action='store', metavar='GRADES', required=True,type=int, help='target number in randmom domain range')
    parser.add_argument('-g', '--game', action='store', metavar='GRADES', required=True, type=int,help='number of round')

    args = parser.parse_args()

print(guess(args.first,args.target,args.game))
