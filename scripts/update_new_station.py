import requests
import json
from community.models import Station

class run():
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data={'stationGrpSeq': 'ALL'},
    ).text
    data = json.loads(data)

    count = 0
    for info in data['realtimeList']:
        if Station.objects.filter(stationId=info['stationId']):
            pass
        else:
            print(info['stationName'] + " 정류소 없음")
            Station(stationName=info['stationName'], stationId=info['stationId'], latitude=info['stationLatitude'], longitude=info['stationLongitude'], parkingBikeTotCnt=info['parkingBikeTotCnt']).save()
            count += 1

    if count == 0:
        print("추가된 정류소 없음.")
    else:
        print(str(count) + "개의 정류소 추가됨.")