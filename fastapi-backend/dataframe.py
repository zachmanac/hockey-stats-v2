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
  
  sorted_final_df = final_df.sort_values(by=['season_id', 'points', 'goals', 'assists'], ascending=[False, False, False, False])

  return sorted_final_df
    
df = create_dataframe(url, key)

print(df)