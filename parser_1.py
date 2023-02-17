import csv
import requests
import json
import credentials


class Pojazd:
    def __init__(self, marka, rok, masa, masa2, isCompleted):
        self.marka = marka
        self.rok = rok
        self.masa = masa
        self.masa2 = masa2
        self.isCompleted = isCompleted

    def insert_Pojazd(self):
        url = 'https://rejestr-bdo.mos.gov.pl/Report2022/WasteReport/TableD8_1/CreateVehicleAcceptedToDismantlingStation'
        data = {"vehicleName": f"{self.marka}", "productionYear": f"{self.rok}", "curbMass": f"{self.masa}",
                "endOfLifeVehicleMass": f"{self.masa2}",
                "isCompleted": f"{self.isCompleted}", "dismantlingStationId": f"{credentials.dismantlingStationId}",
                "reportId": f"{credentials.reportId}"}
        data_json = json.dumps(data)
        cookie= "XXX" #taken from existing browser session
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
                   'Accept': '*/*', 'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                   'Referer': f'https://rejestr-bdo.mos.gov.pl/Report/WasteReport/TableD8_1/{credentials.reportId}/DismantlingStation/{credentials.dismantlingStationId}/Vehicle/Create',
                   'Content-Type': 'application/json; charset=utf-8', 'Origin': 'https://rejestr-bdo.mos.gov.pl',
                   'DNT': '1', 'Cookie': f'{cookie}',
                   'Cache-Control': 'max-age=0',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'sec-gpc': '1'}
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
        isCompleted="true" if row[4]=="t" else "false" 
        pojazdy.append(Pojazd(marka, rok, masa, masa2, isCompleted))

for pojazd in pojazdy:
    print(pojazd.marka,pojazd.rok,pojazd.masa,pojazd.masa2,pojazd.isCompleted)
    try:
        pojazd.insert_Pojazd()
    except:
        print('An error occurred.')
        exit()
