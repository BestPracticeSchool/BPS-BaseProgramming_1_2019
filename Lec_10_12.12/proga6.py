import argparse


def factor(n : int) -> int :
    if n < 2:
        return 1
    return factor(n - 1) * n

parser = argparse.ArgumentParser()
parser.add_argument("factor", help="display factorial of value", type=int)
parser.add_argument("-v", "--verbosity", help="display all info about factorial func", action="store_true")
args = parser.parse_args()

if args.verbosity:
    for i in range(0, args.factor + 1):
        print("Factorial of {}! is {}".format(i, factor(i)))
else:
    print("Factorial of {}! is {}".format(args.factor, factor(args.factor)))
