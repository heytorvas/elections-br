import requests, json
from bs4 import BeautifulSoup

def set_position(position):
    if 'left-wing' in position:
        return 'left'
    elif 'right-wing' in position:
        return 'right'
    else:
        if '[' in position:
            aux = position.split('[')
            return aux[0]
        else:
            return position

def fix_position(dict_party):
    for i in dict_party:
    
        if i['abbrev'] == 'PCdoB' or i['abbrev'] == 'PT' or i['abbrev'] == 'PSOL':
            i['position'] = 'far-left'
        
        if i['abbrev'] == 'PSDB':
            i['position'] == 'centre-right'

        if i['abbrev'] == 'PSL' or i['abbrev'] == 'PSC' or i['abbrev'] == 'Patriota':
            i['position'] == 'far-right'
    
    return dict_party

url = 'https://en.wikipedia.org/wiki/List_of_political_parties_in_Brazil'

r = requests.get(url).text
bs = BeautifulSoup(r, 'lxml')

table = bs.find('table', {'border': '1'})
tr = table.findAll('tr')

dict_party = []
for line in range(1, len(tr)):
    td = tr[line].findAll('td')

    party = {
        'name': td[0].text.strip(),
        'abbrev': td[2].text.strip(),
        'number': td[3].text.strip(),
        'position': set_position(td[8].text.strip().lower())
    }

    dict_party.append(party)

dict_fix = fix_position(dict_party)

with open ('party.json', 'w') as f:
    f.write(json.dumps(dict_fix))
    f.close()