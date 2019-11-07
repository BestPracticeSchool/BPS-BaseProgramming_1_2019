message = input() # Hello World

d = {}
for letter in message.lower():
    if letter in d.keys():
        d[letter] += 10
    else:
        d[letter] = 10

for k,v in d.items():
    print(k, ":", v)

messages =["Hello Bob", "My name is BOb", "I'm 17 y.o."]
d = {}
for message in messages:
    for letter in message.lower():
        if letter in d.keys():
            d[letter] += 10
        else:
            d[letter] = 10

for k,v in d.items():
    print(k, ":", v)