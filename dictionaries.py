dic = {
    1: "Siddhart",
    2: "Vaibhav",
    3: "soyeb",
    }
print(dic[2])

# example 2

info = { "name": "Siddharth","age":23,"aligible":True}
# print(info)
# print(info.get("pop"))
# print(info.keys())
# print(info.values())
 
# for key in info.keys():
#     print(key) 

print(info.items())
for key,values in info.items():
    print(key,values)  # key and values are tuples


#Dictinary Methods
# 1. update()
# Example

mark1 = {101:60,102:90,103:65,104:82,106:50}
mark2 = {155:81,156:92,190:33}

mark1.update(mark2)
print(mark1)

# 2. clear()
# Example
mark1.clear()
print(mark1)

#pop()
#Example
mark1 = {101:60,102:90,103:65,104:82,106:50}
mark1.pop(102)
print(mark1)

#popitem
#Example
mark1.popitem()
print(mark1)

# del() dellet all
#Example del mark1 # it remove all dictionary but if we get valeue so it delete specific value
mark1 = {101:60,102:90,103:65,104:82,106:50}
mark2 = {155:81,156:92,190:33}
mark1.update(mark2)
print(mark1)
del mark1[155]
print(mark1)
