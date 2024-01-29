import pandas as pd

def match_players_save_matching_credit(file1_path, file2_path, output_csv_path):
    # Read CSV files into DataFrames
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Create an empty list to store matching rows
    matching_rows_data = []

    # Iterate through each row in File 1
    for index1, row1 in df1.iterrows():
        file1_players = set([player.strip() for player in row1['Players'].split(',')])
        file1_total_credit = row1['Total Credit']

        # Iterate through each row in File 2
        for index2, row2 in df2.iterrows():
            file2_players = set([player.strip() for player in row2['Players'].split(',')])
            
            # Check if player names in File 1 Row match with player names in File 2 Row
            if file1_players == file2_players:
                matching_rows_data.append({'File1_Row': index1 + 1, 'File2_Row': index2 + 1, 'Players': ', '.join(file1_players), 'Total Credit': file1_total_credit})

                # Print the matching details
                print(f"Matching players in File 1 Row {index1 + 1} with File 2 Row {index2 + 1}:")
                print(file1_players)
                print("\n")

    # Create a DataFrame from the list of matching rows
    matching_rows_df = pd.DataFrame(matching_rows_data)

    # Save the matching rows to a CSV file
    matching_rows_df.to_csv(output_csv_path, index=False)
    print(f"Matching rows saved to {output_csv_path}")
    
# Replace 'fantasy_teams1.csv', 'fantasy_teams.csv', and 'output_matching_rows.csv' with your actual file paths
match_players_save_matching_credit('fantasy_teams.csv', 'fantasy_teams1.csv', 'output_matching_rows.csv')
