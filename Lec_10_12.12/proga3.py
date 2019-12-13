import argparse

def factor(n : int) -> int :
    if n < 2:
        return 1
    return factor(n - 1) * n

parser = argparse.ArgumentParser()
parser.add_argument("factor", help="display factorial of factor variable (int only)", type=int)
parser.add_argument("factor2", help="display factorial of factor variable (int only)", type=int)

args = parser.parse_args()
#print(args.factor)
print(factor(args.factor))
print(factor(args.factor2))