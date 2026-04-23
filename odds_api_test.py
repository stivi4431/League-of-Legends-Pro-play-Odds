import requests

API_KEY = "eM9YZzw4eGKAS8iVRtpVyPbhbzYaCW3so-lAWkU61p3rMR-jB_8"

response = requests.get(
    "https://api.pandascore.co/lol/matches/upcoming",
    params={"token": API_KEY, "per_page": 100}
)

matches = response.json()

lec_matches = []

for m in matches:
    if m["league"]["name"] == "LEC":
        lec_matches.append(m)

for m in lec_matches:
    for i in range(len(m["opponents"])):
        print(m["opponents"][i]["opponent"]["name"])