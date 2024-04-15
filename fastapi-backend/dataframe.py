import pandas as pd
from supabase import create_client, Client

url: str = "https://gwqnevtnmqmlqwgyvtqb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3cW5ldnRubXFtbHF3Z3l2dHFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEzMzgxNzksImV4cCI6MjAyNjkxNDE3OX0.4rcu3MU6w258JYbjcX2PvtIcVd8xIAmOekJoDeyBYZQ"

def create_dataframe(supabase_url, supabase_key):

  supabase: Client = create_client(supabase_url, supabase_key)

  merged_dfs = []

  for season_id in range(20052006, 20222023, 10001):

    # default limit is 1000, limit must be 1004 for 20212022
    player_stats = supabase.table('player_stats') \
      .select('*') \
      .eq('season_id', season_id) \
      .limit(1005) \
      .execute()

    df = pd.DataFrame(player_stats.data)

    players = supabase.table('players') \
      .select('*') \
      .limit(4000) \
      .execute()
    
    df1 = pd.DataFrame(players.data)

    # Merge the player_stats DataFrame with the players DataFrame
    merged_df = pd.merge(df, df1, on='player_id', how='inner')
    merged_dfs.append(merged_df)
    
  final_df = pd.concat(merged_dfs, ignore_index=True)

  # sorted_final_df = final_df.sort_values(by=['season_id', 'points', 'goals', 'assists'], ascending=[False, False, False, False])

  # Filter player data for the 2021-2022 season
  season_2021_2022 = final_df[final_df['season_id'] == 20212022]

  # Get unique player IDs from the 2021-2022 season
  players_2021_2022 = season_2021_2022['player_id'].unique()

  # Filter player data for players who played in the 2021-2022 season
  all_seasons_data = final_df[final_df['player_id'].isin(players_2021_2022)]

  final_df_test = all_seasons_data[['season_id', 'player_id', 'goals', 'assists', 'games_played']][all_seasons_data['games_played'] > 25]

  sorted_final_df = final_df_test.sort_values(by=['season_id', 'goals', 'assists', 'games_played'], ascending=[False, False, False, False])

  return sorted_final_df
    
# df = create_dataframe(url, key)

# print(df)
# print(df[df['season_id'] == 20212022])