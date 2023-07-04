jarrod_hungry = True
jarrod_tired = True

hangry = jarrod_hungry and jarrod_tired
raining = True

if hangry and raining:
    print("Jarrod is miserable!")
elif hangry:
    print("Jarrod is hangry!")
elif jarrod_hungry or jarrod_tired:
    print("Jarrod is grumpy!")