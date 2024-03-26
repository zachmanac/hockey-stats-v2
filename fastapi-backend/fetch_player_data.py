import requests

# n = start condition for list of players
# change after `seasonId%3E=` for different season

def fetch_player_data():
    player_data = []

    for n in range(0, 900, 100):
        url = f"https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={n}&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20232024%20and%20seasonId%3E=20232024"
        response = requests.get(url)
        if response.status_code == 200:
            player_data.append(response.json())
        else:
            return {"error": "Unable to fetch player data"}
    return player_data

fetch_player_data()