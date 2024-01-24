# loops  (bucles)
# range(start,stop,step):


# NUBERS:
# my_list = [1,2,3,4,5,6]

# - bad form:
# print(my_list[0])
# print(my_list[1])


# - best form:
#for iteretor in my_list:
   #print(iteretor)



# sum_of_for_loop = 0

# for x in my_list:
#     sum_of_for_loop += x
# print(sum_of_for_loop)
    

# STRINGS:
# my_list = ["Monday","Tuesday","Wendnesday","Thursday"]
# for x in my_list:
#     print(f"happy {x}!" )


# WHILE:

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is larger or equal to 5")

