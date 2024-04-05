import json
import pandas as pd
from pandas import json_normalize

from supabase import create_client, Client

url: str = "https://gwqnevtnmqmlqwgyvtqb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3cW5ldnRubXFtbHF3Z3l2dHFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEzMzgxNzksImV4cCI6MjAyNjkxNDE3OX0.4rcu3MU6w258JYbjcX2PvtIcVd8xIAmOekJoDeyBYZQ"

# filtered_df = df[df['season'] >= 5]

def create_dataframe(supabase_url, supabase_key):

  supabase: Client = create_client(supabase_url, supabase_key)

  player_stats = supabase.table('player_stats') \
    .select('*') \
    .eq('season_id', 20212022) \
    .order('points', desc=True) \
    .limit(1005) \
    .execute()

  df = pd.DataFrame(player_stats.data)

  players = supabase.table('players') \
    .select('*') \
    .limit(4000) \
    .order('name', desc=True) \
    .execute()
  
  df1 = pd.DataFrame(players.data)

  # Merge the player_stats DataFrame with the players DataFrame
  merged_df = pd.merge(df, df1, on='player_id', how='inner')
  
  return merged_df
  
df = create_dataframe(url, key)

print(df)