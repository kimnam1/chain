import requests
import json
from community.models import Station

def run():
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data={'stationGrpSeq': 'ALL'},
    ).text
    data = json.loads(data)

    for i in Station.objects.all():
        for f in data['realtimeList']:
            if f['stationId'] == i.stationId:
                alert1 = i.stationName
                alert2 = i.parkingBikeTotCnt
                alert3 = f['parkingBikeTotCnt']
                Station.objects.filter(stationId=i.stationId).update(parkingBikeTotCnt=f['parkingBikeTotCnt'])
                print(alert1 + " 정류소 " + str(alert2) + "개 -> " + str(alert3) + "개")
    return data



