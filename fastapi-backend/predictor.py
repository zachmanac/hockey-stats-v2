import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from dataframe import create_dataframe
from supabase import create_client, Client

def train_and_predict_for_player(player_id, df):
  # Filter data for the given player
  player_data = df[df['player_id'] == player_id]

  # Check if there's enough data for training
  if len(player_data) < 2:
    print(f"Not enough data available for player {player_id}. Skipping...")
    return None
  
  # Normalize the games_played feature
  player_data['games_played_normalized'] = player_data['games_played'] / 82.0

  # Separate features (predictors) and target variable
  X = player_data[['season_id', 'games_played_normalized']].values # Input features
  y = player_data[['games_played_normalized', 'goals', 'assists']] # Target variable

  # Train-test split
  # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Train linear regression model
  model = LinearRegression()
  model.fit(X, y)

  # Predict for the next season
  next_season_id = 20222023
  next_season_data = [[next_season_id, 1.0]]
  predictions = model.predict(next_season_data)

  # Inverse transform to get the predicted games played
  predicted_games_played = predictions[0][0] * 82.0

  # Return player ID and predictions
  return player_id, predicted_games_played, predictions[0][1], predictions[0][2]

def predict_for_all_players(df):
  unique_players = df['player_id'].unique()
  predictions_list = []

  for player_id in unique_players:
        predictions = train_and_predict_for_player(player_id, df)
        if predictions is not None:
            predictions_list.append(predictions)

  return predictions_list
   
def main():
    
  url: str = "https://gwqnevtnmqmlqwgyvtqb.supabase.co"
  key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3cW5ldnRubXFtbHF3Z3l2dHFiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTEzMzgxNzksImV4cCI6MjAyNjkxNDE3OX0.4rcu3MU6w258JYbjcX2PvtIcVd8xIAmOekJoDeyBYZQ"

  supabase = create_client(url, key)

  df = create_dataframe(url, key)

  # Predict goals, assists, games played for all players
  predictions = predict_for_all_players(df)

  # Print predictions for all players
  for prediction in predictions:
    player_id = int(prediction[0])
    predicted_games_played = prediction[1]
    predicted_goals = prediction[2]
    predicted_assists = prediction[3]

    try:
        # Insert prediction into Supabase
        supabase.table('predicted_stats').insert([
            {'player_id': player_id, 'games_played': predicted_games_played,
             'goals': predicted_goals, 'assists': predicted_assists}
        ]).execute()
        print(f"Prediction for Player ID {player_id} inserted into the database.")
    except TypeError as e:
        print(f"Error inserting prediction for Player ID {player_id}: {e}")

if __name__ == "__main__":
  main()