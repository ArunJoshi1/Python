numbers = [1,1,2,3,4,4,2,4]
unique = []
for item in numbers:
    if  item not in unique:
        unique.append(item)
print(unique)
