def printer(a):
    print(a)

def collector(f = printer) -> None:
    f("Hey!")

collector()