my_first_dictionary = {}
# my_first_dictionary = dict()

meals = {
        "breakfast":"eggs",
        "lunch":"pasta",
        "dinner":"fish"
        }

#print(meals)

#print(meals["breakfast"])
# print(meals["supper"])
# ^ creates a KeyError as there is no key "supper"

meals["supper"] = "beans"
#print(meals)

meals["dinner"] = "salad"
#print(meals)

del(meals["breakfast"])
#print(meals)
# above to delete a key+value

person_names = {
    "Rob":33,
    "Jim":25,
    "Richard":62,
    "Torres":6201
}

person_names["Steven"] = 44

print(person_names)

person_names["Torres"] = 6202

del(person_names["Jim"])

print(person_names)

print(person_names["Torres"])

print(person_names.keys())

print(person_names.values())

countries = {
    "UK":{"capital":"London",
          "population":1000,
          },
    "Germany":{
        "capital":"Berlin",
        "population":200,
          },
    "Switzerland":{
        "Capital":"Bern",
        "population":23451122,
        }
}

print(countries)

germany_population = countries["Germany"]["population"]
print(germany_population)

# nested dictionaries^

# silly_thing = {
#     1: "2",
#     "three": 1,
#     4: False
# }

# print(silly_thing)


avengers = {
    "Ironman":{
        "Name":"Tony Stark",
        "Attacks":{
            "punch":10,
            "kick":100
        }
    },
    "Hulk":{
        "Name":"Bruce Banner",
        "Attacks":{
            "smash":1000,
            "roll":500
        }
    }
}

hulk_smash = avengers["Hulk"]["Attacks"]["smash"]
print(hulk_smash)