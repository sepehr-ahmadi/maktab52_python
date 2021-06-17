import argparse


def avg(input_list):
    input_list = list(map(int, input_list))

    print(input_list)
    return sum(input_list) / len(input_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Take average of grade')
    parser.add_argument('-f', '--float', action='store', metavar='FLOAT', default=2, type=int, help='Number of grades')
    parser.add_argument('-g', '--grades', nargs='+', action='store', metavar='GRADES', required=True, help='grades')

    args = parser.parse_args()
    if not args.float==2:
        if not len(args.grades)==args.float:
            raise Exception("your float is wrong")
    print(avg(args.grades))
