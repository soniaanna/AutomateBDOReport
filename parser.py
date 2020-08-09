import csv
import requests
import json


class Pojazd:
    def __init__(self, marka, rok, masa, masa2):
        self.marka = marka
        self.rok = rok
        self.masa = masa
        self.masa2 = masa2

    def insert_Pojazd(self):
        url = 'https://rejestr-bdo.mos.gov.pl/Report/WasteReport/TableD8_1/CreateVehicleAcceptedToDismantlingStation'
        data = {"vehicleName": f"{self.marka}", "productionYear": f"{self.rok}", "curbMass": f"{self.masa}",
                "endOfLifeVehicleMass": f"{self.masa2}",
                "isCompleted": "true", "dismantlingStationId": f"{credentials.dismantlingStationId}}",
                "reportId": f"{credentials.reportId}}"}
        data_json = json.dumps(data)
        cookie= "XXX" #taken from existing browser session
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
                   'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.5',
                   'Referer': f'https://rejestr-bdo.mos.gov.pl/Report/WasteReport/TableD8_1/{credentials.reportId}/DismantlingStation/{credentials.dismantlingStationId}}/Vehicle/Create',
                   'Content-Type': 'application/json; charset=utf-8', 'Origin': 'https://rejestr-bdo.mos.gov.pl',
                   'DNT': '1', 'Connection': 'keep-alive', 'Cookie': f'{cookie}',
                   'TE': 'Trailers'}

        r = requests.post(url, data=data_json, headers=headers)
        print(r.status_code)
        print(r.text)
        return r


pojazdy = list()

with open('pojazdy.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')
    for row in csvReader:
        marka = row[0]
        rok = row[1]
        masa = row[2]
        masa2 = row[3]
        pojazdy.append(Pojazd(marka, rok, masa, masa2))

for pojazd in pojazdy:
    print(pojazd.marka,pojazd.rok,pojazd.masa,pojazd.masa2)
    try:
        pojazd.insert_Pojazd()
    except:
        print('An error occurred.')
