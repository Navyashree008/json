a = '{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
new_dict = {}
for x in a.item():
    if x not in new_dict:
        new_dict.append(x)
print(new_dict)