#given a list of strings,
#print out the length of every string in the list

strings = ["apple", "banana", "orange", "kiwi"]

fish = []

# for fruit in strings:
#     print(len(fruit))

def print_length_of_strings(list_of_strings):

    if len(list_of_strings) == 0:
        return

    for word in list_of_strings:
        print(len(word))

print_length_of_strings(strings)

print_length_of_strings(fish)