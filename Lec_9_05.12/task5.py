try:
    with open("log.txt") as f:
        data = f.read()
except FileExistsError as f_err:
    print("error happend: ", f_err)
except FileNotFoundError as ff_err:
    print("error happend: ", ff_err)