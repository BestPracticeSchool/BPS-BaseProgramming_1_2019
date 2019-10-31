d = {"name":"Joe", "age":23, "city":"Moscow", "uni":"MGTU"}
print(d)
for k in d.keys():
    print(k, d[k])

print(d.values())

for _,v in d.items():
    print(v )