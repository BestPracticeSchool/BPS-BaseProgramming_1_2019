import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="display verobosity", action="store_true")
args = parser.parse_args()
print(args)
if args.verbosity:
    print("VERBOOOOSE!")
else:
    print("verb")