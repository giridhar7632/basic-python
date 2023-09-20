# Creating a text file with mission details
with open("missions.txt", "w") as mission_file:
    mission_file.write("Mission: Mars\n")
    mission_file.write("Astronaut: Mark\n")
    mission_file.write("Status: Completed\n")

# Reading and processing data from the file
with open("missions.txt", "r") as mission_file:
    mission_data = mission_file.readlines()

for line in mission_data:
    print(line.strip())
