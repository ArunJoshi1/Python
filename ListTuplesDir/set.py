# Set

s = {1, 2, 4}
s.update([6, 7, 8])  # for add elements
print(s)

# Method in Set
s.discard(8)  # for remove
print(s)

# intersection

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8, 4}
s3 = {8, 9, 10, 11, }
s4 = s1.intersection(s2, s3)
print(s4)

#  difference
s5 = s1.difference(s2, s3)
print(s5)
# union

s6 = s1.union(s2, s3)
print(s6)


