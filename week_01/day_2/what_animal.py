# Ask user "give me an animal"
# Store user input into variable of animal
# If animal is "penguin" 
#    THEN PRINT "This is my favourite animal!"
# END

animal_as_user_typed = input("Give me an animal! ")
animal = animal_as_user_typed.lower()

if animal == "penguin":
    print("This is my favourite animal!")
elif animal == "dog":
    print("Dogs are pretty cool!")
else:    
    print("Not my favourite animal:(")

# animal = input("what's your fav animal? ")

# match animal:
#     case "penguin":
#         print("fav animal")
#     case "dog":
#         print("dogs r cool")
#     case other:
#         print("boo u suck")
#
#cleaner syntax but less reliable