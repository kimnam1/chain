import requests
import json
from community.models import Station

class run():
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data={'stationGrpSeq': 'ALL'},
    ).text
    data = json.loads(data)

    count1 = 0
    count2 = 0
    new_station = {}
    for info in data['realtimeList']:
        if Station.objects.filter(stationId=info['stationId']):
            print(info['stationName'] + " 있음")
            count2 += 1
        else:
            print(info['stationName'] + " 정류소 없음!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            Station(stationName=info['stationName'], stationId=info['stationId'], latitude=info['stationLatitude'], longitude=info['stationLongitude'], parkingBikeTotCnt=info['parkingBikeTotCnt']).save()
            count1 += 1
            new_station.__new__(info['stationName'])

    if count1 == 0:
        print("추가된 정류소 없음.")
        print("총 " + str(count2) + "개 정류소")
    else:
        print(str(count1) + "개의 정류소 추가됨.")