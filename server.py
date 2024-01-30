import pandas as pd

def match_players_save_matching_credit(file1_path, file2_path, output_csv_path):
    # Read CSV files into DataFrames
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Create an empty list to store matching rows
    matching_rows_data = []

    # Iterate through each row in File 1 and check for matching player names and Total Credit in File 2
    for index, row1 in df1.iterrows():
        file1_players = set([player.strip() for player in row1['Players'].split(',')])
        file1_total_credit = row1['Total Credit']

        # Check for matching rows in File 2 based on player names and Total Credit
        match_rows = df2[
            (df2['Players'].apply(lambda x: all(player in [p.strip() for p in x.split(',')] for player in file1_players))) &
            (df2['Total Credit'] == file1_total_credit)
        ]

        # If there is a match, append the matching row to the list
        if not match_rows.empty:
            matching_rows_data.append({'File1_Row': index + 1, 'Matched_Players': ', '.join(file1_players), 'Total_Credit': file1_total_credit})

            # Print the matching details
            print(f"Matching players in File 1 Row {index + 1} with File 2:")
            print(file1_players)
            print(f"Total Credit in File 1 Row {index + 1}: {file1_total_credit}")
            print("Matched rows in File 2:")
            print(match_rows)
            print("\n")
        else:
            # Print if there is no match
            print(f"No match found for players in File 1 Row {index + 1}")
            print(file1_players)
            print(f"Total Credit in File 1 Row {index + 1}: {file1_total_credit}")
            print("\n")

    # Create a DataFrame from the list of matching rows
    matching_rows_df = pd.DataFrame(matching_rows_data)

    # Save the matching rows to a CSV file
    matching_rows_df.to_csv(output_csv_path, index=False)
    print(f"Matching rows saved to {output_csv_path}")

# Replace 'file1.csv', 'file2.csv', and 'output_matching_rows.csv' with your actual file paths
match_players_save_matching_credit('fantasy_teams1.csv', 'fantasy_teams.csv', 'output_matching_rows.csv')
