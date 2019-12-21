import requests
import json
from community.models import Station

def run():
    data = requests.post(
        url='https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do',
        data={'stationGrpSeq': 'ALL'},
    ).text
    data = json.loads(data)

    for info_saved in Station.objects.all():
        for info_update in data['realtimeList']:
            if info_update['stationId'] == info_saved.stationId:
                alert1 = info_saved.stationName
                alert2 = info_saved.parkingBikeTotCnt
                alert3 = info_update['parkingBikeTotCnt']
                Station.objects.filter(stationId=info_saved.stationId).update(parkingBikeTotCnt=info_update['parkingBikeTotCnt'])
                print(alert1 + " 정류소 " + str(alert2) + "개 -> " + str(alert3) + "개")
    return data



