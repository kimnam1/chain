import requests
import json

def run():
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
    ).text
    data = json.loads(data)
    print()
