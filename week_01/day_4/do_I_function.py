
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
    return ship_id["hitpoints"]

# define a function that returns the value for Damage
def DMG_lookup(ship_id):
    return ship_id["weapon"]["weapon_damage"]

def armor_lookup(ship_id):
    return ship_id["armor"]


def penetration_lookup(ship_id):
    return ship_id("weapon_penetration")

def ship_firing(ship_1, ship_2):
    return(HP_lookup(ship_1) - (((armor_lookup(ship_1)-penetration_lookup(ship_2)) * 0.1) *DMG_lookup(ship_2)))
    
print(ship_firing(deimos, valkyrie))
# define a function that returns the value for Armor

# define a function that takes two ships, one firing on the other, 
# and calculating damage dealt, and hp reamining.