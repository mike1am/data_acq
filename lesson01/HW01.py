import requests
from dotenv import load_dotenv
import os
load_dotenv()
from pprint import pprint

URL = "https://api.foursquare.com/v3/places/"
INIT_PARAMS = {}
INIT_HEADERS = {
    "Accept": "*/*",
    "Authorization": os.getenv("FS_API_KEY_01")
}

DEF_QUERY = "8 Марта"
DEF_LOCAT = "Климовск"

query = input("Что хотите искать? ") or DEF_QUERY
locat = input("Где хотите искать? ") or DEF_LOCAT

params = INIT_PARAMS.copy()
params['query'] = query
params['near'] = locat
headers = INIT_HEADERS.copy()

srchRes = requests.get(URL + "search", params=params, headers=headers).json()

for n, loc in enumerate(srchRes['results']):
    # detRes = requests.get(URL + "fsq_id", params={'fsq_id': loc['fsq_id']}, headers=headers).json()
    detRes = requests.get(URL + loc['fsq_id'], params={'fields': 'rating'}, headers=headers).json()

    print(
        f"{n + 1}. {loc['name']}\n\t{loc['location']['address']} - {loc['distance']} м",
        # f"\n\tРейтинг: {detRes['rating']}",
        # sep=""
    )
    pprint(detRes)
