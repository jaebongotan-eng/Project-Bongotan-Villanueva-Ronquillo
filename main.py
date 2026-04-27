#Import the json File.
import json

#Create a function that displays the chosen player's stats.
def player_ranking(data, choice):
    players = data[choice - 1]
    print("PLAYER STATS")
    print("=" * 60)

    for key, value in players.items():
        print(f"{key}:{value}")

#Create a function that ranks the chosen player according to their Performance Efficiency Rating.
def player_per(data,choice):
    print("PLAYER RANKING (ACCORDING TO PER)")
    print("=" * 60)
    if data[choice-1]["PER"] >= 30.0:
        print("All-Time Great")
    elif data[choice-1]["PER"] >= 27.5:
        print("MVP Candidate")
    elif data[choice-1]["PER"] >= 25.0:
        print("Strong All-Star")
    elif data[choice-1]["PER"] >= 20.0:
        print("All-Star Borderline")
    elif data[choice-1]["PER"] >= 15.0:
        print("League Average")
    elif data[choice-1]["PER"] >= 10.0:
        print("Rotation Player")
    elif data[choice-1]["PER"] <= 9.9:
        print("Bench Player/G-League Player")

#Create a function that displays the top 25 players ranked according to Points.
def player_pts(data):
    sorted_data=sorted(data, key=lambda player: player["Pts"], reverse=True)#Sort ranks the points in ascending order but reverse puts it in descending.
    for rank, player in enumerate(sorted_data, start=1):#Enumerate function adds a counter for the ranking.
        print(f"{rank}. {player['Name']} = {player['Pts']:.2f} Points")

