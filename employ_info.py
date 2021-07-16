info1 = ["neelam","programer","24","2400"]
info2 = ["komal","trainer","24","20000"]
inf03 = ["anuradha","HR","25","40000"]
info4 = ["Abhishek","manager","29","63000"]  

emp_no = ["emp1" , "emp2" , "emp3", "emp4"]
detail = ["name" , "designation" , "age" , "salary"]

# dict1 = {}
# dict2 = {}
# dict3 = {}
# dict4 = {}
# j = 0
# while j < len(detail):
#     dict1[detail[j]] = info1[j]
#     j+=1
# k = 0
# while k < len(detail):
#     dict2[detail[k]] = info1[k]
#     k+=1
# print(dict2)
# i = 0
# while i < len(detail):
#     dict3[detail[i]] = info1[i]
#     i+=1
# print(dict3)
# l = 0
# while l < len(detail):
#     dict4[detail[l]] = info1[l]
#     l+=1
# print(dict4)

# employ_info = {}
# emp = 0
# while emp <len(emp_no):

dict1 = []
a = 1
while a <= 4:
    dictionary = {}
    i = 0
    while i < len(detail):
        dictionary[detail[i]] = info1[i]
        i+=1
    dict1.append(dictionary)
    a+=1
print(dict1)

emloy_info = {}
b = 0
while b < len(emp_no):
    emloy_info[emp_no[b]] = dict1[b]
    b+=1
print(emloy_info)

import json
with open("employ_info.json" , "w") as f:
    json.dump(emloy_info,f,indent=4)