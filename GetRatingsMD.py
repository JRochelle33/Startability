import json
import requests

# Note: static URL is for 'week 1', TODO: Make week dynamic
baseUrl = 'https://ratings-api.ea.com/v2/entities/madden-nfl-21?filter=iteration:week-1&sort=overall_rating:DESC,firstName:ASC&limit=20&offset='
catalog = []
i = 0
offset = 0



# Iterate get requests for all player data (20 players per iteration), add each iteration's data to catalog
while i < 96:
    data = requests.get(baseUrl + str(offset))
    catalog = catalog + data.json()['docs']
    offset = offset + 20
    i = i + 1

# Create .txt file and write catalog to it
with open('RatingsMD.txt', 'w') as f:
  json.dump(catalog, f, ensure_ascii=False, indent=4)