#Create a function that displays the top 25 players ranked according to Field Goals Made.
def player_fgm(data):
    sorted_data=sorted(data, key=lambda player: player["FGM"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['FGM']:.2f} Field Goals")

#Create a function that displays the top 25 players ranked according to Field Goals Attempted.
def player_fga(data):
    sorted_data=sorted(data, key=lambda player: player["FGA"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['FGA']:.2f} Field Goals")

#Create a function that displays the top 25 players ranked according to Free Throws Attempted.
def player_fta(data):
    sorted_data=sorted(data, key=lambda player: player["FTA"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['FTA']:.2f} Free Throws")

#Create a function that displays the top 25 players ranked according to Free Throws Made.
def player_ftm(data):
    sorted_data=sorted(data, key=lambda player: player["FTM"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['FTM']:.2f} Free Throws")

#Create a function that displays the top 25 players ranked according to Rebounds.
def player_reb(data):
    sorted_data=sorted(data, key=lambda player: player["REB"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['REB']:.2f} Rebounds")

#Create a function that displays the top 25 players ranked according to Assists.
def player_ast(data):
    sorted_data=sorted(data, key=lambda player: player["AST"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['AST']:.2f} Assists")

#Create a function that displays the top 25 players ranked according to Steals.
def player_stl(data):
    sorted_data=sorted(data, key=lambda player: player["STL"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['STL']:.2f} Steals")

#Create a function that displays the top 25 players ranked according to Blocks.
def player_blk(data):
    sorted_data=sorted(data, key=lambda player: player["BLK"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['BLK']:.2f} Blocks")

#Create a function that displays the top 25 players ranked according to Turnovers
def player_tov(data):
    sorted_data=sorted(data, key=lambda player: player["TOV"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['TOV']:.2f} Turnovers")

#Create a function that displays the top 25 players ranked according to Minutes per game.
def player_min(data):
    sorted_data=sorted(data, key=lambda player: player["MIN"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['MIN']:.2f} Minutes")

#Create a function that displays the top 25 players ranked according to Player Efficiency Rating.
def player_per2(data):
    sorted_data=sorted(data, key=lambda player: player["PER"], reverse=True)
    for rank, player in enumerate(sorted_data, start=1):
        print(f"{rank}. {player['Name']} = {player['PER']:.2f}")

#Create a function that gets and displays the average stats of all the top 25 players in the NBA.
def player_average(data):
    total_pts = sum((player["Pts"]) for player in data)
    average_pts = total_pts / len(data)
    total_fgm = sum((player["FGM"]) for player in data)
    average_fgm = total_fgm / len(data)
    total_fga = sum((player["FGA"]) for player in data)
    average_fga = total_fga / len(data)
    total_fta = sum((player["FTA"]) for player in data)
    average_fta = total_fta / len(data)
    total_ftm = sum((player["FTM"]) for player in data)
    average_ftm = total_ftm / len(data)
    total_reb = sum((player["REB"]) for player in data)
    average_reb = total_reb / len(data)
    total_ast = sum((player["AST"]) for player in data)
    average_ast = total_ast / len(data)
    total_stl = sum((player["STL"]) for player in data)
    average_stl = total_stl / len(data)
    total_blk = sum((player["BLK"]) for player in data)
    average_blk = total_blk / len(data)
    total_tov = sum((player["TOV"]) for player in data)
    average_tov = total_tov / len(data)
    total_min = sum((player["MIN"]) for player in data)
    average_min = total_min / len(data)
    total_per = sum((player["PER"]) for player in data)
    average_per = total_per / len(data)

    print(f"Average Points: {average_pts:.2f} Points")
    print(f"Average Field Goals Made: {average_fgm:.2f} Field Goals")
    print(f"Average Field Goals Attempted: {average_fga:.2f} Field Goals")
    print(f"Average Free Throws Attempted: {average_fta:.2f} Field Goals")
    print(f"Average Free Throws Made: {average_ftm:.2f} Free Throws")
    print(f"Average Rebounds: {average_reb:.2f} Rebounds")
    print(f"Average Assists: {average_ast:.2f} Assists")
    print(f"Average Steals: {average_stl:.2f} Steals")
    print(f"Average Blocks: {average_blk:.2f} Blocks")
    print(f"Average Turnovers: {average_tov:.2f} Turnovers")
    print(f"Average Minutes played: {average_min:.2f} Minutes")
    print(f"Average Performance Efficiency Rating: {average_per:.2f}")

#Load the json file.
try:
    filename = "statistics.json"
    with open(filename,'r') as file:
        # Loading the JSON file
        data = json.load(file)
#Menu
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| WELCOME TO BASKETBALL PLAYER STATISTICS RANKER!                                                                         |")
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| THIS PROGRAM HELPS YOU EXAMINE THE TOP 25 PLAYERS IN THE NBA RIGHT NOW.                                                |")
        print("| THE PROGRAM WILL ASK YOU TO INPUT A CHOICE.                                                                            |")
        print("| EXAMINE A SPECIFIC NBA PLAYER'S STATS, THE AVERAGE STATS OF THE TOP 25 PLAYERS, OR RANK THE PLAYERS BY A CHOSEN STAT.  |")
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| IF YOU CHOSE TO EXAMINE A SPECIFIC NBA PLAYER'S STATS, THE FOLLOWING WILL HAPPEN:                                      |")
        print("|--------                                                                                                                |")
        print("|     THE PROGRAM WILL ASK YOU TO INPUT A RANK OF A PLAYER OUT OF 25.                                                    |")
        print("|     THE PROGRAM WILL THEN PRINT THE STATISTICS OF THAT PLAYER INCLUDING HIS PERFORMANCE EFFICIENCY RATING AND HIS NAME.|")
        print("|     THE PROGRAM WILL THEN RANK THE PLAYER ACCORDING TO THE PLAYER'S PERFORMANCE EFFICIENCY RATING.                     |")
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| IF YOU CHOOSE THE SECOND OPTION, THE PROGRAM WILL PRINT THE AVERAGE STATISTICS OF THE TOP 25 PLAYERS (AVERAGE PTS,ETC.)|")
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| IF YOU CHOOSE THE THIRD OPTION, YOU'LL BE ASKED TO SELECT A STAT FOR RANKING (PTS,REB,TOV,ETC...)                      |")
        print("|-------                                                                                                                 |")
        print("|     THE PROGRAM WILL THEN DISPLAY THE NAMES OF PLAYERS RANKED IN ORDER ACCORDING TO THE STAT.                          |")
        print("|------------------------------------------------------------------------------------------------------------------------|")

#Ask the user for choices
    print("\nEnter 1 if you want to examine a specific player")
    print("Enter 2 if you want to get the top 25 players in the NBA according to a specific stat")
    print("Enter 3 if you want to get the average stats of the top 25 players in the NBA")

    while True:
        try:
            choice_one= int(input("\nEnter your choice (1-3): (type 0 to exit) "))

#Add conditional function to identify the user's choice
            if choice_one == 0:
                break

            elif choice_one == 1:
                while True:
                    try:
                        choice = int(input("\nEnter the rank of the player you want to examine in the top 25 (type 0 to return): "))

                        if choice == 0:
                            break

                        elif 0 < choice <= 25:
                            player_ranking(data, choice)
                            print("")
                            player_per(data,choice)

                        else:
                            print("Please enter 1-25 or 0 to return ")


                    except ValueError:
                        print("Invalid! Please enter a digit or 0 to return ")


            elif choice_one == 2:
                print("="*100)
                print("Enter 1 if you want the players to be ranked by Points")
                print("Enter 2 if you want the players to be ranked by Field Goals Made")
                print("Enter 3 if you want the players to be ranked by Field Goals Attempted")
                print("Enter 4 if you want the players to be ranked by Free Throws Attempted")
                print("Enter 5 if you want the players to be ranked by Free Throws Made")
                print("Enter 6 if you want the players to be ranked by Rebounds")
                print("Enter 7 if you want the players to be ranked by Assists")
                print("Enter 8 if you want the players to be ranked by Steals")
                print("Enter 9 if you want the players to be ranked by Blocks")
                print("Enter 10 if you want the players to be ranked by Turnovers")
                print("Enter 11 if you want the players to be ranked by Minutes")
                print("Enter 12 if you want the players to be ranked by Player Efficiency Rating (PER)")
                print("="*100)

                while True:
                    try:
                        choice = int(input("\nEnter your choice (1-12) or 0 to exit: "))
                        if choice == 0:
                            break

                        if choice == 1:
                            print("RANKING ACCORDING TO POINTS")
                            print("="*60)
                            player_pts(data)

                        elif choice == 2:
                            print("RANKING ACCORDING TO FIELD GOALS MADE")
                            print("="*60)
                            player_fgm(data)

                        elif choice == 3:
                            print("RANKING ACCORDING TO FIELD GOALS ATTEMPTED")
                            print("="*60)
                            player_fga(data)

                        elif choice == 4:
                            print("RANKING ACCORDING TO FREE THROWS ATTEMPTED")
                            print("="*60)
                            player_fta(data)

                        elif choice == 5:
                            print("RANKING ACCORDING TO FREE THROWS MADE")
                            print("="*60)
                            player_ftm(data)

                        elif choice == 6:
                            print("RANKING ACCORDING TO REBOUNDS")
                            print("="*60)
                            player_reb(data)

                        elif choice == 7:
                            print("RANKING ACCORDING TO ASSISTS")
                            print("="*60)
                            player_ast(data)

                        elif choice == 8:
                            print("RANKING ACCORDING TO STEALS")
                            print("="*60)
                            player_stl(data)

                        elif choice == 9:
                            print("RANKING ACCORDING TO BLOCKS")
                            print("="*60)
                            player_blk(data)

                        elif choice == 10:
                            print("RANKING ACCORDING TO TURNOVERS")
                            print("="*60)
                            player_tov(data)

                        elif choice == 11:
                            print("RANKING ACCORDING TO MINUTES PLAYED")
                            print("="*60)
                            player_min(data)

                        elif choice == 12:
                            print("RANKING ACCORDING TO PLAYER EFFICIENCY RATING")
                            print("="*60)
                            player_per2(data)

                        else:
                            print("INVALID (enter 1-12 only) or enter 0 to return")


                    except ValueError:
                        print("Invalid! please enter a digit (1-12) or 0 to return")


            elif choice_one == 3:
                print("AVERAGE STATS")
                print("="*60)
                player_average(data)

        except ValueError:
                print("Invalid! please enter 1-3 (enter 0 to exit)")


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")