celestial_objects = {
    "Sirius": 25,
    "Andromeda Galaxy": 100000,
    "Jupiter": 0.00006,
    "Pleiades": 100,
    "Orion  Nebula": 1000
}

for obj in celestial_objects.items():
    print(obj[0])

luminosties = []
for obj in celestial_objects.items():
    luminosties.append(obj[1])

i = 0
while i < len(luminosties):
    if luminosties[i] < 200:
        print(luminosties[i])
    i+= 1


