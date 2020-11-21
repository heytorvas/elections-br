import plotly.graph_objects as go
from util import get_file_json
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
    party_json = get_file_json('data/party.json')

    for row in votes_list:
        coalition = row['coalition']
        coalition.append(row['party'])
        list_position = []
        res = ''
        position_party_candidate = ''

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
    fig.show()


def plot_map_president_year(year):
    data_frame = pd.read_csv('data/df_president_state_{}.csv'.format(year))
    geojson = get_file_json('data/br-geojson.json')
    fig = px.choropleth(data_frame, geojson=geojson, color="Position",
                        locations="State", featureidkey="properties.UF",
                        hover_data=["State", "Position", "Count"]
                    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.write_html('pages/plot_president_state_year_{}.html'.format(year))