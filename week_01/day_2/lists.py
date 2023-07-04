
# fruits = [
#     "apple",
#     "banana",
#     "grape",
#     "orange",
# ]

# print(fruits)
# print(fruits[0])
# print(fruits[2])
# # print(fruits[10])
# # ^ will give an index error as it outside of the range of the index
# print(fruits[-1])
# print(fruits[-4])

# fruits[0] = "mango"
# print(fruits)

# # to create an emptty list either of the below will work.
# # my_list = []
# # my_list = list()
# # print(my_list)

# # to get the length of the list
# num_of_items = len(fruits)
# print(num_of_items)

# # to add items to a list
# fruits.append("kiwi")
# print(fruits)

# fruits.insert(3, "cheese")
# print(fruits)

# # to remove the last entry in a list
# fruits.pop()
# print(fruits)

# # to remove a specific string
# fruits.remove("cheese")
# print(fruits)

# # to remove a specific index entry
# fruits.remove(fruits[1])
# print(fruits)

task_list = [
    "Shower",
    "Brush Teeth",
    "Drink Coffee",
    "Eat Lunch",
    "Make Bed",
]

print(task_list)

task_list.pop()

print(task_list)

num_of_tasks = len(task_list)
print(num_of_tasks)