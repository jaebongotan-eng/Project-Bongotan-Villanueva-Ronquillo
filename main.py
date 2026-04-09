import json
try:
    filename = "statistics.json"
    with open(filename,'r') as file:
        # Loading the JSON file
        data = json.load(file)
# Menu
        print("\n|------------------------------------------------------------------------------------------------------------------------|")
        print("| WELCOME TO BASKETBALL PLAYER STATISTICS RANKER                                                                         |")
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| THIS PROGRAM HELPS YOU EXAMINE THE TOP 25 PLAYERS IN THE NBA RIGHT NOW.                                                |")
        print("| THE PROGRAM WILL ASK YOU TO INPUT A RANK OF A PLAYER OUT OF 25.                                                        |")
        print("| THE PROGRAM WILL THEN PRINT THE STATISTICS OF THAT PLAYER INCLUDING HIS PERFORMANCE EFFICIENCY RATING AND HIS NAME.    |")
        print("| THE PROGRAM WILL THEN RANK THE PLAYER ACCORDING TO THE PLAYER'S PERFORMANCE EFFICIENCY RATING.                         |")
        print("|------------------------------------------------------------------------------------------------------------------------|")
# Uploading the JSON data to an empty list
    player_rank = []
    for player in data:
        player_rank.append(player["Rank"])
    player_PER = []
    for player in data:
        player_PER.append(player["PER"])
# Choice Variables
    # Sorts The Ranks Of The Players
    player_rank.sort()
    # Puts The Sorted Ranks In Variables
    Top_1 = player_rank[0]
    Top_2 = player_rank[1]
    Top_3 = player_rank[2]
    Top_4 = player_rank[3]
    Top_5 = player_rank[4]
    Top_6 = player_rank[5]
    Top_7 = player_rank[6]
    Top_8 = player_rank[7]
    Top_9 = player_rank[8]
    Top_10 = player_rank[9]
    Top_11 = player_rank[10]
    Top_12 = player_rank[11]
    Top_13 = player_rank[12]
    Top_14 = player_rank[13]
    Top_15 = player_rank[14]
    Top_16 = player_rank[15]
    Top_17 = player_rank[16]
    Top_18 = player_rank[17]
    Top_19 = player_rank[18]
    Top_20 = player_rank[19]
    Top_21 = player_rank[20]
    Top_22 = player_rank[21]
    Top_23 = player_rank[22]
    Top_24 = player_rank[23]
    Top_25 = player_rank[24]
# Input Validation Program
    while True:
        choice = input("\nEnter the rank of the player you want to examine in the top 25 (type 'exit' to leave the search engine): ")
