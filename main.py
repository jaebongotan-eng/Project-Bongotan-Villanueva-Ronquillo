import json
try:
    filename = "statistics.json"
    with open(filename,'r') as file:
        # Loading the JSON file
        data = json.load(file)
# Menu
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| WELCOME TO BASKETBALL PLAYER STATISTICS RANKER                                                                         |")
        print("|------------------------------------------------------------------------------------------------------------------------|")
        print("| THIS PROGRAM HELPS YOU EXAMINE THE TOP 25 PLAYERS IN THE NBA RIGHT NOW.                                                |")
        print("| THE PROGRAM WILL ASK YOU TO INPUT A CHOICE.                                                                            |")
        print("| EXAMINE A SPECIFIC NBA PLAYER'S STATS, THE AVERAGE STATS OF THE TOP 25 PLAYERS, OR RANK THE PLAYERS BY A CHOSEN STAT.  |")
        print("| IF YOU CHOSE TO EXAMINE A SPECIFIC NBA PLAYER'S STATS, THE FOLLOWING WILL HAPPEN:                                      |")
        print("|     THE PROGRAM WILL ASK YOU TO INPUT A RANK OF A PLAYER OUT OF 25.                                                    |")
        print("|     THE PROGRAM WILL THEN PRINT THE STATISTICS OF THAT PLAYER INCLUDING HIS PERFORMANCE EFFICIENCY RATING AND HIS NAME.|")
        print("|     THE PROGRAM WILL THEN RANK THE PLAYER ACCORDING TO THE PLAYER'S PERFORMANCE EFFICIENCY RATING.                     |")
        print("| IF YOU CHOOSE THE SECOND OPTION, THE PROGRAM WILL PRINT THE AVERAGE STATISTICS OF THE TOP 25 PLAYERS (AVERAGE PTS,ETC.)|")
        print("| IF YOU CHOOSE THE THIRD OPTION, YOU'LL BE ASKED TO SELECT A STAT FOR RANKING (PTS,REB,TOV,ETC...)                      |")
        print("|     YOU THE PROGRAM WILL THEN DISPLAY THE NAMES OF PLAYERS RANKED IN ORDER ACCORDING TO THE STAT.                      |")
        print("|------------------------------------------------------------------------------------------------------------------------|")

    def player_ranking(player):
        players = player[choice-1]
        print players
    

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
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")
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
        elif choice == '2':
            for player in data:
                if player["Rank"] == Top_2:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")
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
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")
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
        elif choice == '4':
            for player in data:
                if player["Rank"] == Top_4:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")
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
        elif choice == '5':
            for player in data:
                if player["Rank"] == Top_5:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
   
        elif choice == '6':
            for player in data:
                if player["Rank"] == Top_6:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
     
        elif choice == '7':
            for player in data:
                if player["Rank"] == Top_7:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
       
        elif choice == '8':
            for player in data:
                if player["Rank"] == Top_8:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
     
        elif choice == '9':
            for player in data:
                if player["Rank"] == Top_9:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '10':
            for player in data:
                if player["Rank"] == Top_10:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
       
        elif choice == '11':
            for player in data:
                if player["Rank"] == Top_11:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
       
        elif choice == '12':
            for player in data:
                if player["Rank"] == Top_12:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
        
        elif choice == '13':
            for player in data:
                if player["Rank"] == Top_13:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '14':
            for player in data:
                if player["Rank"] == Top_14:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
     
        elif choice == '15':
            for player in data:
                if player["Rank"] == Top_15:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '16':
            for player in data:
                if player["Rank"] == Top_16:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '17':
            for player in data:
                if player["Rank"] == Top_17:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '18':
            for player in data:
                if player["Rank"] == Top_18:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '19':
            for player in data:
                if player["Rank"] == Top_19:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
      
        elif choice == '20':
            for player in data:
                if player["Rank"] == Top_20:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
       
        elif choice == '21':
            for player in data:
                if player["Rank"] == Top_21:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
     
        elif choice == '22':
            for player in data:
                if player["Rank"] == Top_22:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
        elif choice == '23':
            for player in data:
                if player["Rank"] == Top_23:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
        
        elif choice == "24":
            for player in data:
                if player["Rank"] == Top_24:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
        
        elif choice == "25":
            for player in data:
                if player["Rank"] == Top_25:
                    print(f"Name: {player["Name"]}")
                    print(f"Team: {player["Team"]}")
                    print(f"Points: {player["Pts"]}")
                    print(f"Rebounds: {player["REB"]}")
                    print(f"Assists: {player["AST"]}")
                    print(f"Blocks: {player["BLK"]}")
                    print(f"Steals: {player["STL"]}")
                    print(f"FGM: {player["FGM"]}")
                    print(f"FGA: {player["FGA"]}")
                    print(f"FTA: {player["FTA"]}")
                    print(f"FTM: {player["FTM"]}")
                    print(f"TOV: {player["TOV"]}")
                    print(f"MIN: {player["MIN"]}")
                    print(f"PER: {player["PER"]}")
                    print(f"\nRank: {player["Rank"]}")

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
        else:
            print("Please enter 1-25 or 'exit' only")

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
