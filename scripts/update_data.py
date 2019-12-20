import requests
import json

def run():
    body = {'stationGrpSeq': 'ALL'}
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data=body,
    ).text
    data = json.loads(data)

    # for station_info in data['realtimeList']:
    #     print(station_info['stationName'])

class realtimeData():
    body = {'stationGrpSeq': 'ALL'}
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data=body,
    ).text
    data = json.loads(data)


