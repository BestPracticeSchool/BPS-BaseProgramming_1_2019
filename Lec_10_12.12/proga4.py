import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="display verobosity")
args = parser.parse_args()
print(args)
if args.verbosity:
    print("VERBOOOOSE!", args.verbosity)
else:
    print("verb")