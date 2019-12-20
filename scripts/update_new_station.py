import requests
import json
from bicy_stat.models import Station

class run():
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data={'stationGrpSeq': 'ALL'},
    ).text
    data = json.loads(data)

    for info in data['realtimeList']:
        if Station.objects.filter(stationId=info['stationId']):
            pass
        else:
            print(info['stationName'] + "      doesn't exist!")
            Station(name=info['stationName'], stationId=info['stationId'], latitude=info['stationLatitude'], longitude=info['stationLongitude'], parkingBikeTotCnt=info['parkingBikeTotCnt']).save()