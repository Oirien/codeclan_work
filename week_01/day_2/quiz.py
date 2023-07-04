
my_number = 42
value = int(input("What number am I thinking of? "))

while value != my_number:
    if value > my_number:
        print("Too High!")
    else:
        print("Too Low!")
    value = int(input("Nope! try again! "))
print("Congrats!")