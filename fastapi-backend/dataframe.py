from supabase import create_client, Client

url: str = "https://gwqnevtnmqmlqwgyvtqb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3cW5ldnRubXFtbHF3Z3l2dHFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEzMzgxNzksImV4cCI6MjAyNjkxNDE3OX0.4rcu3MU6w258JYbjcX2PvtIcVd8xIAmOekJoDeyBYZQ"



# filtered_df = df[df['season'] >= 5]

def create_dataframe(supabase_url, supabase_key):

  supabase: Client = create_client(supabase_url, supabase_key)

  