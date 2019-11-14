def super_mega(*args:int, **kwargs:str) -> bool:
    print(args)
    print(kwargs)

super_mega(1,2,3,4,5,6,7,10, kek = 20, lol = 30, mu = "age")
super_mega()
super_mega(kek=20)