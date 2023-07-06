"""
Write each function and test it works by printing a call to the function with any required inputs (argument values) and checking the output (return value) in your terminal by running:

python3 functions_lab.py

Each docstring (""" """) includes instructions for the function name, any parameters it takes, and what it returns

If there is a `pass` in the body of the function, replace it with your own code

Some functions and checks have been started for you!
"""

# === COMPLETED EXAMPLE ==============

"""
return_10 function
takes no parameters
returns the number 10
"""
def return_10():
    return 10

print("------------------------------")
print("By calling return_10, I'm expecting 10, and the result is")
print(return_10())


# === START HERE =====================

"""
add function 
takes the parameters num_1 and num_2
returns the result of adding num_1 and num_2
"""
def add(num_1, num_2):
    return num_1 + num_2

print("------------------------------")
print("By adding 4 and 5, I'm expecting it to be 9, and the result is")
print(add(4, 5))


"""
subtract function
takes the parameters num_1 and num_2
returns the result of subtracting num_2 from num_1
"""
def subtract(num_1, num_2):
    return num_1 - num_2

print("------------------------------")
print("By subtracting 3 from 10, I'm expecting it to be 7, and the result is")
# check by calling the function with the arguments 10 and 3:
print(subtract(10,3))


"""
multiply function
takes the parameters num_1 and num_2
returns the result of multiplying num_1 and num_2
"""
# create the multiply function:
def multiply(num_1,num_2):
    return num_1 * num_2

print("------------------------------")
# replace _ with your own values and expectation:
print("By multiplying 3 and 4, I'm expecting it to be 12, and the result is")
# check by invoking the function with your own values:
print(multiply(3,4))


"""
divide function
takes the parameters num_1 and num_2
returns the resulting of dividing num_1 by num_2
"""
# define the divide function:
def divide(num_1,num_2):
    return num_1 / num_2
print("------------------------------")
# replace _ with your own values and expectation:
print("By dividing 10 by 5, I'm expecting it to be 2, and the result is")
# check by calling the function with your own arguments:
print(divide(10,5))


# === NICE! CONTINUE =================

"""
length_of_string function
takes a parameter str
returns the length of str (number of characters, including spaces and punctuation)
"""
def str_length(string):
    return len(string)

print("------------------------------")
print("By calculating the length of the string 'How now, brown cow?', I'm expecting it to be 19, and the result is")
print(str_length('How now, brown cow?'))


"""
join_string function
takes the parameters str_1 and str_2
returns str_1 and str_2 joined as one string
"""
def combine(str_1,str_2):
    return str_1 + " " + str_2

print("------------------------------")
print("By joining the strings 'go do' and 'good', I'm expecting it to be 'go do good', and the result is")
print(combine("go do","good"))


"""
add_string_as_number function
takes the parameters str_1 and str_2
returns the result of adding str_1 and str_2 as ints
"""
def addstr(str_1,str_2):
    return int(str_1) + int(str_2)

print("------------------------------")
print("By adding the strings '58' and '42' as numbers, I'm expecting it to be 100, and the result is")
print(addstr("58","42"))


"""
number_to_full_name function
takes a parameter month (int)
returns the full name of the month
"""

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
month = 0
def number_to_full_name(month):
     return months[month]

# Sometimes, it's relevant to check the function with different values:
print("------------------------------")
print("By converting 1 to the full month name, I'm expecting it to be 'January', and the result is")
print(number_to_full_name(1))

print("------------------------------")
print("By converting 3 to the full month name, I'm expecting it to be 'March', and the result is")
print(number_to_full_name(3))

print("------------------------------")
print("By converting 9 to the full month name, I'm expecting it to be 'September', and the result is")
print(number_to_full_name(9))


"""
number_to_short_month_name function
takes a parameter month (int)
returns the short name of the month
"""
# HINT: Could you use `number_to_full_name` by calling it from within this function?
def number_to_short_month_name(month):
    return number_to_full_name(month)[0:3]

print("------------------------------")
print("By converting 2 to the short month name, I'm expecting it to be 'Feb', and the result is")
print(number_to_short_month_name(2))

print("------------------------------")
print("By converting 4 to the short month name, I'm expecting it to be 'Apr', and the result is")
print(number_to_short_month_name(4))

print("------------------------------")
print("By converting 10 to the short month name, I'm expecting it to be 'Oct', and the result is")
print(number_to_short_month_name(10))


# === EXTENSIONS =====================

"""
volume_of_cube function
takes a parameter length_of_side
returns the volume of a cube with that length_of_side
"""
# def cube(length_of_side):
#     return length_of_side * length_of_side * length_of_side

def cube(length_of_side):
    return length_of_side**3

# def cube(length_of_side):
#     return pow(length_of_side, 3)

print("------------------------------")
print("By calculating the volume of a cube with the side of 3, I'm expecting it to be 27, and the result is")
print(cube(3))


"""
string_reverse function
takes a parameter str
returns the result of reversing the str
"""
def el_reverso(str_1):
    return str_1[::-1]
print("------------------------------")
print("By reversing the string 'Scotland', I'm expecting it to be 'dnaltocS', and the result is")
print(el_reverso("Scotland"))


# Write a function that converts fahrenheit to celcius (rounded to 2 decimal places):
"""

"""

# def fah_cel_calc(fah_1):
#     return(fah_1 - 32) * (5/9)
# fah_value = fah_cel_calc(75)
# fah_round = round(fah_value, 2)

def farenheit_to_celcius_converter(temp_in_f):
    result = (temp_in_f - 32) * (5/9)
    return round(result, 2)

print("------------------------------")
print("By converting 0 fahrenheit to celcius, I'm expecting it to be -17.78, and the result is")
# print(fah_round)
print(farenheit_to_celcius_converter(0))