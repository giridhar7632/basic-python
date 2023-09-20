# Function to calculate travel time to a planet
def calculate_travel_time(distance_km, spaceship_speed_kmps):
    time_hours = distance_km / spaceship_speed_kmps
    return time_hours


distance_to_mars_km = 225000000
spaceship_speed_kmps = 10000

travel_time_to_mars_hours = calculate_travel_time(
    distance_to_mars_km, spaceship_speed_kmps
)
print(
    f"It will take approximately {travel_time_to_mars_hours:.2f} hours to reach Mars."
)
