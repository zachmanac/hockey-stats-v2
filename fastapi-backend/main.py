import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/player/{player_name}")
async def read_player_stats(player_name: str):
    url = "https://api.nhle.com/stats/rest/en/skater/summary"
    params = {
        "isAggregate": "false",
        "isGame": "false",
        "sort": '[{"property":"points","direction":"DESC"},{"property":"goals","direction":"DESC"},{"property":"assists","direction":"DESC"},{"property":"playerId","direction":"ASC"}]',
        "start": 0,
        "limit": 50,
        "factCayenneExp": "gamesPlayed>=1",
        "cayenneExp": "gameTypeId=2 and seasonId<=20232024 and seasonId>=20232024 and skaterFullName likeIgnoreCase '%" + player_name + "%'"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch player"}