import requests, json, re
from bs4 import BeautifulSoup

headers = {'X-Requested-With': 'XMLHttpRequest'}

params = {
    'sEcho': '7',
    'iColumns': '6',
    'sColumns': 'name,#,family,latitude,longitude,macroarea',
    'iDisplayStart': '0',
    'iDisplayLength': '1000',
    'mDataProp_0': '0',
    'sSearch_0': '',
    'bRegex_0': 'false',
    'bSearchable_0': 'true',
    'bSortable_0': 'true',
    'mDataProp_1': '1',
    'sSearch_1': '',
    'bRegex_1': 'false',
    'bSearchable_1': 'false',
    'bSortable_1': 'true',
    'mDataProp_2': '2',
    'sSearch_2': '',
    'bRegex_2': 'false',
    'bSearchable_2': 'true',
    'bSortable_2': 'true',
    'mDataProp_3': '3',
    'sSearch_3': '',
    'bRegex_3': 'false',
    'bSearchable_3': 'true',
    'bSortable_3': 'true',
    'mDataProp_4': '4',
    'sSearch_4': '',
    'bRegex_4': 'false',
    'bSearchable_4': 'true',
    'bSortable_4': 'true',
    'mDataProp_5': '5',
    'sSearch_5': '',
    'bRegex_5': 'false',
    'bSearchable_5': 'true',
    'bSortable_5': 'true',
    'sSearch': '',
    'bRegex': 'false',
    'iSortCol_0': '0',
    'sSortDir_0': 'asc',
    'iSortingCols': '1',
    '__eid__': 'Varieties',
    '_': '1680506634195',
}

response0 = requests.get('https://phoible.org/languages', params=params, headers=headers)
params['iDisplayStart'] = '1000'
response1 = requests.get('https://phoible.org/languages', params=params, headers=headers)
params['iDisplayStart'] = '2000'
response2 = requests.get('https://phoible.org/languages', params=params, headers=headers)

data0 = json.loads(response0.text)
data1 = json.loads(response1.text)
data2 = json.loads(response2.text)

lines = ["Name\tCode\tFamily\tArea\n"]

for data in [data0, data1, data2]:
    for el in data['aaData']:
        name  = BeautifulSoup(el[0]).text.strip()
        code  = re.findall(r'([^\/]+$)', BeautifulSoup(el[0]).find_all('a', href=True)[0]['href'])[0].strip()
        family = BeautifulSoup(el[2]).text.strip()
        area = BeautifulSoup(el[5]).text.strip()
        line = "\t".join([name, code, family, area]) + "\n"
        lines.append(line)

with open('familydata.tsv', 'w') as f:
    f.writelines(lines)