# Multiple Choice System
        if choice == 'exit':
            break
     
        elif choice == '1':
            for player in data:
                if player["Rank"] == Top_1:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[0] >= 30.0:
                print("All-Time Great")
            elif player_PER[0] >= 27.5:
                print("MVP Candidate")
            elif player_PER[0] >= 25.0:
                print("Strong All-Star")
            elif player_PER[0] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[0] >= 15.0:
                print("League Average")
            elif player_PER[0] >= 10.0:
                print("Rotation Player")
            elif player_PER[0] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '2':
            for player in data:
                if player["Rank"] == Top_2:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[1] >= 30.0:
                print("All-Time Great")
            elif player_PER[1] >= 27.5:
                print("MVP Candidate")
            elif player_PER[1] >= 25.0:
                print("Strong All-Star")
            elif player_PER[1] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[1] >= 15.0:
                print("League Average")
            elif player_PER[1] >= 10.0:
                print("Rotation Player")
            elif player_PER[1] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '3':
            for player in data:
                if player["Rank"] == Top_3:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[2] >= 30.0:
                print("All-Time Great")
            elif player_PER[2] >= 27.5:
                print("MVP Candidate")
            elif player_PER[2] >= 25.0:
                print("Strong All-Star")
            elif player_PER[2] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[2] >= 15.0:
                print("League Average")
            elif player_PER[2] >= 10.0:
                print("Rotation Player")
            elif player_PER[2] <= 9.9:
                print("Bench Player/G-League Player")
     
        elif choice == '4':
            for player in data:
                if player["Rank"] == Top_4:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[3] >= 30.0:
                print("All-Time Great")
            elif player_PER[3] >= 27.5:
                print("MVP Candidate")
            elif player_PER[3] >= 25.0:
                print("Strong All-Star")
            elif player_PER[3] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[3] >= 15.0:
                print("League Average")
            elif player_PER[3] >= 10.0:
                print("Rotation Player")
            elif player_PER[3] <= 9.9:
                print("Bench Player/G-League Player")
     
        elif choice == '5':
            for player in data:
                if player["Rank"] == Top_5:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[4] >= 30.0:
                print("All-Time Great")
            elif player_PER[4] >= 27.5:
                print("MVP Candidate")
            elif player_PER[4] >= 25.0:
                print("Strong All-Star")
            elif player_PER[4] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[4] >= 15.0:
                print("League Average")
            elif player_PER[4] >= 10.0:
                print("Rotation Player")
            elif player_PER[4] <= 9.9:
                print("Bench Player/G-League Player")
   
        elif choice == '6':
            for player in data:
                if player["Rank"] == Top_6:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[5] >= 30.0:
                print("All-Time Great")
            elif player_PER[5] >= 27.5:
                print("MVP Candidate")
            elif player_PER[5] >= 25.0:
                print("Strong All-Star")
            elif player_PER[5] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[5] >= 15.0:
                print("League Average")
            elif player_PER[5] >= 10.0:
                print("Rotation Player")
            elif player_PER[5] <= 9.9:
                print("Bench Player/G-League Player")
     
        elif choice == '7':
            for player in data:
                if player["Rank"] == Top_7:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[6] >= 30.0:
                print("All-Time Great")
            elif player_PER[6] >= 27.5:
                print("MVP Candidate")
            elif player_PER[6] >= 25.0:
                print("Strong All-Star")
            elif player_PER[6] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[6] >= 15.0:
                print("League Average")
            elif player_PER[6] >= 10.0:
                print("Rotation Player")
            elif player_PER[6] <= 9.9:
                print("Bench Player/G-League Player")
       
        elif choice == '8':
            for player in data:
                if player["Rank"] == Top_8:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[7] >= 30.0:
                print("All-Time Great")
            elif player_PER[7] >= 27.5:
                print("MVP Candidate")
            elif player_PER[7] >= 25.0:
                print("Strong All-Star")
            elif player_PER[7] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[7] >= 15.0:
                print("League Average")
            elif player_PER[7] >= 10.0:
                print("Rotation Player")
            elif player_PER[7] <= 9.9:
                print("Bench Player/G-League Player")
     
        elif choice == '9':
            for player in data:
                if player["Rank"] == Top_9:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[9] >= 30.0:
                print("All-Time Great")
            elif player_PER[9] >= 27.5:
                print("MVP Candidate")
            elif player_PER[9] >= 25.0:
                print("Strong All-Star")
            elif player_PER[9] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[9] >= 15.0:
                print("League Average")
            elif player_PER[9] >= 10.0:
                print("Rotation Player")
            elif player_PER[9] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '10':
            for player in data:
                if player["Rank"] == Top_10:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[10] >= 30.0:
                print("All-Time Great")
            elif player_PER[10] >= 27.5:
                print("MVP Candidate")
            elif player_PER[10] >= 25.0:
                print("Strong All-Star")
            elif player_PER[10] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[10] >= 15.0:
                print("League Average")
            elif player_PER[10] >= 10.0:
                print("Rotation Player")
            elif player_PER[10] <= 9.9:
                print("Bench Player/G-League Player")
       
        elif choice == '11':
            for player in data:
                if player["Rank"] == Top_11:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[11] >= 30.0:
                print("All-Time Great")
            elif player_PER[11] >= 27.5:
                print("MVP Candidate")
            elif player_PER[11] >= 25.0:
                print("Strong All-Star")
            elif player_PER[11] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[11] >= 15.0:
                print("League Average")
            elif player_PER[11] >= 10.0:
                print("Rotation Player")
            elif player_PER[11] <= 9.9:
                print("Bench Player/G-League Player")
       
        elif choice == '12':
            for player in data:
                if player["Rank"] == Top_12:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[12] >= 30.0:
                print("All-Time Great")
            elif player_PER[12] >= 27.5:
                print("MVP Candidate")
            elif player_PER[12] >= 25.0:
                print("Strong All-Star")
            elif player_PER[12] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[12] >= 15.0:
                print("League Average")
            elif player_PER[12] >= 10.0:
                print("Rotation Player")
            elif player_PER[12] <= 9.9:
                print("Bench Player/G-League Player")
        
        elif choice == '13':
            for player in data:
                if player["Rank"] == Top_13:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[13] >= 30.0:
                print("All-Time Great")
            elif player_PER[13] >= 27.5:
                print("MVP Candidate")
            elif player_PER[13] >= 25.0:
                print("Strong All-Star")
            elif player_PER[13] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[13] >= 15.0:
                print("League Average")
            elif player_PER[13] >= 10.0:
                print("Rotation Player")
            elif player_PER[13] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '14':
            for player in data:
                if player["Rank"] == Top_14:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[14] >= 30.0:
                print("All-Time Great")
            elif player_PER[14] >= 27.5:
                print("MVP Candidate")
            elif player_PER[14] >= 25.0:
                print("Strong All-Star")
            elif player_PER[14] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[14] >= 15.0:
                print("League Average")
            elif player_PER[14] >= 10.0:
                print("Rotation Player")
            elif player_PER[14] <= 9.9:
                print("Bench Player/G-League Player")
     
        elif choice == '15':
            for player in data:
                if player["Rank"] == Top_15:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[15] >= 30.0:
                print("All-Time Great")
            elif player_PER[15] >= 27.5:
                print("MVP Candidate")
            elif player_PER[15] >= 25.0:
                print("Strong All-Star")
            elif player_PER[15] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[15] >= 15.0:
                print("League Average")
            elif player_PER[15] >= 10.0:
                print("Rotation Player")
            elif player_PER[15] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '16':
            for player in data:
                if player["Rank"] == Top_16:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[16] >= 30.0:
                print("All-Time Great")
            elif player_PER[16] >= 27.5:
                print("MVP Candidate")
            elif player_PER[16] >= 25.0:
                print("Strong All-Star")
            elif player_PER[16] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[16] >= 15.0:
                print("League Average")
            elif player_PER[16] >= 10.0:
                print("Rotation Player")
            elif player_PER[16] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '17':
            for player in data:
                if player["Rank"] == Top_17:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[17] >= 30.0:
                print("All-Time Great")
            elif player_PER[17] >= 27.5:
                print("MVP Candidate")
            elif player_PER[17] >= 25.0:
                print("Strong All-Star")
            elif player_PER[17] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[17] >= 15.0:
                print("League Average")
            elif player_PER[17] >= 10.0:
                print("Rotation Player")
            elif player_PER[17] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '18':
            for player in data:
                if player["Rank"] == Top_18:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '19':
            for player in data:
                if player["Rank"] == Top_19:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '20':
            for player in data:
                if player["Rank"] == Top_20:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
       
        elif choice == '21':
            for player in data:
                if player["Rank"] == Top_21:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
     
        elif choice == '22':
            for player in data:
                if player["Rank"] == Top_22:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
      
        elif choice == '23':
            for player in data:
                if player["Rank"] == Top_23:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
        
        elif choice == "24":
            for player in data:
                if player["Rank"] == Top_24:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
        
        elif choice == "25":
            for player in data:
                if player["Rank"] == Top_25:
                    for x in player.items():
                        print(x)
            print("\nRanking:")
            if player_PER[8] >= 30.0:
                print("All-Time Great")
            elif player_PER[8] >= 27.5:
                print("MVP Candidate")
            elif player_PER[8] >= 25.0:
                print("Strong All-Star")
            elif player_PER[8] >= 20.0:
                print("All-Star Boarder")
            elif player_PER[8] >= 15.0:
                print("League Average")
            elif player_PER[8] >= 10.0:
                print("Rotation Player")
            elif player_PER[8] <= 9.9:
                print("Bench Player/G-League Player")
        else:
            print("Please enter 1-25 or 'exit' only")

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
