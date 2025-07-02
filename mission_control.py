mission_duration = 10 #Duration of the mission in hours
fuel_level = 1000 #Initial fuel level in gallons
distance_to_destination = 500000 #Distance to the destination in km
mission_time = 0 #Initialize mission time
fuel_compensation_rate = 50 #gallons per hour
distance_traveled_per_hour = 50000 #km/hr

while mission_time <= mission_duration:
    distance_to_destination -= distance_traveled_per_hour
    fuel_level -= fuel_compensation_rate
    print("Distance to Destination:", distance_to_destination, "Fuel level:", fuel_level, "Mission Time:", mission_time)
    if fuel_level <= 0 or distance_to_destination <= 0:
        break
    mission_time += 1
print("Mission Complete")