import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", help="value for calculation", type=int)
parser.add_argument("-p", "--power", help="flag for powering values", action="count")

args = parser.parse_args()
if args.power:
    print("{}^{} is {}".format(args.value, args.power, args.value ** args.power))
else:
    print("{}^0 is 1".format(args.value))