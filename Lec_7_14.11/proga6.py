print(1, 2, 3,4 , "asd", "asdqwe", sep=", ", end="\n")

def printer(*args):
    print(args)
    print(type(args))
    for i in args:
        print(i)
    return args

printer(1,2,3,4,5,6,"q", "w", "asdqw")


