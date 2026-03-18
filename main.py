import json

try:
    filename = "statistics.json"
    with open(filename,'r') as file:
        # Loading the JSON file
        data = json.load(file)

# Menu
    print("                                                                   WELCOME TO BASKETBALL PLAYER STATISTICS RANKER")
    print("                                    \nINSTRUCTIONS:")
    print("                                                        THIS PROGRAM HELPS YOU EXAMINE THE TOP 25 PLAYERS IN THE NBA RIGHT NOW.")
    print("                                                            THE PROGRAM WILL ASK YOU TO INPUT A RANK OF A PLAYER OUT OF 25.")
    print("                                 THE PROGRAM WILL THEN PRINT THE STATISTICS OF THAT PLAYER INCLUDING HIS PERFORMANCE EFFICIENCY RATING AND HIS NAME.")
    print("                                            THE PROGRAM WILL THEN RANK THE PLAYER ACCORDING TO THE PLAYER'S PERFORMANCE EFFICIENCY RATING.")

    choice = int(input("\nEnter the rank of the player you want to examine in the top 25: "))

    player_rank = []
    for player in data:
        player_rank.append(player["Rank"])

# Choice Variables
    Top_1 = min(player_rank)
    Top_2 = min(player_rank) + 1
    Top_3 = min(player_rank) + 2
    Top_4 = min(player_rank) + 3
    Top_5 = min(player_rank) + 4
    Top_6 = min(player_rank) + 5
    Top_7 = min(player_rank) + 6
    Top_8 = min(player_rank) + 7
    Top_9 = min(player_rank) + 8
    Top_10 = min(player_rank) + 9
    Top_11 = min(player_rank) + 10
    Top_12 = min(player_rank) + 11
    Top_13 = min(player_rank) + 12
    Top_14 = min(player_rank) + 13
    Top_15 = min(player_rank) + 14
    Top_16 = min(player_rank) + 15
    Top_17 = min(player_rank) + 16
    Top_18 = min(player_rank) + 17
    Top_19 = min(player_rank) + 18
    Top_20 = min(player_rank) + 19
    Top_21 = min(player_rank) + 20
    Top_22 = min(player_rank) + 21
    Top_23 = min(player_rank) + 22
    Top_24 = min(player_rank) + 23
    Top_25 = max(player_rank)

# Multiple Choice System
    if choice == 1:
        for player in data:
            if player["Rank"] == Top_1:
                for x in player.items():
                    print(x)
    elif choice == 2:
        for player in data:
            if player["Rank"] == Top_2:
                for x in player.items():
                    print(x)
    elif choice == 3:
        for player in data:
            if player["Rank"] == Top_3:
                for x in player.items():
                    print(x)
    elif choice == 4:
        for player in data:
            if player["Rank"] == Top_4:
                for x in player.items():
                    print(x)
    elif choice == 5:
        for player in data:
            if player["Rank"] == Top_5:
                for x in player.items():
                    print(x)
    elif choice == 6:
        for player in data:
            if player["Rank"] == Top_6:
                for x in player.items():
                    print(x)
    elif choice == 7:
        for player in data:
            if player["Rank"] == Top_7:
                for x in player.items():
                    print(x)
    elif choice == 8:
        for player in data:
            if player["Rank"] == Top_8:
                for x in player.items():
                    print(x)
    elif choice == 9:
        for player in data:
            if player["Rank"] == Top_9:
                for x in player.items():
                    print(x)
    elif choice == 10:
        for player in data:
            if player["Rank"] == Top_10:
                for x in player.items():
                    print(x)
    elif choice == 11:
        for player in data:
            if player["Rank"] == Top_11:
                for x in player.items():
                    print(x)
    elif choice == 12:
        for player in data:
            if player["Rank"] == Top_12:
                for x in player.items():
                    print(x)
    elif choice == 13:
        for player in data:
            if player["Rank"] == Top_13:
                for x in player.items():
                    print(x)
    elif choice == 14:
        for player in data:
            if player["Rank"] == Top_14:
                for x in player.items():
                    print(x)
    elif choice == 15:
        for player in data:
            if player["Rank"] == Top_15:
                for x in player.items():
                    print(x)
    elif choice == 16:
        for player in data:
            if player["Rank"] == Top_16:
                for x in player.items():
                    print(x)
    elif choice == 17:
        for player in data:
            if player["Rank"] == Top_17:
                for x in player.items():
                    print(x)
    elif choice == 18:
        for player in data:
            if player["Rank"] == Top_18:
                for x in player.items():
                    print(x)
    elif choice == 19:
        for player in data:
            if player["Rank"] == Top_19:
                for x in player.items():
                    print(x)
    elif choice == 20:
        for player in data:
            if player["Rank"] == Top_20:
                for x in player.items():
                    print(x)
    elif choice == 21:
        for player in data:
            if player["Rank"] == Top_21:
                for x in player.items():
                    print(x)
    elif choice == 22:
        for player in data:
            if player["Rank"] == Top_22:
                for x in player.items():
                    print(x)
    elif choice == 23:
        for player in data:
            if player["Rank"] == Top_23:
                for x in player.items():
                    print(x)
    elif choice == 24:
        for player in data:
            if player["Rank"] == Top_24:
                for x in player.items():
                    print(x)
    elif choice == 25:
        for player in data:
            if player["Rank"] == Top_25:
                for x in player.items():
                    print(x)

    else:
        print("Not available")


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
