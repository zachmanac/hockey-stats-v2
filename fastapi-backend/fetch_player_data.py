from supabase import create_client, Client
import requests

url: str = "https://cserpqafduzvhzigjtwa.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNzZXJwcWFmZHV6dmh6aWdqdHdhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA1NDgxODUsImV4cCI6MjA1NjEyNDE4NX0.sKjF8KmoymgWVnisaHRDxKesibIZHReNTyVXdThY6p0"
supabase: Client = create_client(url, key)

# range(0, max amount of player in hundreds, increment step(should be 100))
# change `season_id` for different season

def fetch_player_data():
    player_data = []
    season_id = 20232024

    for n in range(0, 1100, 100):
        url = f"https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={n}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C={season_id}%20and%20seasonId%3E={season_id}"
        response = requests.get(url)
        if response.status_code == 200:
            player_data.extend(response.json()['data'])
        else:
            return {"error": "Unable to fetch player data"}
    return player_data

def insert_player_data(player_data):
    for player in player_data:
        print("player: ", player)

        player_info = {
            'player_id': player['playerId'],
            'name': player['skaterFullName'],
            'position': player['positionCode']
        }

        players_data, players_count = supabase.table('players').upsert([player_info]).execute()
        
        player_stats = {
            'player_id': player['playerId'],
            'games_played': player['gamesPlayed'],
            'goals': player['goals'],
            'assists': player['assists'],
            'points': player['points'],
            'season_id': player['seasonId'],
            'ev_goals': player['evGoals'],
            'ev_points': player['evPoints'],
            'faceoff_win_percent': player['faceoffWinPct'],
            'game_winning_goals': player['gameWinningGoals'],
            'ot_goals': player['otGoals'],
            'penalty_minutes': player['penaltyMinutes'],
            'plus_minus': player['plusMinus'],
            'points_per_game': player['pointsPerGame'],
            'pp_goals': player['ppGoals'],
            'pp_points': player['ppPoints'],
            'sh_goals': player['shGoals'],
            'sh_points': player['shPoints'],
            'shooting_percent': player['shootingPct'],
            'shots': player['shots'],
            'time_on_ice_per_game': player['timeOnIcePerGame']
        }

        stats_data, stats_count = supabase.table('player_stats').upsert([player_stats]).execute()

insert_player_data(fetch_player_data())