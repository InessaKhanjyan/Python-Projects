thrust = input("What is the thrust? ")
mass_flow = input("What is the mass_flow? ")

#thrust = float(input(what is...))

thrust = float(thrust)
mass_flow = float(mass_flow)

specific_impulse = thrust / (mass_flow * 9.81)
exhaust_velocity = specific_impulse * 9.81

print(specific_impulse, exhaust_velocity)