import plotly.graph_objects as go
from util import *
import pandas as pd
import plotly.express as px
from collections import Counter

def check_counter_position_repeated(counter_position):
    rev_dict = {} 
    for key, value in counter_position.items(): 
        rev_dict.setdefault(value, set()).add(key) 
      
    result = [values for key, values in rev_dict.items() if len(values) > 1]
    return list(result)

def set_position_election(votes_list):
    party_json = get_file_json('assets/party.json')

    for row in votes_list:
        coalition = row['coalition']
        coalition.append(row['party'])
        list_position = []
        res = ''
        position_party_candidate = 'unknown'

        for i in coalition:
            for party in party_json:
                if party['abbrev'] == i:
                    list_position.append(party['position'])
                if party['abbrev'] == row['party']:
                    position_party_candidate = party['position']

        counter_position = dict(Counter(list_position))
        result = check_counter_position_repeated(counter_position)

        if len(result) > 0:
            res = position_party_candidate

        else:
            res = max(counter_position, key= lambda x: counter_position[x]) 

        row.update({'position': res}) 

    return votes_list

def set_position_election_only(votes_list):
    party_json = get_file_json('assets/party.json')

    coalition = votes_list['coalition']
    coalition.append(votes_list['party'])
    list_position = []
    res = ''
    position_party_candidate = 'unknown'

    for i in coalition:
        for party in party_json:
            if party['abbrev'] == i:
                list_position.append(party['position'])

            if party['abbrev'] == votes_list['party'].strip().replace(' ', ''):
                position_party_candidate = party['position']

    counter_position = dict(Counter(list_position))
    result = check_counter_position_repeated(counter_position)

    if len(result) > 0:
        res = position_party_candidate

    else:
        res = max(counter_position, key= lambda x: counter_position[x]) 

    votes_list.update({'position': res})
    return votes_list

def get_count_position(votes_list_position):
    far_left = 0
    left = 0
    centre_left = 0
    centre = 0
    centre_right = 0
    right = 0
    far_right = 0
    unknown = 0

    for row in votes_list_position:
        if row['position'] == 'far-left':
            far_left += int(row['num_votes'])
        
        elif row['position'] == 'left':
            left += int(row['num_votes'])

        elif row['position'] == 'centre-left':
            centre_left += int(row['num_votes'])

        elif row['position'] == 'centre':
            centre += int(row['num_votes'])

        elif row['position'] == 'centre-right':
            centre_right += int(row['num_votes'])

        elif row['position'] == 'right':
            right += int(row['num_votes'])

        elif row['position'] == 'far-right':
            far_right += int(row['num_votes'])

        else:
            unknown += int(row['num_votes'])

    count_position = {
        'far-left': far_left,
        'left': left,
        'centre-left': centre_left,
        'centre': centre,
        'centre-right': centre_right,
        'right': right,
        'far-right': far_right,
        'unknown': unknown
    }

    return count_position

def show_plot(count):
    labels = [i for i in count.keys()]
    values = [j for j in count.values()]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.write_html('pages/plot_especific.html')

def set_color(position):
    if(position == 'far-left'):
        return "maroon"
    elif(position == 'left'):
        return "red"
    elif(position == 'centre-left'):
        return "darkred"
    elif(position == 'centre'):
        return "slateblue"
    elif(position == 'centre-right'):
        return "royalblue"
    elif(position == 'right'):
        return "blue"
    elif(position == 'far-right'):
        return "midnightblue"
    else:
        return "grey"

def plot_map_president_year(year):
    data_frame = pd.read_csv('data/df_president_state_{}.csv'.format(year))
    geojson = get_file_json('assets/br-geojson.json')
    title = "Ideological Position Based of Each State of Brazil on Presidential Election in {}".format(year)

    fig = px.choropleth(data_frame, geojson=geojson, color="Position",
                        locations="State", featureidkey="properties.UF",
                        hover_data=["State", "Position"])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    fig.write_html('pages/plot_mayor_state_{}.html'.format(year))

def plot_mayor_state_year(uf, year):
    data_frame = pd.read_csv('data/df_mayor_{}_{}.csv'.format(uf, year))
    geojson = get_geojson_state(uf)

    fig = px.choropleth(data_frame, geojson=geojson, color="Position",
                        locations="City Code", featureidkey="properties.GEOCODIGO",
                        hover_data=["City", "Position", "Num Votes"]
                    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    fig.write_html('pages/plot_mayor_{}_{}.html'.format(uf, year))