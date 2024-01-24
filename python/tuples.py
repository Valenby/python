# list ordered and the number is not repiteted
# discard = discart a number 

my_set = { 1,2,3}
print(my_set)

for x in my_set:
    print(x)

my_set.discard(3)
print(my_set)

# my_set.clear()
# print(my_set)

my_set.add(4)
print(my_set)

my_set.update([5,9])
print(my_set)