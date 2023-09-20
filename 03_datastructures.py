# Lists
planets = ["Earth", "Mercury", "Venus", "Mars", "Jupiter"]

# Tuples
moon_tup = ("Ganymede", "Titan", "Europa", "Moon")

# Dictionaries
planet_data = {
    "Earth": {"radius_km": 6371, "distance_to_sun_km": 149.6e6},
    "Mars": {"radius_km": 3389, "distance_to_sun_km": 227.9e6},
    "Jupiter": {"radius_km": 69911, "distance_to_sun_km": 778.3e6},
}

# Accessing data from these structures
print(f"List of Planets: {planets[0]}")
print(f"Tuple of Moons: {moon_tup[2]}")
print(f"Radius of Earth: {planet_data['Earth']['radius_km']} km")