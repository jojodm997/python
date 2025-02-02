supplies = ["Tent", "sleeping bags", "water", "raspberry pi", "coffe", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows", ]

camp_site = ["Crystal Lake", 404, 89.3, True]
me = supplies[4]
you = supplies[-9]
print(me)
print(you)
print(supplies)

supplies.extend(["toilet pepper", "bidet"])

supplies = supplies + ["toilet pepper", "bidet"]

supplies.insert(0, "popok")

supplies.insert(-1, "pengangguran")

supplies.clear()

atuple = ("fauzan", "hackwell",)

print(type(atuple))

print("This item was jut deleted: " + supplies.pop(0))

supplies.pop(0)

print(supplies)
