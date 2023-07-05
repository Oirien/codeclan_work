# FUNCTIONS
# makes code reusable
# makes code organised
# DRY coding (Don't repeat yourself)
# encapsulate your code

# def greet():
#     print("Hello")

# greet()
#invokes the function greet

# def greet(name):
#     return "Hey " + name

# greeting = greet("Rob") # assigning the output to a variable
# print(greeting)


# functions with multiple parameters
# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " + name
# # calling a function with multiple parameters
# greeting = greet("Rob", "morning")
# print(greeting)



# def area_calc(width, height):
#     return width * height

# print(area_calc(13,44))

# area = area_calc(4.33,4)
# print(area)

def area_calc(width, height):
    return width * height

width_1 = 42
height_1 = 24

area = area_calc(width_1, height_1)
print(area)

width_2 = 52523
height_2 = 4432

area = area_calc(width_2, height_2)
print(str(area) + " meters squared")
# ^^^ using variables within to define parameters within a function.

chickens = [
     { "name": "Margaret","age": 2,"eggs": 0},
     { "name": "Hetty", "age": 1, "eggs": 2 },
     { "name": "Henrietta", "age": 3, "eggs": 1 },
     { "name": "Audrey", "age": 2, "eggs": 0 },
     { "name": "Mabel", "age": 5, "eggs": 1 }
]

def count_eggs(list_of_chickens):
    total_eggs = 0

    for chicken in list_of_chickens:
        total_eggs += chicken["eggs"]
        chicken["eggs"] = 0 # eggs have been collected

    return(f"{total_eggs} eggs collected")

print(count_eggs(chickens))