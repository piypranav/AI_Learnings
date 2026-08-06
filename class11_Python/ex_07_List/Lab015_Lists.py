my_list = [1, 2, 3]
my_list_2 = [1, True, 3.14, "Hello", [1, 2, 3], (1, 2, 3), {1: "one", 2: "two"}]

print(my_list)
print(my_list_2)
print(len(my_list_2))
print(my_list)
print(my_list_2[1])
print(my_list_2[3])
print(my_list_2[4][1])
print(my_list_2[5])
print(my_list_2[5][2])
print(my_list_2[6])
print(my_list_2[6][1])
print(type(my_list_2[4]))
print(type(my_list_2[5]))
print(type(my_list_2[6]))
print("=========================================================")
# it also have inbuild function like insert, extend, append, remove, pop, clear, index, count, sort, reverse, copy  

my_list_2[4][2] = 7
print(my_list_2[4])
print(my_list_2[4][2])

my_list_2[6][2] = "seven"
print(my_list_2[6])
print(my_list_2[6][2])

my_list_2[6][3] = "eight"
print(my_list_2[6])
print(my_list_2[6][3])

# my_list_2[5][2] = 7
# print(my_list_2[5])
# print(my_list_2[5][2])

for element in my_list_2:
    print(element)
