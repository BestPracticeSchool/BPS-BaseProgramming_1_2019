import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo" , help="this is echo flag")
args = parser.parse_args()

print(args.echo)