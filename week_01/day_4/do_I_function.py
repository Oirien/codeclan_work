
deimos = {
    "ship_class": "Deimos",
    "hitpoints": 500,
    "armor": 12,
    "weapon":{
        "weapon_name": "Tungsten Railgun",
        "weapon_damage": 50,
        "weapon_penetration": 10
    }
}
# Create a dictionary for ship one
valkyrie = {
    "ship_class": "Valkyrie",
    "hitpoints": 300,
    "armor": 7,
    "weapon":{
        "weapon_name": "Plasma Missile",
        "weapon_damage": 90,
        "weapon_penetration": 3
    }
}
# Create a dictionary for ship two

# define a function that returns the value for HP
def HP_lookup(ship_id):
    for stats in ship_id:
        return stats["hitpoints"]
    
print(HP_lookup(deimos))
# define a function that returns the value for Damage

# define a function that returns the value for Armor

# define a function that takes two ships, one firing on the other, and calculating damage dealt, and hp reamining.