from get_votes import *
from build_graph import *
import pandas as pd
import plotly.express as px
from util import *

uf = 'TO'
year = 2016


data_frame = pd.read_csv('data/df_mayor_{}_{}.csv'.format(uf, year))
geojson = get_geojson_state(uf)

fig = px.choropleth(data_frame, geojson=geojson, color="Position",
                    locations="City Code", featureidkey="properties.GEOCODIGO",
                    hover_data=["City", "Position", "Num Votes"]
                )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_html('img/fig1.html')

# tse_codes = get_file_json('data/tse-code-city.json')
# dict_state = []
# for city in tse_codes:
#     if city['uf'] == uf:
#         dict_city = {
#             'name': city['nome_municipio'],
#             'uf': city['uf'],
#             'tse_code': city['codigo_tse'],
#             'ibge_code': city['codigo_ibge']
#         }
#         dict_state.append(dict_city)


# list_city = []
# for city in dict_state:
#     votes_list = get_mayor_votes_list(year, city['tse_code'])

#     votes_count = []
#     for i in votes_list:
#         votes_count.append(int(i['num_votes']))
    
#     major_vote = largest_votes(votes_count)

#     most_votes_candidate = []
#     for i in votes_list:
#         if int(i['num_votes']) == major_vote:
#             most_votes_candidate.append(i)
    
#     votes_list_position = set_position_election(most_votes_candidate)
#     list_city.append(votes_list_position)

#     print(votes_list_position)


# list_city = get_file_json('data/test_state_to.json')

# year_election = []
# city_code = []
# city = []
# num_votes = []
# position = []

# for i in list_city:
#     year_election.append(i['year_election'])
#     city_code.append(i['city_code'])
#     city.append(i['city'])
#     num_votes.append(i['num_votes'])
#     position.append(i['position'])

# cities_json = { 
#     'Year Election': year_election,
#     'City Code': city_code,
#     'City': city,
#     'Num Votes': num_votes, 
#     'Position': position, 
# } 
    
# df = pd.DataFrame(cities_json)
# df.to_csv('data/df_mayor_{}_{}.csv'.format(uf, year), index = False)
# print(df)























# states = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",	
#  	"MG", "PA", "PB", "PR", "PE", "PI",	"RJ", "RN",	"RS", "RO",	"RR", "SC",	
#  	"SP", "SE", "TO"]

# for uf in states:
#     geo_json = get_geojson_state(uf)

#     cities_list = []
#     for i in geo_json['features']:
#         cities_list.append(i['properties']['NOME'].upper())

#     for city in cities_list:
#         code = get_tse_code(uf, city)
#         if str(code) == 'None':
#             print("{}/{} - {}".format(city, uf, code))