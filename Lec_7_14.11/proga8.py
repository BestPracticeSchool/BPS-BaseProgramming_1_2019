def another_metrics(**kwargs):
    print(kwargs)
    print(type(kwargs))

another_metrics(name = "John", age = 10)