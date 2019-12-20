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
                Station.objects.filter(stationId=i.stationId).update(parkingBikeTotCnt=f['parkingBikeTotCnt'])
    return data



