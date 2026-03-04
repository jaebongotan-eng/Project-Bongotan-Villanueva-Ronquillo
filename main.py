import json

try:
    filename = "statistics.json"
    with open(filename,'r') as file:
        # Loading the JSON file
        data = json.load(file)

# Menu
    print("WELCOME TO BASKETBALL PLAYER STATISTICS RANKER")
    print("INSTRUCTIONS:")
    print("THIS PROGRAM HELPS YOU EXAMINE THE TOP 25 PLAYERS IN THE NBA RIGHT NOW.")
    print("THE PROGRAM WILL ASK YOU TO INPUT A RANK OF A PLAYER OUT OF 25.")
    print("THE PROGRAM WILL THEN PRINT THE STATISTICS OF THAT PLAYER INCLUDING HIS PERFORMANCE EFFICIENCY RATING AND HIS NAME.")
    print("THE PROGRAM WILL THEN RANK THE PLAYER ACCORDING TO THE PLAYER'S PERFORMANCE EFFICIENCY RATING.")

    choice = int(input("Enter the rank of the player you want to examine in the top 25:"))

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")