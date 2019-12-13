import argparse


def factor(n : int) -> int :
    if n < 2:
        return 1
    return factor(n - 1) * n

parser = argparse.ArgumentParser()
parser.add_argument("factor", help="display factorial of value", type=int)
parser.add_argument("-v", "--verbosity", help="display all info about factorial func", type=int, choices=[0,1,2])
args = parser.parse_args()

if args.verbosity == 1:
    for i in range(0, args.factor + 1):
        print("Factorial of {}! is {}".format(i, factor(i)))
elif args.verbosity == 2:
        for i in range(0, args.factor + 1):
            print("Factorial of {}! is {}\nSquare of {}^2 is {}".format(i, factor(i), i, i**2))
elif args.verbosity == 0:
    print("Factorial of {}! is {}".format(args.factor, factor(args.factor)))
else:
    print("WAT")