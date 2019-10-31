message = "Hello world!"
ticker = {}
for let in message:

   # ticker[let] = ticker.get(1,??) + 1

    if let in ticker.keys():
        ticker[let] += 1
    else:
        ticker[let] = 1
keys = list(ticker.keys())
keys.sort()
for k in keys:
    print(k, ":", ticker[k])

print(dir(ticker))