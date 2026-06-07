import time
import requests
from pypresence import Presence

app_Id = "1513309358723961022"
RPC = Presence(app_Id)

RPC.connect()


while (True):
    try:
        current_champion = "No Champ Selected"
        current_level = 0
        kills = 0
        deaths = 0
        assists = 0
        cs = 0


        response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify = False)

        daten = response.json()

        summoner_name = daten["activePlayer"]["riotId"]

        for spieler in daten["allPlayers"]:
            if spieler["riotId"] == summoner_name:
                current_champion = spieler["championName"]
                current_level = spieler["level"]
                kills = spieler["scores"]["kills"]
                deaths = spieler["scores"]["deaths"]
                assists = spieler["scores"]["assists"]
                cs = spieler["scores"]["creepScore"]

        print(f'Champion: {current_champion}\nLevel: {current_level}\nKills: {kills}\nDeaths: {deaths}\nAssists: {assists}\nCS: {cs}')
        RPC.update(state="In A Match", details="Test")
    except requests.exceptions.ConnectionError:
        try:
            RPC.update(state="In Main Menu", details="Waiting for Match")
        except Exception:
            pass


    except Exception as randoFehler:
        print("Entweder Discord UND ODER League geschlossen")


    time.sleep(60)