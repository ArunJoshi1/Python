names=['marsh','joshi','rahul','som','rachna']
print(names[::-1])
names.clear()
print(names)

# method of list or array

numbers=[i for i in range(1,10)]
print(numbers)
print(numbers.index(5))
numbers.append(20)
numbers.insert(0,30)
print(numbers)
numbers.remove(20)
print(numbers)
print(numbers.pop(),numbers)
print(numbers.pop(),numbers)
print(numbers.pop(),numbers)
numbers.append(1)
print(30 in numbers)
print(numbers.count(1))

# sort
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

